# 🇸🇦 Saudi Vision 2030 Economic Analytics

An interactive **Saudi Vision 2030 tourism and economic transformation analytics dashboard** built with Python, Pandas, and Streamlit. The project analyzes Q1 2026 tourism-sector data across Saudi regions and presents key indicators, regional comparisons, and employment/hospitality statistics.

## 📊 Project Overview

The dashboard focuses on the tourism and hospitality side of Saudi Arabia's economic transformation under Vision 2030.

It provides:

- Key tourism and hospitality performance indicators
- Tourism establishments by region
- Saudi tourism employment by region
- Non-Saudi tourism employment by region
- Licensed hospitality facilities
- Available hospitality rooms by region
- Regional Saudi employment data
- Clean processed CSV datasets derived from the source workbook
- Visualizations generated from the processed data

## 🚀 Interactive Dashboard

The application is built with **Streamlit** and uses repository-relative data paths so it can run locally or on Streamlit Community Cloud.

Main application:

```text
dashboard/app.py
```

## 🗂️ Repository Structure

```text
saudi-vision2030-economic-analytics/
│
├── dashboard/
│   └── app.py
│
├── data/
│   ├── raw/
│   │   └── vision2030/
│   │       └── tourism_original.xlsx
│   │
│   └── processed/
│       ├── dashboard_kpis.csv
│       ├── economic_transformation_scorecard.csv
│       └── vision2030/
│           ├── available_rooms_by_region_q1_2026.csv
│           ├── historical_hospitality_facilities.csv
│           ├── historical_occupancy.csv
│           ├── historical_tourism_employment.csv
│           ├── historical_tourism_establishments.csv
│           ├── licensed_hospitality_facilities_q1_2026.csv
│           ├── non_saudi_employment_by_region_q1_2026.csv
│           ├── saudi_employment_by_region_q1_2026.csv
│           ├── serviced_apartment_occupancy_q1_2026.csv
│           ├── total_employment_by_region_q1_2026.csv
│           ├── tourism_establishments_by_region_q1_2026.csv
│           ├── tourism_establishments_q1_2026.csv
│           ├── tourism_non_saudi_employment_q1_2026.csv
│           ├── tourism_saudi_employment_q1_2026.csv
│           └── tourism_total_employment_q1_2026.csv
│
├── visualizations/
│   └── vision2030/
│       ├── licensed_hospitality_facilities_q1_2026.png
│       ├── tourism_establishments_q1_2026.png
│       └── tourism_saudi_employment_q1_2026.png
│
└── requirements.txt
```

## 🛠️ Technology Stack

- **Python**
- **Pandas** — data loading, cleaning, transformation, and aggregation
- **Streamlit** — interactive dashboard
- **Matplotlib** — analytical visualizations
- **CSV / Excel** — source and processed datasets
- **Git & GitHub** — version control and project publication

## 📈 Dashboard Sections

### Key Indicators

The dashboard calculates and displays:

- Licensed hospitality facilities
- Tourism establishments
- Total tourism employment
- Saudi tourism employment
- Non-Saudi tourism employment
- Available hospitality rooms

### Regional Analysis

Regional comparisons are provided for:

- Tourism establishments
- Saudi tourism employment
- Non-Saudi tourism employment

The dashboard removes the aggregate `Total` row from regional charts so that individual regions can be compared directly.

### Hospitality Data

Interactive tables provide the processed licensed-facility and available-room datasets.

### Employment Data

The dashboard includes the processed Saudi employment-by-region dataset and separates Saudi and non-Saudi tourism employment for analysis.

## 🧹 Data Processing Approach

The project keeps the original tourism workbook under `data/raw/` and stores cleaned analytical datasets under `data/processed/`.

The dashboard converts numeric fields with error handling and removes empty/extraction rows before analysis. KPI totals preferentially use an explicit `Total` row when available and otherwise calculate totals from the cleaned regional data.

## 📚 Data Source

The primary tourism dataset is the **Saudi Tourism Establishments Statistics — Q1 2026** workbook. The repository preserves the original workbook and the processed CSV outputs used by the dashboard.

## ▶️ Run Locally

Clone the repository and install the dependencies:

```bash
git clone https://github.com/Hadi-Saeed-2006/saudi-vision2030-economic-analytics.git
cd saudi-vision2030-economic-analytics
pip install -r requirements.txt
```

Start the Streamlit dashboard:

```bash
streamlit run dashboard/app.py
```

## ☁️ Deployment

The dashboard is structured for deployment through **Streamlit Community Cloud** using:

- Repository: `Hadi-Saeed-2006/saudi-vision2030-economic-analytics`
- Branch: `main`
- Main file: `dashboard/app.py`

## 🎯 Project Goals

This project demonstrates practical skills in:

- Data cleaning and preparation
- Exploratory data analysis
- Regional economic comparison
- Tourism and employment analytics
- KPI design
- Data visualization
- Interactive dashboard development
- Reproducible data-project structure
- GitHub-based portfolio development

## 🔭 Future Development

Planned extensions can include additional historical tourism trends, broader Saudi economic indicators, forecasting, deeper Vision 2030 transformation metrics, and comparative analysis with other regions and economies.

---

**Project:** Saudi Vision 2030 Economic Analytics  
**Focus:** Tourism, hospitality, employment, and economic transformation  
**Reference period:** Q1 2026
