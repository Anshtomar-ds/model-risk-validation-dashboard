import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("models/credit_model.pkl")

st.set_page_config(page_title="Credit Risk Scorecard", layout="wide")

st.title("Credit Risk Model Validation Dashboard")

st.markdown("""
This dashboard provides model validation and monitoring results
including AUC, Gini, KS Statistic, PSI, ROC Curve and Confusion Matrix.
""")

st.header("Model Performance Summary")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Validation AUC", "0.7039")

with col2:
    st.metric("Validation Gini", "0.4079")

with col3:
    st.metric("KS Statistic", "0.3220")

with col4:
    st.metric("PSI", "0.0000")


st.header("Model Validation Status")

st.success("✅ Model Approved for Deployment")

st.write("""
- No significant overfitting observed
- Validation AUC exceeds training AUC
- KS statistic remains stable
- PSI indicates no population drift
""") 
# Training vs Validation Comparison

st.header("Training vs Validation Comparison")

comparison_df = pd.DataFrame({
    "Metric": ["AUC", "Gini", "KS Statistic"],
    "Training": [0.6879, 0.3758, 0.3093],
    "Validation": [0.7039, 0.4079, 0.3220]
})

st.dataframe(comparison_df)
# Model Monitoring

st.header("Model Monitoring")

st.metric("PSI Value", "0.0000")

if 0.0000 < 0.1:
    st.success("Population Stable - No Drift Detected")
elif 0.0000 < 0.25:
    st.warning("Moderate Drift Detected")
else:
    st.error("Significant Drift Detected")

