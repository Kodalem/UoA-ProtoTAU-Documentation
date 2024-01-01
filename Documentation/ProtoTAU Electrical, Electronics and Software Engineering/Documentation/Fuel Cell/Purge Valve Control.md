---
authors: Christine Koppel
tags:
  - Rust
  - Safety Critical
  - Chemistry
date:
  - 2023-12-27
---

# Purge Valve Control

> [!info]
> <span style="color: #e3e00a;"> <i class="fa-regular fa-copyright fa-spin"></i></span> Because of the whole documentation of the hydrogen fuel cell manual being, alas, confidential, following documentation has opaque description and explaination. If the following manual of the FC-X-®-1020ACS Fuel Cell Stack is acquired, this following section will start to make sense. 

## Technical Constraints

### Power 

Summary of the working principles of the hydrogen fuel cell performance, the following parameters determine the performance and power of the engine.

| Current                                                     | Voltage                 | Efficiency                                                                          | Reliability                                                                  |
|-------------------------------------------------------------|-------------------------|-------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| Larger Load <i class="fa-solid fa-arrow-up-right-dots"></i> | Lower voltage per cell <i class="fa-solid fa-arrow-down-long"></i> | Bigger loss due to heat  <i class="fa-solid fa-arrow-down-long"></i>                | Danger of clogging of the system <i class="fa-solid fa-arrow-down-long"></i> |
| Smaller load <i class="fa-solid fa-arrow-down-long"></i>    | More voltage per cell <i class="fa-solid fa-arrow-up-right-dots"></i>  | Bigger efficiency due to less heat <i class="fa-solid fa-arrow-up-right-dots"></i>  | Less chances of clogging <i class="fa-solid fa-arrow-up-right-dots"></i>                                                    |

### Cooling

Due to wanting to prevent further potential clogging and better performance at the very least 280$m^3$ of airflow. 
For this, we are going to attach two [NF-20-A 5V with PWM Noctua(tm) fans,](https://noctua.at/en/nf-a20-5v-pwm/specification) which will give us in full power 293.8$m^3$ of airflow in total.

## Working Principle

The hydrogen fuel cell works by the principle of cyclical flow of hydrogen in short bursts with longer variable pauses - hence 'purging'.
The short burst will be the constant time of recommendation of about 2000 milliseconds, and the purge wait period is depended on the desired and designed current load of the system, which for this case will be at around 25 amps due to the super-capacitor charger having maximum designed input current load of 20 amps - extra current applied to due the lack of knowledge and future-proofing the wear and tear of the fuel cell engine.
This lower-end current of the designed 75 amps, will give us considerable efficiency and reliability gains.

For the startup purge, the time opening window and stop cycle is given to be short to enable the flow of hydrogen in the capacitive membranes of the vehicle, providing with increase of current of the system. After the startup sequence, following the desired current calculations and flow window, the system will systematically start to provide consistent amount of current.

During this process the microcontroller will output the status of the valves in UART towards another microcontroller dealing with wireless transmitting the data.

## Code
Following code snippet is from the following [Github repository](https://github.com/Kodalem/Ballard-1020ACS-Fuel-Cell-Stack-Control/tree/master).

```rust
#![no_std]
#![no_main]

use bme680::*;
use bsp::entry;
use core::fmt;
use core::fmt::Write;
use core::time::Duration;
use defmt::*;
use defmt_rtt as _;

use embedded_hal::blocking::delay;
use embedded_hal::blocking::delay::DelayMs;
use embedded_hal::blocking::i2c;
use embedded_hal::digital::v2::OutputPin;
use embedded_hal::digital::v2::ToggleableOutputPin;
use panic_probe as _;
// Pull in any important traits
use rp_pico::hal::prelude::*;

use cortex_m::delay::Delay;
use hal::gpio::Pins;
use hal::multicore::{Multicore, Stack};

// A shorter alias for the Hardware Abstraction Layer, which provides
// higher-level drivers.
use rp_pico::hal;

// Provide an alias for our BSP so we can switch targets quickly.
// Uncomment the BSP you included in Cargo.toml, the rest of the code does not need to change.
use rp_pico as bsp;
// use sparkfun_pro_micro_rp2040 as bsp;

use bsp::hal::{
    clocks::{init_clocks_and_plls, Clock},
    fugit::RateExtU32,
    pac,
    sio::Sio,
    uart::{DataBits, StopBits, UartConfig},
    watchdog::Watchdog,
};
use rp_pico::hal::bsp_pins;

/// Stack for core 1
///
/// Core 0 gets its stack via the normal route - any memory not used by static
/// values is reserved for stack and initialised by cortex-m-rt.
/// To get the same for Core 1, we would need to compile everything seperately
/// and modify the linker file for both programs, and that's quite annoying.
/// So instead, core1.spawn takes a [usize] which gets used for the stack.
/// NOTE: We use the `Stack` struct here to ensure that it has 32-byte
/// alignment, which allows the stack guard to take up the least amount of
/// usable RAM.
static mut CORE1_STACK: Stack<4096> = Stack::new();

fn current_purge_calculation(desired_current: u32) -> u32 {
    // Check if the current is under the fuel cell limit (75Amps)
    if desired_current <= 75 {
        let purge_time: u32 = (2300 * 1000) / desired_current;
        // Return the purge time
        return purge_time;
    } else {
        // Print an error message and throw an error
        crate::panic!("Desired current is over the fuel cell limit of 75Amps!");
    }
}

#[entry]
fn main() -> ! {
    info!("Program start");
    let mut pac = pac::Peripherals::take().unwrap();
    let core = pac::CorePeripherals::take().unwrap();
    let mut watchdog = Watchdog::new(pac.WATCHDOG);
    let mut sio = Sio::new(pac.SIO);

    // External high-speed crystal on the pico board is 12Mhz
    let external_xtal_freq_hz = 12_000_000u32;
    let clocks = init_clocks_and_plls(
        external_xtal_freq_hz,
        pac.XOSC,
        pac.CLOCKS,
        pac.PLL_SYS,
        pac.PLL_USB,
        &mut pac.RESETS,
        &mut watchdog,
    )
    .ok()
    .unwrap();

    let mut delay = cortex_m::delay::Delay::new(core.SYST, clocks.system_clock.freq().to_Hz());

    let pins = bsp::Pins::new(
        pac.IO_BANK0,
        pac.PADS_BANK0,
        sio.gpio_bank0,
        &mut pac.RESETS,
    );

    // Multi-core setup
    let mut mc = Multicore::new(&mut pac.PSM, &mut pac.PPB, &mut sio.fifo);
    let cores = mc.cores();
    let core1 = &mut cores[1];

    let uart_pins = (
        // UART TX (characters sent from RP2040) on pin 1 (GPIO0)
        pins.gpio0.into_function(),
        // UART RX (characters received by RP2040) on pin 2 (GPIO1)
        pins.gpio1.into_function(),
    );
    let mut uart = bsp::hal::uart::UartPeripheral::new(pac.UART0, uart_pins, &mut pac.RESETS)
        .enable(
            UartConfig::new(9600.Hz(), DataBits::Eight, None, StopBits::One),
            clocks.peripheral_clock.freq(),
        )
        .unwrap();

    // Configure two pins as being I²C, not GPIO
    let sda_pin = pins.gpio20.into_function::<hal::gpio::FunctionI2C>();
    let scl_pin = pins.gpio21.into_function::<hal::gpio::FunctionI2C>();

    info!("I2C pins configured");

    // Create the I²C driver, using the two pre-configured pins. This will fail
    // at compile time if the pins are in the wrong mode, or if this I²C
    // peripheral isn't available on these pins!
    let i2c = hal::I2C::i2c0(
        pac.I2C0,
        sda_pin,
        scl_pin,
        400.kHz(),
        &mut pac.RESETS,
        &clocks.peripheral_clock,
    );

    info!("I2C driver created");

    // Set the relay control pin
    let mut relay_control_pin = pins.gpio22.into_push_pull_output();

    // Set the desired current (A)
    let desired_current: u32 = 50;
    // Set the purge setup time (ms)
    let purge_setup_time: u32 = 2000;
    // Set the purge duration, it should be less than 500ms
    let purge_duration: u32 = 500;

    // Print the purge valve control setup sequence
    info!("Purge valve control setup sequence");
    // Print the desired current
    info!("Desired current: {}", desired_current);
    // Calculate the purge time
    let purge_time: u32 = current_purge_calculation(desired_current);
    // Print the purge time
    info!("Purge time: {}", purge_time);

    // Print the purge valve startup sequence
    info!("Purge valve startup sequence");

    // Turn on the purge relay
    relay_control_pin.set_high().unwrap();
    // Print the purge relay is on
    info!("Purge relay is on");
    // Send data over UART that the purge relay is on
    writeln!(uart, "ON\r\n").unwrap();
    // Delay for the purge setup time
    delay.delay_ms(purge_setup_time);
    // Turn off the purge relay
    relay_control_pin.set_low().unwrap();
    // Send data over UART that the purge relay is off
    writeln!(uart, "OFF\r\n").unwrap();
    // Print the purge relay is off
    info!("Purge relay is off");

    uart.write_full_blocking(b"UART example\r\n");

    let mut value = 0u32;

    // Start the second core running the communication and temperature measurement loop
    info!("Starting core 1");
    core1
        .spawn(unsafe { &mut CORE1_STACK.mem }, move || {
            // Get the second core's copy of the `CorePeripherals`, which are per-core.
            // Unfortunately, `cortex-m` doesn't support this properly right now,
            // so we have to use `steal`.
            let core = unsafe { pac::CorePeripherals::steal() };
            // Loop the temperature measurement and communication
            loop {}
        })
        .unwrap();

    // Print the purge valve control runtime sequence and loop forever
    info!("Purge valve control runtime sequence");
    loop {
        // Turn on the purge relay
        relay_control_pin.set_high().unwrap();
        // Print the purge relay is on
        info!("Purge relay is on");
        // Send data over UART that the purge relay is on
        writeln!(uart, "ON\r\n").unwrap();
        // Delay for the purge duration
        delay.delay_ms(purge_duration);

        // Turn off the purge relay
        relay_control_pin.set_low().unwrap();
        // Print the purge relay is off
        info!("Purge relay is off");
        // Send data over UART that the purge relay is off
        writeln!(uart, "OFF\r\n").unwrap();
        // Delay for the purge time
        delay.delay_ms(purge_time);
    }
}

// End of file
```

