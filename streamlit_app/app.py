import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Claims Sentiment Dashboard",
    layout="wide"
)

st.title("Insurance Claims Sentiment & Renewal Risk Dashboard")

claims = pd.read_csv("data/sample_claims_data.csv")

total_claims = len(claims)
total_claim_amount = claims["claim_amount"].sum()
avg_claim_amount = claims["claim_amount"].mean()

col1, col2, col3 = st.columns(3)

col1.metric("Total Claims", total_claims)
col2.metric("Total Claim Amount", f"${total_claim_amount:,.0f}")
col3.metric("Average Claim Amount", f"${avg_claim_amount:,.0f}")

st.subheader("Claims Data")
st.dataframe(claims)

st.subheader("Claim Volume by Type")
st.bar_chart(claims["claim_type"].value_counts())

st.subheader("Claim Volume by State")
st.bar_chart(claims["state"].value_counts())

st.subheader("High Value Claims")
high_value_claims = claims[claims["claim_amount"] > 1000]
st.dataframe(high_value_claims)
