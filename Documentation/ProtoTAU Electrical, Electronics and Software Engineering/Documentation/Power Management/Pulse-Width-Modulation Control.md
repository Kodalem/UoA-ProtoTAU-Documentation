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
[Adafruit DS3502 I2C Digital Potentiometer](https://cdn-learn.adafruit.com/downloads/pdf/ds3502-i2c-potentiometer.pdf)
[Voltage-Controlled Pulse Width Modulator (PWM) - LTC6992](https://www.analog.com/media/en/technical-documentation/data-sheets/LTC6992-1-6992-2-6992-3-6992-4.pdf)

# Working Principle
## Duty Cycle Control
Duty Cycle is proportional to the voltage applied to the MOD pin, $V_{mod}$ .
$$\textrm{Duty Cycle = D} = \frac{V_{mod}}{0.8V-V_{set}}-\frac{1}{8}$$
*to be elaborated further*
# PCB
![[Pasted image 20231101143337.png]]