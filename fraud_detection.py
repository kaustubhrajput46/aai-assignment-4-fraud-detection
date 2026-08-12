import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from pyod.models.auto_encoder import AutoEncoder
from pyod.utils.data import generate_data
import os

# Set random seed for reproducibility
np.random.seed(42)

print("Starting Assignment 4: PyOD AutoEncoder Fraud Detection")

# 1. Generate Synthetic Credit Card Fraud Data
# We simulate a dataset with 30 features (like V1-V28, Time, Amount)
# n_train: normal transactions, n_test: testing transactions
print("Generating synthetic dataset to mimic credit card transactions...")
X_train, X_test, y_train, y_test = generate_data(
    n_train=5000, 
    n_test=1000, 
    n_features=30, 
    contamination=0.05, 
    random_state=42
)

# In a real scenario, you'd load the Kaggle dataset here:
# df = pd.read_csv('creditcard.csv')
# X = df.drop(['Class'], axis=1)
# y = df['Class']

# 2. Data Preprocessing
print("Normalizing features using StandardScaler...")
scaler = StandardScaler()
X_train_norm = scaler.fit_transform(X_train)
X_test_norm = scaler.transform(X_test)

# 3. Build and Train the PyOD AutoEncoder Model
# AutoEncoder detects anomalies by training on normal-like data and flagging high reconstruction errors.
print("Initializing the AutoEncoder model...")
# Using default parameters with a simple architecture
clf = AutoEncoder(
    hidden_neurons=[30, 15, 15, 30], 
    epochs=15, 
    batch_size=32, 
    dropout_rate=0.2, 
    l2_regularizer=0.1, 
    contamination=0.05, 
    random_state=42, 
    verbose=0
)

print("Training the AutoEncoder...")
clf.fit(X_train_norm)

# 4. Predict Anomalies
print("Predicting anomalies on the test set...")
# Predict anomaly scores and outlier labels
y_train_pred = clf.labels_  # binary labels (0: inliers, 1: outliers)
y_train_scores = clf.decision_scores_  # raw outlier scores

y_test_pred = clf.predict(X_test_norm)
y_test_scores = clf.decision_function(X_test_norm)

# 5. Evaluate Performance
from pyod.utils.data import evaluate_print
print("\nModel Evaluation:")
evaluate_print('AutoEncoder', y_test, y_test_scores)

# Save the predictions to a CSV for manifest
results_df = pd.DataFrame({
    'True_Label': y_test,
    'Predicted_Label': y_test_pred,
    'Anomaly_Score': y_test_scores
})
results_df.to_csv('fraud_detection_results.csv', index=False)
print("Results saved to 'fraud_detection_results.csv'.")
print("Experiment completed successfully.")
