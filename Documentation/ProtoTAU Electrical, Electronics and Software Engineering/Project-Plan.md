---
title: Project Plan for the Second Half Session
author:
- Christine Elizabeth Koppel
fontsize: 10pt
mainfont: DejaVuSerif.ttf
sansfont: DejaVuSans.ttf
monofont: JetBrainsMonoNerdFontMono-Regular.ttf
mathfont: texgyredejavu-math.otf
geometry: left=2.21cm,right=2.21cm,top=2.5cm,bottom=2.5cm
block-headings: true
header-includes:
- \usepackage{fvextra}
- \DefineVerbatimEnvironment{Highlighting}{Verbatim}{breaklines,commandchars=\\\{\}}
- \usepackage{amsmath,amssymb,pgfgantt} 
- \usepackage{xcolor} 
- \newganttchartelement{orangebar}{ orangebar/.style={ inner sep=0pt, draw=red!66!black, very thick, top color=white, bottom color=orange!80 }, orangebar label font=\slshape, orangebar left shift=.1, orangebar right shift=-.1 } 
- \newganttchartelement{bluebar}{ bluebar/.style={ inner sep=0pt, draw=purple!44!black, very thick, top color=white, bottom color=blue!80 }, bluebar label font=\slshape, bluebar left shift=.1, bluebar right shift=-.1 } 
- \newganttchartelement{pinkbar}{ pinkbar/.style={ inner sep=0pt, draw=magenta!40!black, very thick, top color=white, bottom color=magenta!80 }, pinkbar label font=\slshape, pinkbar left shift=.1, pinkbar right shift=-.1 } 
- \newganttchartelement{greenbar}{ greenbar/.style={ inner sep=0pt, draw=green!50!black, very thick, top color=white, bottom color=green!80 }, greenbar label font=\slshape, greenbar left shift=.1, greenbar right shift=-.1 } 
- \newganttchartelement{violetbar}{ violetbar/.style={ inner sep=0pt, draw=violet!50!black, very thick, top color=white, bottom color=purple!80 }, violetbar label font=\slshape, violetbar left shift=.1, violetbar right shift=-.1 } 
- \newganttchartelement{limebar}{ limebar/.style={ inner sep=0pt, draw=yellow!50!black, very thick, top color=white, bottom color=lime!80 }, limebar label font=\slshape, limebar left shift=.1, limebar right shift=-.1 }
- \let\paragraph\oldparagraph
- \let\subparagraph\oldsubparagraph
- \usepackage{titlesec, blindtext, color}
- \titleformat{\chapter}{\normalfont\bfseries}{\thechapter}{}{\Large}
- \titleformat{\section}{\normalfont\bfseries}{\section}{}{\large}
- \titleformat{\subsection}{\normalfont\bfseries}{\subsection}{}{\normalsize}
- \titleformat{\subsubsection}{\normalfont\bfseries}{\subsubsection}{}{\normalsize}
---


# Project Plan - IMU Sensor Application in the Ground-Based Vehicle Velocity Calculation

## Project Objective Recap
This dissertation aims to show how feasible it could be to use and design the purely IMU-based velocity calculation of the vehicle in use to give the driver of the vehicle its status of speed.
Here are the following objectives in this dissertation:

 - Review of the IMUs (Internal Measurement Units) available, and their capabilities, constraints and sensitivity.
 - Take note of and discuss the causes of the IMU errors and what could be done feasibly to prepare for them.
 - Review of the systems used to send and receive data from the IMU.
 - Creating the calculation algorithms and/or a filter design to compensate for the errors such as axis shifts, noise, misalignment and other parameters affecting the accuracy. Optionally providing a memory safe implementation of the algorithms in the embedded device.
 - Implementation of the design of the vehicle and gathering following test run data.
 - Discussion of the feasibility of the pure IMU-based design over the GPS-based, Hall-Effect sense and other velocity calculation methods.

## Winter Term Work Plan

### Preamble
As the required hardware is acquired:

 - BNO085 and LSM6DS3TR-C IMUs 
 - Raspberry Pi Pico W microcontrollers -
 - IPS and regular LCDs

With the optionals of:

 - 3D printing material
 - GPS module

Boilerplate software has been implemented and which could output raw data to the microcontroller, which proves us that the IMU is working and is able to be used in the project.

### Software Development
The software development is the next integral part of the project, where the IMU data is processed and the velocity is calculated. The software development has the following consecutive objectives:

 - Preliminary reading material of the IMU data processing (SPI and I2C protocols)
 - Implementing raw data logging into the microcontroller
 - Reading mathematical solutions and implementing algorithms for the real-time velocity calculation, and logging it.
 - Algorithm implementation of filtering the data noise for the embedded device.

With the optional, but useful objectives of:

 - Debugger implementation for the embedded device for troubleshooting, reading and debugging.
 - Further optimisation of the algorithms for the embedded device.
 - Open-Source publishing of the software under the Mozilla Public License 2.0 or GPL 3.0.

### Design Implementation and Data Collection
The design implementation and data collection is the next integral part of the project, where the IMU is implemented into the vehicle and the data is collected. The design implementation and data collection has the following consecutive objectives:

 - Designing the vehicle to fit the IMU and the microcontroller and having the initial test trial.
 - Gathering the data from the vehicle from consecutive results, and fixing the design if needed.
 - Analysing the data and comparing it to the other velocity calculation methods in the same run.
 - Final data collection and analysis which will be used in the dissertation with references to past trials and lessons learned.

### Writing - Documentation and Dissertation
The writing of the dissertation will be done over the both software and design development, as it is written in a flowing concurrent progression. The writing has the following consecutive objectives:

 - Justifying and documenting the design choices of the sensors, hardware and the software chosen.
 - Writing the documentation of the software development and design implementation in the personal markdown logs.
 - Discussing the data collected and analysing it.
 - Writing the dissertation with the following chapters:
   - Introduction
   - Literature Review
   - Methodology
   - Design and Implementation
   - Results and Analysis
   - Conclusion
   - References
   - Appendices
 - Proofreading and formatting to be more readable and correct dissertation.

## Optional Discussion of Winter Term Work Plan
As this is done in regard to the student society, ProtoTAU, for engineers to design the most efficient and reliable vehicle in an endurance competition, this dissertation has attached optional objectives.

### Hardware Development and Design
This entire design will be implemented in custom designed and also documented hardware for controlling, powering and monitoring the vehicle. The hardware development and design has the following consecutive objectives that will be done in parallel with the software development and design implementation and data collection:

 - Power management and safety design of the vehicle.
 - Electronics cooling and added redundancy.
 - Communication of the hardware electronics and the software.
 - Selecting and footprinting the components to the PCBs.
 - Total hardware assembly.
 - Safety features and chassis for the electronics.

### Documentation Foundation
The documentation foundation will be written and published in a society/personal website, for the main project topic after the completion of the whole design of this. All of this will be written in standard Markdown (.md) format. The documentation foundation has the following consecutive objectives:

 - Writing more automated documentation updating system for the website.
 - Better styling of the website.

Following parts have already been achieved in the current Autumn term:

 - Having the base system of publishing the documentation in web format from markdown.
 - Publishing the documentation of the hardware development and design in the ProtoTAU GitHub repository.
 - Webhosting the documentation.


\newpage\pdfpagewidth=594mm \pdfpageheight=420mm


# Gannt Chart
\begin{ganttchart}[
hgrid,
vgrid,
time slot format={isodate-yearmonth},
x unit=2mm,
y unit chart=6mm,
y unit title=8mm
]{2023-10-12}{2024-04-30}
\gantttitlecalendar{year, month=name, week}
    \ganttgroup[
        group/.append style={fill=orange}
    ]
    {Preparation and Acquirement}{2023-10-12}{2023-12-08}\\ [grid]
    \ganttorangebar[
        name=Pre-Reading of the Required Hardware
    ]
    {Pre-Reading of the Required Hardware}{2023-10-12}{2023-10-30}\\ [grid]
    \ganttorangebar[
        name=Hardware Acquirement
    ]
    {Hardware Acquirement}{2023-11-5}{2023-11-17}\\ [grid]
    \ganttorangebar[
        name=Initial Hardware Boilerplate Software
    ]
    {Initial Hardware Boilerplate Software}{2023-11-17}{2023-11-22}\\

    \ganttlinkedorangebar[name=Activity Summary]{Activity Summary}{2023-12-03}{2023-12-05}

    %Implementing links
    \ganttlink[link mid=0.75]{Pre-Reading of the Required Hardware}{Hardware Acquirement}
    \ganttlink{Hardware Acquirement}{Initial Hardware Boilerplate Software}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
\ganttnewline[thick, black]

    \ganttgroup[
        group/.append style={fill=green}
    ]{Software Development}{2023-12-15}{2023-12-22}
    \ganttgroup[
        group/.append style={fill=green}
    ]{}{2023-12-26}{2023-12-29}
    \ganttgroup[
        group/.append style={fill=green}
    ]{}{2024-01-02}{2024-02-26}\\ [grid]

    
    \ganttgreenbar[
        name=Pre-Reading of Software
    ]
    {Pre-Reading of Software}{2023-12-15}{2023-12-18}\\ [grid]

    \ganttgreenbar[
        name=Implementation of Raw Logging and Calculations
    ]
    {Implementation of Raw Logging and Calculations}{2023-12-19}{2023-12-21}\\ [grid]

    \ganttlinkedmilestone{Displacement and Velocity Logger}{2023-12-22}\\

    \ganttlinkedgreenbar[
        name=Filtering and Optimising Design
    ]
    {Filtering and Optimising Design}{2023-12-26}{2023-12-29}
    \ganttlinkedgreenbar{}{2024-01-02}{2024-01-15}

    \\ [grid]

    \ganttgreenbar[
        name=Debugger Hardware
    ]
    {Debugger Hardware}{2023-12-15}{2023-12-22}\\  [grid]

    \ganttgreenbar[
        name=Further Improvements 
    ]
    {Further Improvements}{2024-02-12}{2024-02-25}\\ [grid] 

    \ganttlinkedmilestone[
        name=sM0
    ]
    {Public Open Source Repository of the Design}{2024-02-26}\\ [grid]

    
    %Implementing links
    \ganttlink[link mid=0.75]{Pre-Reading of Software}{Implementation of Raw Logging and Calculations}


%%%%%%%%%%%%%%%%%%%%%%%%%%%%    
\ganttnewline[thick, black]

    \ganttgroup[
        group/.append style={fill=purple}
    ]{Design Implementation and Data Collection}{2024-01-21}{2024-02-25}

    \\
    \ganttvioletbar[
        name=Initial Trial
    ]
    {Initial Trial}{2024-01-22}{2024-01-30}\\ [grid]

    \ganttlinkedvioletbar[
        name=Initial Data Collection and Analysis 
    ]
    {Initial Data Collection and Analysis }{2024-02-01}{2024-02-05}\\

    \ganttlinkedvioletbar[
        name=Potential Back to Drawing Board
    ]
    {Potential Back to Drawing Board}{2024-02-06}{2024-02-14}\\

    \ganttlinkedvioletbar[
        name=Further Trials and Collection
    ]
    {Further Trials and Collection}{2024-02-14}{2024-02-22}\\

    \ganttlinkedvioletbar[
        name=Final Data Analysis
    ]
    {Final Data Analysis}{2024-02-23}{2024-02-25}\\[grid]
    
    \ganttlinkedmilestone{Working Design}{2024-02-25}\\


%%%%%%%%%%%%%%    
\ganttnewline[thick, black]

    \ganttgroup[
        group/.append style={fill=lime}
    ]{Writing - Documentation and Dissertation}{2023-12-15}{2024-04-01}

    \\
    \ganttlimebar[
        name=Hardware Selection Justification
    ]
    {Hardware Selection Justification}{2023-10-15}{2023-10-28}
    \ganttlimebar[
        name=Hardware Selection Justification
    ]
    {Hardware Selection Justification}{2023-12-13}{2023-12-16}
    \\ [grid]

    \ganttlimebar[
        name=Running Time Documentation of the Software Development
    ]
    {Running Time Documentation of the Software Development}{2023-12-15}{2024-02-05}\\

    \ganttlimebar[
        name=Hardware Implementation Discussion and Parameters
    ]
    {Hardware Implementation Discussion and Parameters}{2023-11-15}{2024-01-26}\\

    \ganttlimebar[
        name=Data Collection Discussion
    ]
    {Data Collection Discussion}{2024-02-01}{2024-02-30}\\

    \ganttlimebar[
        name=Data Analysis Discussion
    ]
    {Data Analysis Discussion}{2024-02-23}{2024-02-30}\\[grid]
    \ganttlimebar[
        name=Further Writing Formatting and Improvements
    ]
    {Further Writing, Formatting and Improvement}{2024-02-23}{2024-04-18}\\[grid]
    
    \ganttlinkedmilestone[name=wM0]{Final Supervised Writing}{2024-04-01}\\

    \ganttmilestone[name=wM1]{Date of Completion}{2024-04-18}\\

    \ganttlink[]{Further Writing Formatting and Improvements}{wM1}


%%%%%%%%%%%%%%
\ganttnewline[thick, black]

    \ganttgroup[
        group/.append style={fill=magenta}
    ]
    {Optional: Hardware Development and Design}{2023-10-12}{2023-12-08} [grid]
    \ganttgroup[
        group/.append style={fill=magenta}
    ]{}{2023-12-15}{2023-12-22}
    \ganttgroup[
        group/.append style={fill=magenta}
    ]{}{2023-12-26}{2023-12-29}
    \ganttgroup[
        group/.append style={fill=magenta}
    ]{}{2024-01-02}{2024-01-15}\\ [grid]

    \ganttpinkbar[
        name=Vehicle Power System Design
    ]
    {Vehicle Power System Design}{2023-10-12}{2023-10-30}\\ [grid]
    \ganttpinkbar[
        name=Electronics Cooling and Added Redundancy
    ]
    {Electronics Cooling and Added Redundancy}{2023-10-30}{2023-11-15}\\ [grid]
    \ganttpinkbar[
        name=Communications and Telemetry System Design
    ]
    {Communications and Telemetry System Design}{2023-12-15}{2023-12-22}\\ [grid]
    \ganttpinkbar[
        name=Component Selection
    ]
    {Component Selection}{2023-12-16}{2023-12-18}\\ [grid]
    \ganttpinkbar[
        name=PCB Footprinting
    ]
    {PCB Footprinting}{2023-12-18}{2023-12-20}\\ [grid]
    \ganttpinkbar[
        name=Hardware Assembly
    ]
    {Hardware Assembly}{2024-01-14}{2024-01-21}\\ [grid]
    \ganttlinkedmilestone[name=Milestone2]{Completed Vehicle Electronics}{2024-01-22}\\
    \ganttpinkbar[
        name=Component Chassis and Corporeal Safety
    ]
    {Component Chassis and Corporeal Safety}{2024-01-12}{2024-01-16} \\ [grid]
    \ganttpinkbar[
        name=Safety Design
    ]
    {Safety Design}{2023-10-12}{2023-12-22}
    \ganttlinkedpinkbar{}{2023-12-26}{2023-12-28} \\ [grid]


    %Implementing links
    \ganttlink[link mid=0.75]{Vehicle Power System Design}{PCB Footprinting}
    \ganttlink[link mid=0.75]{Electronics Cooling and Added Redundancy}{PCB Footprinting}
    \ganttlink[link mid=0.75]{Communications and Telemetry System Design}{Hardware Assembly}
    \ganttlink[link mid=0.75]{Component Selection}{PCB Footprinting}
    \ganttlink[link mid=0.75]{Component Selection}{Hardware Assembly}
    \ganttlink[link mid=0.75]{PCB Footprinting}{Hardware Assembly}
    \ganttlink[link mid=0.75]{Safety Design}{Hardware Assembly}
    \ganttlink[link mid=0.75]{Safety Design}{Component Chassis and Corporeal Safety}
    \ganttlink[link mid=0.75]{Component Chassis and Corporeal Safety}{Milestone2}




%%%%%%%%%%%%%%%%%
\ganttnewline[thick, black]

    \ganttgroup[
        group/.append style={fill=blue}
    ]
    {Optional: Documentation Foundation}{2023-10-12}{2023-12-18} [grid]
    \ganttgroup[
        group/.append style={fill=blue}
    ]{}{2024-01-05}{2024-01-20}\\ [grid]
    \ganttbluebar[
        name=Base Web Foundation
    ]
    {Base Web Foundation}{2023-10-12}{2023-10-14}\\
    \ganttlinkedmilestone[name=bM0]{Working Website}{2023-10-16}\\
    [grid]
    \ganttbluebar[
        name=Documentation Update Framework
    ]{Documentation Update Framework}{2023-10-18}{2023-10-30}\\
    \ganttlinkedmilestone[name=bM1]{Documentation Production Builder}{2023-11-05}\\
    
    [grid]
    \ganttbluebar[
        name=Further Styling
    ]
    {Further Styling}{2024-01-05}{2024-01-10}\\

    %Implementing links
    \ganttlink[link mid=0.75]{bM0}{Documentation Update Framework}
\end{ganttchart}