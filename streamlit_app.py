import pandas as pd
import streamlit as st
import requests
from io import StringIO

st.set_page_config(page_title="Scenario-Forge MVP", layout="wide")
st.title("📦 Scenario-Forge – Crisis Simulation MVP")

# Google Drive direct link to your sample CSV
sample_url = "https://drive.google.com/uc?export=download&id=1-FP3yUBQfGeLTmOq3iERMi6wETM2-RBo"

# Load CSV from Google Drive if no upload
uploaded_file = st.file_uploader("📄 Upload your supply chain CSV", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
else:
    st.info("💡 No file uploaded — loading sample scenario...")
    response = requests.get(sample_url)
    df = pd.read_csv(StringIO(response.text))
    st.success("✅ Sample file loaded automatically!")

# Show the table
st.write("Here’s a preview of your supply chain data:")
st.dataframe(df)

# Fake AI output
st.markdown("### 🧠 Simulation Result")
st.markdown("""
🚨 **Disruption Simulation: Red Sea Drone Attack Detected**  
- **Port Delays:** +10 days on LaneA (Damietta → Hamburg)  
- **SKU Impacted:** CHR01  
- **Stockout Risk:** High within 5 days

🧠 **AI Recommendation:**  
- Reroute via Alexandria → Rotterdam (adds 2 days, saves $300)  
- Add 25 buffer units to CHR01 inventory next cycle  
- Notify customer in Hamburg of new ETA
""")

