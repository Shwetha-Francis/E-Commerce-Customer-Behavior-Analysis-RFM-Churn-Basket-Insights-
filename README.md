# 🛍️ E-Commerce Customer Behavior Analysis: RFM, Churn & Basket Insights  — Retail Analytics Project

A end-to-end SQL analytics project analyzing 800,000+ retail transactions to uncover revenue trends, customer behavior, and churn risk.

---

## 📌 Project Overview

**Customer Pulse** is a portfolio data analytics project built on the [Online Retail II dataset](https://archive.ics.uci.edu/dataset/502/online+retail+ii) from the UCI Machine Learning Repository. The project covers the full analytics workflow — from raw data ingestion to SQL analysis to a Power BI dashboard.

| Detail | Info |
|---|---|
| **Dataset** | Online Retail II (UCI) |
| **Rows** | ~805,000 transactions |
| **Period** | December 2009 – December 2011 |
| **Tools** | Python, SQLite, SQL, Power BI |
| **Goal** | Understand revenue trends, customer segments, and churn risk |

---

## 📁 Folder Structure

```
customer-pulse-sql/
│
├── data/
│   └── online_retail_II.xlsx       # Raw dataset
│
├── sql/
│   ├── monthly_revenue.sql
│   ├── top_products.sql
│   ├── rfm_segments.sql
│   ├── segment_summary.sql
│   ├── country_sales.sql
│   ├── churn_risk.sql
│   └── basket_analysis.sql
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
├── findings/
│   └── (insights and notes)
│
├── retail.db                        # SQLite database
├── setup.py                         # Data ingestion script
├── export_csvs.py                   # CSV export script
└── Customer_Pulse_Dashboard.pbix    # Power BI dashboard
```

---

## 🛠️ Setup & How to Run

### 1. Clone the repo
```bash
git clone https://github.com/Shwetha-Francis/customer-pulse-sql.git
cd customer-pulse-sql
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
- ❌ Lost/Others

### 4. Segment Summary
Aggregates RFM segments to show customer count, average spend, and average order frequency per segment.

### 5. Country Sales
Ranks countries by total revenue and unique customer count. The UK dominates with ~£14.7M in revenue.

### 6. Churn Risk
Identifies customers who have not placed an order in over 90 days — **3,318 customers** flagged as churn risk.

### 7. Basket Analysis
Finds product pairs frequently bought together using a self-join on invoice ID — useful for cross-sell recommendations.

---

## 📊 Power BI Dashboard

The dashboard includes 5 visuals:

| Visual | Type | Insight |
|---|---|---|
| Revenue Trend | Line chart | Month-over-month revenue growth |
| Top Products by Revenue | Bar chart | Best-selling products |
| Customer Segments | Donut chart | RFM segment distribution |
| Top 10 Countries by Revenue | Bar chart | Geographic revenue breakdown |
| Churn Risk Customers | Card | Count of at-risk customers |

Interactive slicers for **Country** and **Customer Segment** allow dynamic filtering across visuals.

---

## 💡 Key Findings

- **Revenue grew significantly** from 2009 to 2011, with peak months in Q4 (holiday season)
- **United Kingdom** accounts for the vast majority of revenue (~£14.7M)
- **3,318 customers** are at churn risk (no purchase in 90+ days)
- Top products are dominated by **gift and home décor items**
- RFM segmentation reveals a healthy mix of Champions and Loyal Customers

---

## 🗃️ Dataset Source

- **Name:** Online Retail II
- **Source:** [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/502/online+retail+ii)
- **License:** Creative Commons Attribution 4.0 International (CC BY 4.0)

---

## 👩‍💻 Author

**Shwetha**  
Aspiring Data Analyst | SQL · Python · Power BI  
[LinkedIn](#) · [GitHub](#)

---

*Built as part of a data analytics portfolio project.*
