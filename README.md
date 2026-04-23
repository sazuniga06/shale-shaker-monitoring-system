# Real-Time Monitoring and Fault Detection System for Shale Shaker Machines

This repository contains the technical documentation, industrial logic, and hardware design for a modular monitoring system designed for oil production optimization. The system focuses on vibration analysis and early fault detection in shale shaker machines.

## Authors and CRediT Roles
* **Hernán Paz Penagos:** Conceptualization, Methodology, Software, Hardware, Supervision, Project administration, Resources, Writing - review & editing.
* **Santiago Alejandro Zuñiga Melo:** Investigation, Formal analysis, Data curation, Validation, Visualization, Writing - original draft, Writing - review & editing.

## Project Overview
The system implements a real-time monitoring and SCADA-compatible architecture for shale shaker diagnostics:
* **Sensing:** BMI323 IMU for triaxial vibration and acceleration monitoring.
* **Industrial Logic:** PLC-based monitoring for shift detection and persistent alarms.
* **Architecture:** SCADA integration for remote supervision and maintenance alerts.
* **Connectivity:** ESP32 wireless module for data transmission to centralized servers.

## Repository Structure
* `/Hardware`: System schematics including power supply, sensor integration, and wireless module.
* `/software/plc`: Logic implementation for industrial controllers (Structured Text - IEC 61131-3).
* `/software/scripts`: Python algorithms for signal processing, filtering, and vibration shift detection.
* `/docs`: Technical documentation, SCADA tag mapping, and sample vibration datasets.

## Technical Highlights
* **Diagnostic Accuracy:** Error margin below 5% compared to certified laboratory equipment.
* **Economic Impact:** 20% estimated reduction in maintenance costs through proactive monitoring.
* **Statistical Validation:** Real-time Z-test and RMS calculation for mechanical fault identification.

## License
MIT License
