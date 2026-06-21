# Credit Risk Model Validation Dashboard

## Project Overview

This project demonstrates the validation and monitoring of a credit risk model using key risk analytics metrics. The dashboard provides model performance evaluation and population stability monitoring through an interactive Streamlit application.

## Features

- Model Performance Evaluation
  - AUC (Area Under Curve)
  - Gini Coefficient
  - KS Statistic

- Model Monitoring
  - Population Stability Index (PSI)
  - Drift Detection

- Training vs Validation Comparison

- Interactive Dashboard using Streamlit

## Tech Stack

- Python
- Pandas
- NumPy
- Scikit-Learn
- Streamlit
- Joblib

## Project Structure

```text
model-risk-validation/
│
├── app.py
├── requirements.txt
├── README.md
├── data/
├── models/
└── notebooks/
```

## Dashboard Metrics

| Metric | Value |
|----------|----------|
| Validation AUC | 0.7039 |
| Validation Gini | 0.4079 |
| KS Statistic | 0.3220 |
| PSI | 0.0000 |

## Key Findings

- ✅ Model approved for deployment
- ✅ No significant overfitting observed
- ✅ Validation AUC exceeds minimum acceptable threshold
- ✅ KS Statistic indicates good discriminatory power
- ✅ PSI indicates no population drift

## Deployment

The dashboard is deployed using Streamlit Cloud.

## Live Demo

🚀 [Open Credit Risk Validation Dashboard](https://model-risk-validation-dashboard-finjjkytqredheywlappmby.streamlit.app/)

## Key Outcomes

- Evaluated credit risk model performance.
- Compared training and validation metrics.
- Implemented PSI-based drift monitoring.
- Built and deployed an interactive dashboard.

## Author

Ansh Kumar Singh Tomar

M.Tech Artificial Intelligence & Data Science

IIT Patna
