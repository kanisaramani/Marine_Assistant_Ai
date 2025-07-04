import pandas as pd
from model.risk_classifier import classify_bleaching_risk
from llm.explainer import load_llm, explain_risk

# Load data and model
df = pd.read_csv("Data/sample_sst.csv")
llm = load_llm()

# Print results with explanations
for _, row in df.iterrows():
    region = row["region"]
    anomaly = row["sst_anomaly_celsius"]
    risk = classify_bleaching_risk(anomaly)
    
    explanation = explain_risk(region, risk, anomaly, llm)

    print(f"\n📍 {region}")
    print(f"SST Anomaly: {anomaly}°C")
    print(f"Bleaching Risk: {risk}")
    print(f"Explanation: {explanation}")

