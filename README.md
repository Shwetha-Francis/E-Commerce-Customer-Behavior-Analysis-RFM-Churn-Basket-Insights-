# 🛍️ E-Commerce Customer Behavior Analysis: RFM, Churn & Basket Insights

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/SQLite-SQL-lightgrey?style=for-the-badge&logo=sqlite" />
  <img src="https://img.shields.io/badge/Power%20BI-Dashboard-yellow?style=for-the-badge&logo=powerbi" />
</p>

<p align="center">
  <b>End-to-end SQL analytics on 800,000+ retail transactions — uncovering revenue trends, customer segments, and churn risk</b>
</p>

---

## 🧩 Business Problem

A UK-based e-commerce retailer needed to understand why certain customer segments were going quiet and which products and regions were driving the most value. Key questions:

- *Which customers are at risk of churning — and how many?*
- *What does the revenue trend look like across 2009–2011?*
- *Which products and countries generate the most revenue?*
- *How are customers segmented by buying behavior?*

**Customer Pulse** was built to answer these questions using SQL analytics and a Power BI dashboard — giving a full picture of customer health, product performance, and geographic revenue distribution.

---

## 💡 Key Business Recommendations

| Finding | Recommendation | Estimated Impact |
|--------|----------------|-----------------|
| 3,318 customers have not purchased in 90+ days | Launch a re-engagement email campaign targeting at-risk segment with personalized offers | Recover 10–15% of lapsed customers |
| UK accounts for ~£14.7M revenue — other markets underrepresented | Expand marketing and fulfillment to top non-UK countries (Germany, France, EIRE) | Diversify revenue base, reduce single-market risk |
| Q4 consistently outperforms other quarters | Pre-load inventory and run promotions starting October to maximize holiday season revenue | Capture full Q4 uplift across gift and home décor SKUs |
| Champions and Loyal Customers form the core revenue base | Introduce loyalty rewards and early-access offers for top RFM segments | Increase retention and average order value |
| Top products dominated by gift and home décor items | Bundle top SKUs with complementary products (basket analysis pairs) for cross-sell | Increase basket size per transaction |

---

## 📌 Project Overview

| Detail | Info |
|---|---|
| **Dataset** | Online Retail II (UCI Machine Learning Repository) |
| **Rows** | ~805,000 transactions |
| **Period** | December 2009 – December 2011 |
| **Tools** | Python, SQLite, SQL, Power BI |
| **Goal** | Understand revenue trends, customer segments, and churn risk |

---

## 📊 Key Findings

- **Revenue grew significantly** from 2009 to 2011, with Q4 consistently outperforming other quarters by 35%+
- **United Kingdom** dominates revenue at ~£14.7M — the next highest markets are Germany, France, and EIRE
- **3,318 customers** flagged as churn risk — no purchase in 90+ days
- **Top products** are concentrated in gift and home décor categories — top 10 SKUs contribute a disproportionate share of total revenue
- **RFM segmentation** reveals a healthy base of Champions and Loyal Customers, with a meaningful At Risk cohort requiring re-engagement
- **Basket analysis** identifies product pairs frequently bought together — actionable for cross-sell and bundle strategy

---

## 🔍 SQL Analyses

### 1. Monthly Revenue
Tracks total revenue month-over-month to identify growth trends and seasonal patterns.

### 2. Top Products
Ranks products by total revenue and units sold to identify best-performing SKUs.

### 3. RFM Segmentation
Segments customers based on **Recency**, **Frequency**, and **Monetary** scores into:
- 🏆 Champions
- 💛 Loyal Customers
- 🆕 New Customers
- ⚠️ At Risk
- ❌ Lost / Others

### 4. Segment Summary
Aggregates RFM segments to show customer count, average spend, and average order frequency per segment.

### 5. Country Sales
Ranks countries by total revenue and unique customer count. The UK dominates with ~£14.7M in revenue.

### 6. Churn Risk
Identifies customers who have not placed an order in over 90 days — **3,318 customers** flagged as churn risk.

### 7. Basket Analysis
Finds product pairs frequently bought together using a self-join on invoice ID — useful for cross-sell and bundling recommendations.

---

## 📈 Power BI Dashboard

The dashboard includes 5 visuals with interactive slicers for **Country** and **Customer Segment**:

| Visual | Type | Insight |
|---|---|---|
| Revenue Trend | Line chart | Month-over-month revenue growth |
| Top Products by Revenue | Bar chart | Best-selling products |
| Customer Segments | Donut chart | RFM segment distribution |
| Top 10 Countries by Revenue | Bar chart | Geographic revenue breakdown |
| Churn Risk Customers | Card | Count of at-risk customers |

---

## 📐 Project Workflow

```
Raw Excel → Python Ingestion → SQLite DB → SQL Analysis → CSV Exports → Power BI Dashboard → Business Insights
```

1. **Data Ingestion** — `setup.py` loads the raw `.xlsx` into a SQLite database
2. **SQL Analysis** — 7 analytical queries covering revenue, products, RFM, churn, and basket patterns
3. **CSV Export** — `export_csvs.py` exports query results for Power BI consumption
4. **Power BI Dashboard** — interactive dashboard with slicers for dynamic filtering

---

## 📁 Folder Structure

```
customer-pulse-sql/
│
├── data/
│   └── online_retail_II.xlsx       # Raw dataset
│
├── sql/
│   ├── 01_monthly_revenue.sql
│   ├── 02_top_products.sql
│   ├── 03_rfm_segmentation.sql
│   ├── 04_segment_summary.sql
│   ├── 05_country_sales.sql
│   ├── 06_churn_risk.sql
│   └── 07_basket_analysis.sql
│
├── exports/
│   ├── monthly_revenue.csv
│   ├── top_products.csv
│   ├── rfm_segments.csv
│   ├── segment_summary.csv
│   ├── country_sales.csv
│   ├── churn_risk.csv
│   └── basket_analysis.csv
│
├── findings/                        # Insights and notes
├── retail.db                        # SQLite database
├── setup.py                         # Data ingestion script
├── export_csvs.py                   # CSV export script
└── Customer_Pulse_Dashboard.pbix    # Power BI dashboard
```

---

## 🛠️ Setup & How to Run

### 1. Clone the repo
```bash
git clone https://github.com/Shwetha-Francis/E-Commerce-Customer-Behavior-Analysis-RFM-Churn-Basket-Insights-.git
cd E-Commerce-Customer-Behavior-Analysis-RFM-Churn-Basket-Insights-
```

### 2. Install dependencies
```bash
pip install pandas openpyxl
```

### 3. Load data into SQLite
```bash
python setup.py
```

### 4. Export CSVs for Power BI
```bash
python export_csvs.py
```

### 5. Open the dashboard
Open `Customer_Pulse_Dashboard.pbix` in Power BI Desktop.

---

## 🗃️ Dataset Source

- **Name:** Online Retail II
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## 👩‍💻 Author

**Shwetha Francis** | BTech in AI & Data Science  
Data Analyst | SQL · Python · Power BI  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://linkedin.com/in/your-profile)
[![GitHub](https://img.shields.io/badge/GitHub-Portfolio-black)](https://github.com/Shwetha-Francis)

---

*Built as part of a data analytics portfolio — [github.com/Shwetha-Francis](https://github.com/Shwetha-Francis)*
