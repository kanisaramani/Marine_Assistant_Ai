import streamlit as st
import pandas as pd
from model.risk_classifier import classify_bleaching_risk
from llm.explainer import load_llm, explain_risk

st.set_page_config(page_title="Marine Heatwave & Coral Risk Monitor", layout="centered")

# Load CSV data
df = pd.read_csv("Data/sample_sst.csv")

# Load LLM once
@st.cache_resource
def get_model():
    return load_llm()

llm = get_model()

st.title("🌊 Marine Heatwave & Coral Bleaching AI Assistant")
st.markdown("This tool analyzes sea surface temperature (SST) anomalies to estimate coral bleaching risk and explain the reasoning.")

# Show data
st.subheader("📊 SST Anomalies")
st.dataframe(df)

# Process and show results
st.subheader("🧠 AI Risk Assessment")

for _, row in df.iterrows():
    region = row["region"]
    anomaly = row["sst_anomaly_celsius"]
    risk = classify_bleaching_risk(anomaly)
    explanation = explain_risk(region, risk, anomaly, llm)

    with st.expander(f"📍 {region} — {risk} Risk"):
        st.write(f"**SST Anomaly**: {anomaly}°C")
        st.write(f"**Bleaching Risk**: {risk}")
        st.write(f"**AI Explanation**: {explanation}")
