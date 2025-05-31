# ------- streamlit_app.py ------------
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Scenario-Forge", layout="wide")
st.title("Scenario-Forge – Stress-test your supply chain in 60 s")

uploaded = st.file_uploader("Upload your lane/SKU CSV", type="csv")
if uploaded:
    df = pd.read_csv(uploaded)
    st.success(f"Loaded {df.shape[0]} rows")
    st.dataframe(df.head())

    if st.button("Run Scenario"):
        with st.spinner("Simulating…"):
            kpis = {
                "Total landed cost change": "+7.8 %",
                "Avg lead-time change": "+4.5 days",
                "Stock-out risk": "23 %",
                "CO₂ footprint change": "+3.1 t"
            }
        st.subheader("Key KPIs")
        st.write(kpis)

        st.info("📄 PDF playbook generation disabled in this demo build.")
else:
    st.info("⬆️ Upload the demo_network.csv to see a demo run")
