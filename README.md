# Real-Time Monitoring and Fault Detection System for Shale Shaker Machines

This repository contains the technical documentation, source code, and hardware design for a modular monitoring system designed for oil production optimization. The system focuses on vibration analysis and early fault detection in shale shaker machines.

## Authors and CRediT Roles
* **Hernán Paz Penagos:** Conceptualization, Methodology, Supervision, Project administration, Funding acquisition.
* **Santiago Alejandro Zuñiga Melo:** Software, Validation, Data Curation, Hardware Design, Writing - Original Draft.

## Project Overview
Shale shakers are vital for solid separation in drilling fluids. This project implements a real-time monitoring system using:
* **Microcontroller:** PIC18F14K22 for data management.
* **Sensors:** BMI323 IMU for triaxial vibration and acceleration monitoring.
* **Connectivity:** ESP32 wireless module for data transmission and analysis.

## Repository Structure
* `/hardware`: System schematics including power supply, MCU, and IMU sensor integration.
* `/software/firmware`: C/C++ code implemented for the PIC18F14K22 microcontroller.
* `/software/scripts`: Python logic for vibration shift detection (change >= 5%).
* `/docs`: Technical documentation and sample vibration datasets.

## Technical Highlights
* **Diagnostic Accuracy:** Error margin below 5% compared to certified laboratory equipment.
* **Economic Impact:** 20% estimated reduction in maintenance costs through proactive monitoring.
* **Statistical Validation:** Real-time Z-test and RMS calculation for mechanical fault identification.

## License
MIT License
