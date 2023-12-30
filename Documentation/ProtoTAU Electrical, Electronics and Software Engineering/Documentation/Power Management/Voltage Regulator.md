---
tags:
  - Power
  - PCB
date:
  - 2023-10-30
authors: 
  - Christine Koppel
---

# Model
Texas Instruments
[TPS7A85 - High-Current (4A), High-Accuracy (1%), Low-Noise (4.4 μVRMS), LDO Voltage Regulator](https://www.ti.com/lit/ds/symlink/tps7a85.pdf?ts=1698150512304&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FTPS7A85)

# 5V - 4A Output
## Calculations
### [Output Voltage](https://www.ti.com/lit/ds/symlink/tps7a85.pdf?ts=1698150512304&ref_url=https%253A%252F%252Fwww.ti.com%252Fproduct%252FTPS7A85#%5B%7B%22num%22%3A155%2C%22gen%22%3A0%7D%2C%7B%22name%22%3A%22XYZ%22%7D%2C0%2C469.3%2C0%5D)
The TPS7A85 can either be used with the internal ANY-OUT network or by using external resistors. Using the ANY-OUT network allows the TPS7A85 to be programmed from 0.8 V to 3.95 V. To extend this output voltage range to 5.0 V, external resistors must be used. 
$V_{out} = V_{NR/SS}*(1+R_1/R_2)$ where $V_{NR/SS} = 0.8V$

Using an R1 of 12.1 kΩ is recommended to optimize the noise and PSRR.

We are going to design the voltage regulator to output 5V and 4A.
$5V = 0.8V * (1 + 12.1kΩ/R_2)$
Solve for $R_2$ , $R_2 = - \frac{R_1*V_{NR/SS}}{V_{NR/SS}-V_{out}}$
$R_2 = - \frac{12.1kΩ*0.8V}{0.8V-5V} = 2304.761905Ω ≈ 2.3kΩ$ 

### Noise
#### Feed-Forward Capacitor ($C_{ff}$)
Quoting the documentation:
- *Although a feed-forward capacitor ($C_{ff}$) from the FB pin to the OUT pin is not required to achieve stability, a 10-nF external feed-forward capacitor optimizes the transient, noise, and PSRR performance. A higher capacitance $C_{ff}$ can be used; however, the start-up time is longer and the power-good signal can incorrectly indicate that the output voltage is settled. To ensure proper Power-Good (PG) functionality the time constant defined by $C_{NR/SS}$  must be greater than or equal to the time constant from the $C_{ff}$*

We are going to use a 100nF feed-forward capacitor. 


#### Noise-Reduction and Soft-Start Capacitor ($C_{NR/SS}$)
Quoting the following documentation:
- *To achieve a monotonic start-up, the TPS7A85 error amplifier tracks the voltage ramp of the external soft-start capacitor until the voltage approaches the internal reference. The soft-start ramp time depends on the soft-start charging current $I_{NR/SS}$, the soft-start capacitance $C_{NR/SS}$, and the internal reference $V_{NR/SS}$. Soft-start ramp time can be calculated with: $t_{ss} = (V_{NR/SS}*C_{NR/SS})/I_{NR/SS}$*, where $I_{NR/SS}$ has typical value of 6.2 µA and $V_{NR/SS}$.

For low-noise applications, a 10-nF to 1-µF $C_{NR/SS}$ is recommended per documentation.

We are going to use a 500nF capacitor, to reduce the noise the most sensible amount as possible, as this voltage rail-line is used by sensors, which could and can affect the accuracy of the data plots. Also it ensures the proper Power-Good (PG) as it is larger than feed-forward capacitor. 

Thus the soft-ramp time calculated per the chosen capacitor is...
$$$t_{ss} = (0.8V*500nF)/6.2 µA = 65ms$$
#### Power-Good 
Quoting the documentation:
- *The power-good circuit monitors the voltage at the feedback pin to indicate the status of the output voltage. When the feedback pin voltage falls below the PG threshold voltage $(V_{IT(PG)} + V_{HYS(PG)})$, typically 89.3%), the PG pin open-drain output engages and pulls the PG pin close to GND. When the feedback voltage exceeds the $V_{IT(PG)}$ threshold by an amount greater than $V_{HYS(PG)}$ (typically 91.3%), the PG pin becomes high impedance. By connecting a pullup resistor to an external supply, any downstream device can receive power-good as a logic signal that can be used for sequencing. Make sure that the external pullup supply voltage results in a valid logic signal for the receiving device or devices*
- *The lower limit of 10 kΩ results from the maximum pulldown strength of the power-good transistor, and the upper limit of 100 kΩ results from the maximum leakage current at the power-good node. If the pullup resistor is outside of this range, then the power-good signal may not read a valid digital logic level.*

Per documentation sheet, the power good resistor should be between 10kΩ to 100kΩ.

A strong low resistance pull-down resistor is used to make noise voltages smaller, because noise currents from unintended coupling and EMI will be filtered out.
A weak high resistance pull-down resistor is used to make the amount of required current smaller to power the device as it works less against the resistor, thus last longer, parts can be smaller and don't get as hot.

Taking that to account, as this vehicle has to focus on the energy efficiencies and has limited power to run the entire system, thus the high resistance pull-down resistor is used, but close to the limit, as we would like to still eliminate the noise in the sensing equipment. We are going to use the 80kΩ pulldown resistor as the power-good resistor.

#### Input ($C_{in}$)and Output ($C_{out}$) Capacitor Requirements 

As per documentation:
 - *The TPS7A85 is designed and characterized for operation with ceramic capacitors of 47 µF or greater (22 μF or greater of effective capacitance) at the output and 10 µF or greater (5 μF or greater of effective capacitance) at the input. Using at least a 47-µF capacitor is highly recommended at the input to minimize input impedance. Place the input and output capacitors as near as practical to the respective input and output pins to minimize trace parasitics. If the trace inductance from the input supply to the TPS7A85 is high, a fast current transient can cause VIN to ring above the absolute maximum voltage rating and damage the device. This situation can be mitigated by additional input capacitors to dampen the ringing and to keep the ringing below the device absolute maximum ratings.*

We are going to use 50nF for both capacitors.

## PCB Schematic
![[Pasted image 20231101143227.png]]
#### To be completed:
- Getting an answer from Fuel Cell & Safety on the voltage requirements of the valves
- Practical PCB design considerations
