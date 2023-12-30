---
tags:
  - Introductory
  - Slides
  - Meeting
date:
  - 2023-08-18
authors: 
  - Christine Koppel
---

# Introduction
---
## Goals (informal)
- Get the PCB actually done and assembled.
- Document as much as we could and *should*.
- Make it future-proof
- Get a system created so Data and Telemetry people have something to actually do and should.
---
## Goals (formal)
- Finish the KiCAD schematic of the electronics
- Check up the PCB creation and ask for feedback from professors.
- Waiting the delivery of the components and assembly tools
- Agree on the foundation how we will design the system
- [Follow the proposed plan and adapt it without much sacrifice](Gantt%20Chart.xlsx)
---
## Optional goals
- Unify our documentation in own made home server and host the webserver for it (Obsidian).
- [Learn how to make our own motor (for people who have courses in this especially ie. MechElec, EEE and Electrical Engineers)](BrushlessPermanentMagnetMotorDesignVersion2.pdf)
---
## Risks and "Elephants in the room"
- Does the motor ***actually*** work.
- Some solutions are now in purely followed by datasheets and thus we may or may not know the reality of the matters at hand.
- We may need to have to outsource ourselves to other teams as they also need EEES advice on the matters.
---
# System

---
## Charging System
![](Pasted%20image%2020231009144032.png)
[Documentation](https://www.analog.com/media/en/technical-documentation/data-sheets/MAX17701.pdf)

---
## Voltage Step-Up

![](Pasted%20image%2020231009144406.png)
[Documentation](https://www.ti.com/lit/ds/symlink/lm5122.pdf?ts=1677148436094)

[Power Bench](https://webench.ti.com/power-designer/)

---
## Phase Controller

![](Pasted%20image%2020231009145106.png)
[Documentation](https://www.analog.com/media/en/technical-documentation/data-sheets/ltc7061.pdf)

[Simulation LTSpice](Draft1.asc)


---
## Logic Controller

![](Pasted%20image%2020231009145903.png)

[Inverter Documentation](https://www.ti.com/lit/ds/symlink/sn74lvc1g14.pdf)

[AND-Gate Documentation](https://assets.nexperia.com/documents/data-sheet/74HC_HCT08.pdf)

---
## Pulse Width Controller
![](Pasted%20image%2020231009150127.png)

[Modulator Documentation](https://www.analog.com/media/en/technical-documentation/data-sheets/LTC6992-1-6992-2-6992-3-6992-4.pdf)

[Digital Potentiometer Documentation](https://cdn-learn.adafruit.com/downloads/pdf/ds3502-i2c-potentiometer.pdf)

---
## Microcontroller and I2C 

![](Pasted%20image%2020231009155547.png)

[Microcontroller Documentation](https://datasheets.raspberrypi.com/pico/pico-datasheet.pdf)

[Active Terminator](https://learn.adafruit.com/adafruit-ltc4311-i2c-extender-active-terminator/overview)

---
### Questions?

---
### Post-Meeting Report
 - Two attendants, Johnathan and Dawid.
 - Got the confirmation of that members can join in committee meetings as the observers. 

