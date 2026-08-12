import os
import pandas as pd
import streamlit as st

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(BASE, "data", "processed", "vision2030")

st.set_page_config(
    page_title="Saudi Vision 2030 Economic Analytics",
    page_icon="🇸🇦",
    layout="wide",
)

st.title("🇸🇦 Saudi Vision 2030 Economic Analytics")
st.caption("Tourism and economic transformation dashboard — Q1 2026")


def load_csv(filename):
    path = os.path.join(DATA, filename)
    df = pd.read_csv(path)
    # Remove Excel extraction footer rows and blank rows.
    df = df.dropna(how="all")
    return df


# Load reliable processed datasets. We intentionally do not use dashboard_kpis.csv
# because its extracted KPI values may contain source-sheet navigation text.
est = load_csv("tourism_establishments_by_region_q1_2026.csv")
saudi = load_csv("saudi_employment_by_region_q1_2026.csv")
non_saudi = load_csv("non_saudi_employment_by_region_q1_2026.csv")
total_emp = load_csv("tourism_total_employment_q1_2026.csv")
fac = load_csv("licensed_hospitality_facilities_q1_2026.csv")
rooms = load_csv("available_rooms_by_region_q1_2026.csv")


def numeric_total(df, column):
    values = pd.to_numeric(df[column], errors="coerce")
    # Prefer the explicit Total row when available.
    if "region" in df.columns:
        total_rows = df[df["region"].astype(str).str.strip().str.lower() == "total"]
        if not total_rows.empty:
            value = pd.to_numeric(total_rows.iloc[0][column], errors="coerce")
            if pd.notna(value):
                return float(value)
    return float(values.sum())


# KPI values are computed from the clean source tables instead of the malformed
# dashboard_kpis.csv extraction.
kpi_values = [
    ("Licensed hospitality facilities", numeric_total(fac, "total_licensed_facilities")),
    ("Tourism establishments", numeric_total(est, "establishments")),
    ("Tourism employment", numeric_total(total_emp, "total_employment")),
    ("Saudi tourism employment", numeric_total(saudi, "saudi_total")),
    ("Non-Saudi tourism employment", numeric_total(non_saudi, "non_saudi_total")),
    ("Available hospitality rooms", numeric_total(rooms, "total_available_rooms")),
]

st.header("Key Indicators")
cols = st.columns(4)
for i, (label, value) in enumerate(kpi_values[:4]):
    cols[i].metric(label, f"{value:,.0f}")

cols2 = st.columns(2)
for i, (label, value) in enumerate(kpi_values[4:6]):
    cols2[i].metric(label, f"{value:,.0f}")

st.divider()

# Clean regional tables for charts.
def clean_region_table(df, value_column):
    out = df.copy()
    out["region"] = out["region"].fillna("").astype(str).str.strip()
    out[value_column] = pd.to_numeric(out[value_column], errors="coerce").fillna(0)
    out = out[(out["region"] != "") & (out["region"].str.lower() != "total")]
    return out.sort_values(value_column, ascending=False)


est_chart = clean_region_table(est, "establishments")
saudi_chart = clean_region_table(saudi, "saudi_total")
non_saudi_chart = clean_region_table(non_saudi, "non_saudi_total")

st.header("Tourism Establishments by Region")
st.bar_chart(est_chart.set_index("region")["establishments"])

st.header("Saudi Tourism Employment by Region")
st.bar_chart(saudi_chart.set_index("region")["saudi_total"])

st.header("Non-Saudi Tourism Employment by Region")
st.bar_chart(non_saudi_chart.set_index("region")["non_saudi_total"])

st.header("Licensed Hospitality Facilities")
st.dataframe(fac, use_container_width=True)

st.header("Available Hospitality Rooms")
st.dataframe(rooms, use_container_width=True)

st.header("Saudi Employment Data")
st.dataframe(saudi, use_container_width=True)

st.divider()
st.caption("Source: Saudi Tourism Establishments Statistics — Q1 2026.")
