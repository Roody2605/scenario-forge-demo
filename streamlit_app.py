import streamlit as st
import pandas as pd

st.set_page_config(page_title="Scenario-Forge MVP", layout="wide")
st.title("📦 Scenario-Forge – Crisis Simulation MVP")

uploaded_file = st.file_uploader("📄 Upload your supply chain CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.write("Here’s a preview of your supply chain data:")
    st.dataframe(df)

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
else:
    st.info("👉 Upload a CSV to simulate a disruption.")
    st.markdown(
        "[📥 Download Sample CSV](https://drive.google.com/uc?export=download&id=1-FP3yUBQfGeLTmOq3iERMi6wETM2-RBo)",
        unsafe_allow_html=True
    )

