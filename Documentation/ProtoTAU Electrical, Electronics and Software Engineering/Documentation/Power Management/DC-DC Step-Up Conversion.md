---
tags:
  - Power
  - PCB
date:
  - 2023-11-01
authors: 
  - Christine Koppel
---

#### MOSFETs Assumptions
The maximum current we can pass through the MOSFET is dependent on the thermal design and breakdown voltage maximum designed amount. We need to estimate the power dissipation of the MOSFET and make sure we can provide sufficient cooling using a heatsink or a fan. MOSFET power dissipation is related to the on- resistance $R_{ds}$ and the current.
Thus, we need to seek from the specification sheets which can tolerate the voltage and has the lowest possible $R_{ds}$ and higher $V_{gs}$.

Other useful reading:
[Understanding Power MOSFET Parameters](https://www.taiwansemi.com/assets/uploads/productcategoryfile/AN-1001_A1611.pdf)


# 5V - 12V - Solenoid Valve Rail

## Theoretical 
## Load Transient Waveform 
![[amCharts (1).png]]
Reading this graph, we can see that at the minimum the output voltage from the conversion is 11.78V and, at the maximum, 12.15. 
### MOSFET Selection
#### IQDH35N03LM5CGATMA1
[The following datasheet](https://www.mouser.co.uk/datasheet/2/196/Infineon_DS_IQDH35N03LM5CG_2_1-3197486.pdf)shows that it's $R_{ds}$ is 0.35mΩ, which currently the lowest available and sold MOSFET with lower $R_{ds}$.

## PCB Schematic
![[Pasted image 20231102121851.png]]



# 12V - 48V - Motor Power Rail

## Theoretical 
### MOSFET Selection
#### IPTC039N15NM5ATMA1
[The following datasheet](https://www.mouser.co.uk/datasheet/2/196/Infineon_IPTC039N15NM5_DataSheet_v02_01_EN-3165633.pdf)shows that it's $R_{ds}$ is 0.35mΩ, which currently the lowest available and affordable MOSFET with lower $R_{ds}$.

## PCB Schematic
![[Pasted image 20231102125448.png]]
