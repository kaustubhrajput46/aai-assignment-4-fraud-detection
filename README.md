# Fraud Detection with PyOD AutoEncoder

This project implements an unsupervised deep learning model for detecting credit card fraud using PyOD's AutoEncoder.

## Overview
Due to the Kaggle creditcard.csv dataset requiring authentication to download, this project generates a synthetic dataset that mimics the original structure (`Time`, `V1`-`V28`, `Amount`, `Class`), totaling around 10,000 samples with a 0.17% fraud rate (contamination).

The synthetic data is then scaled and passed to a PyOD AutoEncoder model to detect anomalies based on reconstruction errors.

## Files
- `fraud_detection.py`: Main Python script.
- `requirements.txt`: Python dependencies.
- `manifest.json`: Project manifest.
- `Kaustubh_Rajput_AAI_Assignment_4.docx`: APA 7 formatted report containing the source code and results.
- `README.md`: This file.

## Usage
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the code:
   ```bash
   python fraud_detection.py
   ```
This will output a classification report to the console and save the reconstruction error histogram as `output.png`.
