---
tags:
  - Power
  - PCB
date:
  - 2023-11-01
authors: 
  - Christine Koppel
---
# Model
[ACS37010 - 450 kHz, High Accuracy Current Sensor
With Zero Current Voltage Reference in SOIC-6 Package](https://www.mouser.co.uk/datasheet/2/1115/ACS37010_Datasheet-3312854.pdf)

***5V Variant, which can run in 4.5-5.5V $V_{CC}$ range! Not the 3.3V!***
## Safety
Fused-lead SOIC-6 package supports 840 $V_{RMS}$  basic isolation and 420 $V_{RMS}$ reinforced isolation, which means that we can surely use it in the 48V 20A rail.
## Analog to Digital Conversion
The microcontroller's built-in ADC converter is used to get the measure current from an analog output signal.
For Raspberry Pi Pico has **12-bit ADC** with a quantization level of **4096**.
### Future improvements
The future inheritor of this project could use a [ADS127L21 512-kSPS, Programmable Filter, 24-Bit, Wideband Delta-Sigma ADC](https://www.ti.com/lit/ds/symlink/ads127l21.pdf?ts=1698839022326&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FADS127L21) or [Ultra-high-resolution 31-bit 4-kSPS 1-channel delta-sigma ADC](https://www.ti.com/lit/ds/symlink/ads1281.pdf?ts=1698762932082&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FADS1281), which can give a more of accurate reading, although it could be an overkill.
## Supply Bypass Capacitor
We are going to use a standard 100nF bypass capacitor on all current sensors..
# Current Sensing 48V 20A Rail
This sensor is used to measure the current from the motor power supply.
![[Pasted image 20231101142940.png]]
# Current Sensing Fuel-Cell Rail
This sensor is used to measure the current from the hydrogen fuel cell.
![[Pasted image 20231101143056.png]]
# Current Sensing 5V 20A Rail
This sensor is used to measure the current from the super-capacitor.
![[Pasted image 20231101142850.png]]

# Code
```rust
TODO: WRITE THE CODE FOR THE ADC MEASUREMENT FOR EACH MICROCONTROLLER
```
