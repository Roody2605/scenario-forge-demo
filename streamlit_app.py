import streamlit as st
import pandas as pd

st.set_page_config(page_title="Scenario-Forge MVP", layout="wide")
st.title("📦 Scenario-Forge – Crisis Simulation MVP")

# CSV Upload Section
uploaded_file = st.file_uploader("📄 Upload your supply chain CSV", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")
    st.write("Here’s a preview of your supply chain data:")
    st.dataframe(df)

    # Placeholder for simulation logic
    st.info("Simulation module coming soon...")

else:
    st.info("👉 Upload a CSV to simulate a disruption.")
    st.markdown(
        "[📥 Download Sample CSV](https://convex-wheel-335365.framer.app/sample-csv)",
        unsafe_allow_html=True
    )
