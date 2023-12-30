
## Fans
### Preface
Fans have to be 5V and preferably of a high-performance and reliable, which is going to be by [Noctua](https://noctua.at/en/products/fan?connector=12&voltage=5). Fan is used to flow the passive heat made by the driver out of the driving compartment and take new air in.

The intake is going to be Rectangular Trapezoid with a 60mm x 60mm hole for the fan.

The outtake is going to be a 200mm x 200mm hole under the wooden floor.
### Model
[NF-A6x25 5V PWM](https://noctua.at/en/nf-a6x25-5v-pwm) - is to be chosen in the intake design, which has $29.2m^3/h$. airflow.

[NF-A20 5V PWM](https://noctua.at/en/nf-a20-5v-pwm) - is to be chosen in the outtake design which has $146.9m^3/h$ airflow.

#### Dummy Fan Control Code
```python
from machine import Pin, PWM
from time import sleep

led = PWM(Pin(11))
led.freq(1000)

while True:
    for duty in range(0,65535):
        led.duty_u16(duty)
        sleep(0.0001)
```

## Heatsinks

### Heatsink Selection
We are going to consult the wholesalers of the electronics components to provide us with the heatsinks in regards to their specifications we require, such as size and area.
### Thermal Paste Selection
We are going to use [Thermogrizzly Kryonaut](https://www.thermal-grizzly.com/en/products/16-kryonaut-en) to maximise our performance, high-temperature range support and effectiveness of the heatsinks. 
### MOSFET
In the hot components such as MOSFETS, as stated in the [[DC-DC Step-Up Conversion#MOSFETs Assumptions]], we need to provide adequate cooling to the system to maintain its integrity and efficiency. We are going to use the heatsinks on the chips in the system.

## Driver's Comfort
Extra fans near the driver?