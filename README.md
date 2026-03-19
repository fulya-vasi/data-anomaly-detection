# Data Anomaly Detection Pipeline (Python)

## Context

This project is inspired by my Bachelor thesis on AI-based anomaly detection in critical infrastructure systems (e.g., water supply and SCADA systems).
It demonstrates a simplified prototype of how anomalies in sensor data can be detected using machine learning.

## Overview

This project simulates sensor data (e.g. temperature and pressure) and detects anomalies using a machine learning model.

It was created to explore basic data processing, anomaly detection and visualization workflows in Python.

It reflects a simple end-to-end data pipeline including data generation, processing, analysis and export, similar to basic ETL workflows.

The implementation focuses on clean and modular Python code as well as reproducible data processing.

## Technologies

- Python
- pandas
- numpy
- scikit-learn
- matplotlib

## What it does

- Generates synthetic sensor data
- Injects artificial anomalies
- Applies anomaly detection using Isolation Forest
- Visualizes the results
- Exports processed data to CSV

## Output

The results are stored in:

data/output.csv

The column `anomaly` contains:

- 1 = normal value
- -1 = anomaly

## Example Output

### Console Output
![Console Output](images/output-console.png)

### Visualization
![Anomaly Plot](images/anomaly-plot.png)

## Run the project

pip install -r requirements.txt
python main.py
