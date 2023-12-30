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
[MAX17701 - 4.5V to 60V, Synchronous Step-Down Supercapacitor Charger Controller](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX17701.pdf)
[Supercapacitor - SkelTec](https://1188159.fs1.hubspotusercontent-na1.net/hubfs/1188159/02-DS-220909-SKELCAP-CELLS-1F.pdf)

# Theory
## Super-capacitor theoretical use time.
Assuming that the super-capacitor is charged into the fullest charge and we don't have any supply current from the hydrogen fuel cell.

The amount of energy that is required to holdup or backup the system:
$$E_{stored}=\frac{1}{\%Effeciency}*Power*Time$$
Flipping this equation in regards to time:
$$Time=\frac{\%Effeciency*E_{stored}}{Power}$$
The stored energy in a capacitor:
$$E_{stored}=\frac{1}{2}*Capacitance*Voltage^2$$
As our design has 6400F total capacitance and 5V output from the 2x2 super-capacitor array. Although the rated voltage is $2*2.85=5.7V$, the output still will be 5V.
$$E_{stored}=\frac{1}{2}*6400F*5V^2=\text{80000 Joules}$$
Thus we get the amount of time the energy could be in use, assuming that we go on full power 1000W of the whole system usage and 80% efficiency.
$$Time=\frac{80\%*\text{80000 Joules}}{1000W_{full-power}} = \text{64 seconds} = \text{1 minute 4 seconds}$$
Assuming we go medium power 700W instead which would be likely the average range of the power consumed.
$$Time=\frac{80\%*\text{80000 Joules}}{700W_{medium-power}} = \text{91 seconds} = \text{1 minute 31 seconds}$$


## MAX17701 Component Selection
%%I, Christine, wish I wasn't dumb last year and not writing this **shit** down%%

### Inductor Selection

### Output Capacitor Selection

### Input Capacitor Selection

### Operating Input-Voltage Range

### CC Mode Charging Current

### Setting the Input Undervoltage-Lockout Level (UVLO)

### Current Regulation Loop Compensation (COMP)

### Setting the Output Voltage and Voltage Regulation Loop (FB)

### Output Overvoltage Protection

### Input Short-Circuit Protection External nMOSFET Selection
The MOSFET used has the turn-off time at 38.9ns, which is under the maximum allowed 150ns.

### Step-Down Converter nMOSFET Selection

