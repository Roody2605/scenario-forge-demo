# streamlit_app.py  — safe offline demo, no file upload needed
import streamlit as st
import pandas as pd
from io import StringIO

# ---- Page config ----
st.set_page_config(page_title="Scenario-Forge Demo", layout="wide")

st.title("Scenario-Forge – Stress-test your supply chain in 60 s")

# ---- Hard-coded demo network ----
CSV = StringIO("""
Supplier,Origin,Destination,SKU,Monthly_Qty,Transit_Days,Lane_Cost_EGP
ACME Metals,Port Said,Cairo DC,SheetSteel,120,3,15000
Delta Plastics,Alexandria,Giza DC,PolyBag,500,2,8000
Nile Textiles,Suez,Cairo DC,CottonRoll,350,1,4000
""")

df = pd.read_csv(CSV, skipinitialspace=True)
st.success("✅ Demo network loaded (3 rows)")
st.dataframe(df, use_container_width=True)

# ---- Fake scenario run ----
if st.button("Run Scenario"):
    with st.spinner("Simulating …"):
        kpis = {
            "Δ Cost": "+7.8 %",
            "Δ Lead-time": "+4.5 days",
            "Stock-out risk": "23 %",
            "Δ CO₂": "+3.1 t"
        }
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Δ Cost", kpis["Δ Cost"])
    col2.metric("Δ Lead-time", kpis["Δ Lead-time"])
    col3.metric("Stock-out", kpis["Stock-out risk"])
    col4.metric("Δ CO₂", kpis["Δ CO₂"])
    st.success("🎉 Scenario complete – PDF export will be enabled in next build")
