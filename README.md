🌊 Marine Heatwave & Coral Bleaching AI Assistant

This is a lightweight, explainable AI tool that analyzes Sea Surface Temperature (SST) anomalies to estimate the risk of coral bleaching — and provides natural language explanations using a domain-aware language model.

> Built in under a day using Python, Streamlit, and Hugging Face Transformers 🚀



🔍 What It Does

- ✅ Loads ocean temperature anomaly data (CSV)
- ✅ Classifies coral bleaching risk as Low / Moderate / High
- ✅ Uses an LLM to explain the risk in plain language
- ✅ Presents all results in an interactive Streamlit dashboard





📁 Project Structure

marine-ai-assistant/
├── app.py                     # Streamlit app
├── test_classifier.py         # CLI test runner
├── Data/
│   └── sample_sst.csv         # Sample ocean SST anomaly data
├── model/
│   └── risk_classifier.py     # Classifies bleaching risk
├── llm/
│   └── explainer.py           # LLM explanation logic
├── requirements.txt
└── README.md



🧠 Tech Stack

- Python
- Streamlit
- Hugging Face Transformers (flan-t5-base)
- Pandas



📚 Data Source

Sample data is adapted for demo purposes. Real-time SST anomaly data can be retrieved from:
- NOAA Coral Reef Watch
- GHRSST
- CMEMS (Copernicus Marine)


✨ Future Ideas

- 🌐 Add real-time API data feed
- 🗺️ Visualize bleaching zones on a map
- 📩 Email alerts to marine researchers
- 🌍 Translate summaries to regional languages

🙌 Acknowledgments

Huge thanks to:
- NOAA Coral Reef Watch (https://coralreefwatch.noaa.gov)
- Hugging Face (https://huggingface.co/)
- Streamlit (https://streamlit.io/)
