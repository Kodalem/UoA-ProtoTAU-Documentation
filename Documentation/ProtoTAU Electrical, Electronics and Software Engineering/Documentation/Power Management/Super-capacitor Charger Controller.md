---
tags:
  - Power
  - PCB
date:
  - 2023-11-01
authors: 
  - Christine Koppel
---
> [!todo]
> - Finalize the PCB Layout and document this here.
> - Select the capacitor component models and double check their rated voltage.
> - Add more inter-links between chapters for better readability and referencing


# Components
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

#### MOSFETs selection

As the maximum input voltage of the design is going to be assumed to be around 40V, the MOSFETS are picked, whomstever has the turn-on time under 150ns and lowest possible $R_{ds}$ 
We choose the [RX3G18BGN Power MOSFET](https://fscdn.rohm.com/en/products/databook/datasheet/discrete/transistor/mosfet/rx3g18bgnc16-e.pdf) in this design, as it the MOSFET that provided us with the lowest possible $R_{ds}$ within the 40V of $V_{DSS}$  and turn on speed of 47ns
#### Base Conditions

$$f_{SW} = 185kHz$$

$$V_{OUT} = 5V$$

$$V_{REF} = 2.5V  $$

$$ESR_{SUP} = 0.14mOhms  $$

As 18 fuel cells are used, and approximate reference voltage per cell around 51.7A load is 0.67 V per cell

$$V_{IN} = \text{18 Fuel Cells} * 0.67V = 12.06V \approx 12V$$

Thus, duty cycle of the super-capacitor charger is $$V_{OUT} / V_{IN}$$...

$$Duty Cycle = 5V / 12V = 0.4166(6)$$

As the hydrogen fuel cell can output at the very least 75 Amps of current, but wanting to stay within efficiency and safety boundaries, the charging current maximum can be assumed to be few magnitudes smaller in the run time.

$$I_{CHGMAX} = 50A$$




#### Switching Frequency and External Clock Synchronization 

The device can be programmed from 125KHz to 2.2MHz by using a resistor $R_{RT/SYNC}$ connected from the RT/SYNC pin to SGND/EP. It can be calculated with the following:

$$R_{RT/SYNC} (kOhm) = \frac{44830}{f_{SW}(KHz)}-1.205$$

If left unconnected, it will operate the device at 350KHz default frequency. 

Fot this design, we will focus on the efficiency gains as per focus of the design, which means that higher frequencies are not desired for this scenario as per [MOSFET switching losses](https://www.ti.com/lit/an/snva399a/snva399a.pdf), but we will sacrifice the component size in the process which we can sacrifice in this scenario as we are dealing with a vehicle.

Thus, we will program the device to run around the 185KHz frequency, which will need to following resistor:

$$R_{RT/SYNC} (kOhm) = \frac{44830}{185(KHz)}-1.205 = 241.119kOhm$$

### Inductor Selection

Three parameters specify the operation of the device: inductance value $L$, direct current resistance $R_{DCR}$ and inductor saturation current $I_{SAT}$. Current ripple ratios is to be assumed to be around 0.3.

The inductance values are calculated with the following:

$$ L1 = \frac{V_{OUT} * (1 - \text{Duty Cycle})} {LIR * I_{CHGMAX} * f_{SW}} $$

$$ L2 = \frac{V_{OUT}}{600000 * I_{CHGMAX}} $$

Thus following the design, the inductance values are:

$$ L1 = \frac{5V * (1 - 0.4166(6))} {0.3 * 50A * 185KHz} = 0.0001051051H = 1.051051 \mu H$$

$$ L2 = \frac{5V}{600000 * 50A} = 0.00000016(6) H = 166.6(6)nH$$

The design recommendation is to use the higher inductance value, which is $L1$ in this case.

#### Component Specific Selection

For this component, [the HC3 Series Power Inductor model HC3-1R0-R](https://www.mouser.ee/datasheet/2/87/cooid00010_181-2264062.pdf) is used, as it gives us the lowest possible  $R_{DCR} = 0.42mOhm$ with inductance of $1.0 \mu H$


### Output Capacitor Selection

In order to reduce voltage ripple across the super capacitor, additional X7R ceramic capacitors are used at the output of the charger, X7R is preferred by the manufacturer's notes due to their stability in temperature variable environments.

To calculate the output capacitance, the following equation is used:

$$ C_{OUT} = \frac{ 25 * I_{CHGMAX} }{ f_{SW} * V_{OUT} } $$

Thus, in the design, the output capacitance is:

$$ C_{OUT} = \frac{ 25 * 50A }{ 185KHz * 5V } = 1.351 mF $$

### Input Capacitor Selection

The input capacitor reduces peak currents drawn from the power source and reduces noise and the voltage ripple on the input caused by the switching converter.

The input capacitor is calculated with the following equation:

$$ C_{VIN} = \frac { I_{CHGMAX}*\text{Duty Cycle}*(1-\text{Duty Cycle}) }{ \text{Efficiency of the converter} * f_{SW} * \Delta V_{IN}} $$


We are going to assume the efficiency of the converter to be 80% and the input voltage ripple to be 2V to guarantee robustness.

Thus, in the design, the input capacitance is:

$$ C_{VIN} = \frac { 50A * 0.4166(6) * (1-0.4166(6)) }{ 0.8 * 185KHz * 2V } = 41.0565\mu F $$

### Operating Input-Voltage Range

The minimum operating voltage is given by two parameter equations:

$$ V_{DCIN (MIN1)} = (\frac{ V_{OUT} + I_{CHGMAX} * (R_{DSON(LS)} + R_{DCR(MAX)} ) }{ 1-(1.05*f_{SW}*(t_{DTHL} + t_{MINONDL(MAX)} )) }) + I_{CHGMAX} * (R_{DSON(HS)} - R_{DSON(LS)} ) $$

$$ V_{DCIN (MIN2)} = V_{OUT} + 2.1V $$ 

The maximum operating voltage is given by the following equation:

$$ V_{DCIN(MAX)} = \frac{V_{OUT}}{1.05*f_{SW} * t_{MINONDH(MAX)}}$$

Where $t_{MINONDH(MAX)}$ is assumed to be absolute worst case scenario of 150ns. 

> [!note]
> It appears that the maximum operating voltage is not a concern for this design, as we use a lower switching frequency.


$$ V_{DCIN(MAX)} = \frac{5V}{1.05*185KHz * 150ns} = 171.6V $$

As the maximum operating voltage is way above the cells count could ever sensibly produce and add to the design, for future proofing and assuming low current run-time of the vehicle, we declare that it's going to be:

$$ V_{DCIN(MAX)} = 40V $$

>[!warning]
> <span style="color: #e3e00a;"> <i class="fa-solid fa-bolt fa-fade"></i> </span> Always assume everything in input is ***40V MAXIMUM*** rated, when designing anything between supercapacitor and super-capacitor charger!

### CC Mode Charging Current

As per design recommendations, the selection of current sense resistor $R_S$ involves trade-offs between power loss and charging current accuracy. 
Told best way to select the current sense resistor is to obtain/assume the voltage drop across the resistor, where the smaller difference between the voltage drops decreases the power loss, but also the accuracy.

We are going to use the smallest recommended voltage difference of $R_S$ to be 25mV which means about +/-8% accuracy, because we are going for the sensible amounts of efficiency in the design - not for precision electronics.


The following equation is used to calculate the current sense resistor:

$$ R_S =  \frac{V_{CSP}-V_{CSN} } { I_{CHGMAX} } = \frac{25mV}{I_{CHGMAX}} = \frac{25mV}{50A} = 500\mu Ohms $$


$V_{ILIM}$ voltage of ILIM pin can be calculated with the following equation next:

$$ V_{ILIM} = 30 * R_S * I_{CHGMAX} = 30 * 500\mu Ohms * 50A =  750mV $$

Resistor divider of $V_{REF}$ to SGND/EP can be used to program $V_{ILIM}$, thus the following equation is used to calculate the resistor divider:

$$R_{LIM1} = 20 * (V_{REF} - V_{ILIM})kOhm = 20 * (2.5V - 0.75V)kOhm = 35kOhms  $$

$$R_{LIM2} = 20 * V_{ILIM}kOhm = 20 * 0.75V = 15kOhm$$

RC filter needs to be connected to preserve the accuracy and bandwidth of the $V_ILIM$ pin. The following equation is used to calculate the RC filter, where $R1$ is 40 ohms for minimal impact on the current sense resistor:

$$C_{RC} = \frac{1}{2*\pi*R1*5*f_{SW}} = \frac{1}{2*\pi*40Ohms*5*185kHz} = 4.301 nF$$

### Setting the Input Undervoltage-Lockout Level (UVLO)

This component has adjustable input undervoltage-lockout levelling using the EV/UVLO pin, which stops the charger operation in the case of the voltage of the system not being in the desired voltage operation level.

To design the UVLO, resistor divider from the DCIN to SGND/EP is connected, which sets the UVLO threshold voltage. The following equation is used to calculate the resistor divider:

$$R_{UVLO1} = 10000 * V_{DCIN(MIN)} =   10000 * 7.1 V = 71000Ohms $$

This sets the voltage at which the device us required to turn on.

Also, the second resistor divider is used to set the hysteresis of the UVLO, which is the difference between the turn-on and turn-off voltages. The following equation is used to calculate the resistor divider, where the threshold voltage of EN/UVLO is $V_{ENABLE_{THRESHOLD}}$ is 1.25V and $I_{EB_{BIAS}} = 3 \mu A$:

$$R_{UVLO2} = \frac{V_{ENABLE_{THRESHOLD}}*R1}{V_{DCIN(MIN)} - V_{ENABLE_{THRESHOLD}} + (I_{EB_{BIAS}} * R1) }  = \frac{1.25V*71000Ohms}{7.1V - 1.25V + (3\mu A * 71000Ohms) } = 14.6 kOhms$$

### Current Regulation Loop Compensation (COMP)

This component has the following feature to tune the current loop control performance of the current mode controller, this selection depends on the chosen inductor and its resistance, current sense resistor, maximum operating input voltage and worst-case maximum ESR of the super-capacitor, the maximum on-resistances of step-down converter MOSFETs.

The compensation resistor is $R_Z$ is calculated with the following equation:

$$R_Z = \frac{3000*L*f_{SW}}{V_{DCIN(MAX)}*R_S} = \frac{3000*1.051051 \mu H*185kHz}{40V*500\mu Ohms } = 29116.7 Ohms $$

The compenstation capacitor $C_Z$ is calculated with the following equation:

$$C_Z = \frac{0.8*L}{R_Z*R_E} = \frac{0.8* 1\mu H}{29116.7Ohms*3.222mOhms}  = 8.528nF$$

Where $R_E$ is calculated with the following.

>[!note]
> In this design process, we have not yet finalized the connection solution, thus we assume the $R_{CONNECTION} $ is assumed to be 1 mOhm.


$$R_E = [R_{DCR}+R_S+ R_{DSONHS}* \text{Duty Control (MAX)} + R_{DSON(LS)} * (1-D_{MIN}) +ESR_{SUP} + R_{CONNECTION}  ] = [0.42mOhm + 500\mu Ohms+ 1.64mOhms * 0.125 + 1.64mOhms * (1 - 0.4166) + 0.14mOhms  + 1mOhms  ] = 3.222mOhms $$


Thus, we can calculate the high frequency pole capacitor $C_P$ using the following equation:

$$C_P = \frac{0.35}{R_Z * f_{SW}} = \frac{0.35}{29116.7 Ohm* 185kHz} = 64.976pF $$

### Setting the Output Voltage and Voltage Regulation Loop (FB)

This component features a FB pin to regulate the voltage across the supercapacitor to the desired level by connecting a feedback resistor divider with the compensating capacitor. 

Calculation of $R_{TOP}$ and $R_{BOT}$ is calculated with the following equations:

$$R_{TOP} = 10 * V_{OUT} * 10^3 = 10 * 5 * 10^3 = 50kOhm $$

$$R_{BOT} = \frac{R_{TOP}}{ \frac {V_{OUT}}{V_{FBREG}} -1 }* 10^3 = \frac{50kOhm}{ \frac {5V}{1.250V} -1}* 10^3 = 16.66(6)kOhm$$

And calculation of compensating capacitor $C_{FB}$



$$C_{FB} =\frac{1}{1.5*10^6*R_{PAR}} = \frac{1}{1.5*10^3*12.5kOhms} = 53.33nF $$


Where $R_{PAR}$ is:

$$R_{PAR} = \frac{R_{TOP}*R_{BOT}}{R_{TOP}+R_{BOT}} = \frac{50kOhm * 16.667MOhm}{50kOhm + 16.667MOhm} = 12.5kOhm$$
### Output Overvoltage Protection


The following component has the following overvoltage detection comparator at the OVI pin, which is setup by the following midpoint of a resistor divider output towards the SGND/EP.

We are suggested to select the resistor at the range of 50kOhm to 100kOhms, which gives us the means to calculate the next resistor in the following equation:

The overvoltage level of the super-capacitors is going to be $2 * V_R = 2.85 * 2 = 5.7 V$ as we connect the supercapacitors in two by two, two in series and two in parallel. The threshhold voltage was given, whjich was to be 1.26V

$$R2 = \frac{R1}{\frac{V_{OUTOV}}{V_{OVITH}}-1} = \frac{50kOhm}{\frac{5.7V}{1.26V}-1} = 14.2kOhm$$

### Bootstrap Capacitor Selection

Bootstrap capacitor capacitance is determined by the high-side MOSFET selection, which is calculated with the following:


$$C_{BST} \ge \frac{\Delta Q_g}{\Delta V_{BST}} = \frac{\text{Total Gate Charge}}{\text{Voltage Variation Allowed}}  = \frac{168nC}{20mV} = 8.4 \mu F$$


### Bootstrap Diode Selection

The following diode should be Shottky type, with the ratings where the reverse voltage rating is over the sum of maximimum input voltage with extra factor of 10V and average forward current rating over 1A.

For this case, we chose the [SK25](https://eu.mouser.com/datasheet/2/849/sk22-3324185.pdf), as it had the lowest available leakage current and forward voltage. 


