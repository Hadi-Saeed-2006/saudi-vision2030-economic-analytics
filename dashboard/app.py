
import streamlit as st
import pandas as pd
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

st.set_page_config(
    page_title="Saudi Vision 2030 Economic Analytics",
    page_icon="🇸🇦",
    layout="wide"
)

st.title("🇸🇦 Saudi Vision 2030 Economic Analytics")
st.caption("Tourism and economic transformation dashboard — Q1 2026")

kpis = pd.read_csv(os.path.join(BASE, "data/processed/dashboard_kpis.csv"))

st.header("Key Indicators")

cols = st.columns(4)

for i, (_, row) in enumerate(kpis.head(4).iterrows()):
    cols[i].metric(
        row["kpi"],
        f"{row['value']:,.0f}"
    )

st.divider()

est = pd.read_csv(
    os.path.join(
        BASE,
        "data/processed/vision2030/tourism_establishments_by_region_q1_2026.csv"
    )
)

saudi = pd.read_csv(
    os.path.join(
        BASE,
        "data/processed/vision2030/saudi_employment_by_region_q1_2026.csv"
    )
)

non_saudi = pd.read_csv(
    os.path.join(
        BASE,
        "data/processed/vision2030/non_saudi_employment_by_region_q1_2026.csv"
    )
)

fac = pd.read_csv(
    os.path.join(
        BASE,
        "data/processed/vision2030/licensed_hospitality_facilities_q1_2026.csv"
    )
)

st.header("Tourism Establishments by Region")
st.bar_chart(est.set_index("region")["establishments"])

st.header("Saudi Tourism Employment by Region")
st.bar_chart(saudi.set_index("region")["saudi_total"])

st.header("Non-Saudi Tourism Employment by Region")
st.bar_chart(non_saudi.set_index("region")["non_saudi_total"])

st.header("Licensed Hospitality Facilities")
st.dataframe(fac, use_container_width=True)

st.header("Saudi Employment Data")
st.dataframe(saudi, use_container_width=True)

st.divider()
st.caption(
    "Source: Saudi Tourism Establishments Statistics — Q1 2026."
)
