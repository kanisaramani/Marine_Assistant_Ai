from transformers import pipeline

# Load a small instruction-tuned model
def load_llm():
    return pipeline("text2text-generation", model="google/flan-t5-base")

# Generate an explanation
def explain_risk(region, risk_level, sst_anomaly, llm):
    prompt = (
        f"The sea surface temperature anomaly in {region} is {sst_anomaly}°C, "
        f"which is considered a {risk_level} risk for coral bleaching. "
        f"Explain why this could be harmful to marine ecosystems."
    )
    response = llm(prompt, max_new_tokens=80, do_sample=False)
    return response[0]['generated_text']
