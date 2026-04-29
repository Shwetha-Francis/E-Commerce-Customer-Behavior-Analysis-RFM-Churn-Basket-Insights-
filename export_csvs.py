import sqlite3
import csv
import os

DB_PATH = "retail.db"
EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

queries = {
    "monthly_revenue": """
        SELECT 
            strftime('%Y-%m', invoice_date) AS month,
            ROUND(SUM(quantity * price), 2) AS revenue
        FROM transactions
        WHERE quantity > 0 AND price > 0 AND customer_id IS NOT NULL
        GROUP BY month
        ORDER BY month
    """,

    "top_products": """
        SELECT 
            description AS product,
            ROUND(SUM(quantity * price), 2) AS revenue,
            SUM(quantity) AS units_sold
        FROM transactions
        WHERE quantity > 0 AND price > 0 AND customer_id IS NOT NULL
        GROUP BY description
        ORDER BY revenue DESC
        LIMIT 20
    """,

    "rfm_segments": """
        WITH rfm AS (
            SELECT
                customer_id,
                CAST(julianday('2011-12-31') - julianday(MAX(invoice_date)) AS INTEGER) AS recency,
                COUNT(DISTINCT invoice) AS frequency,
                ROUND(SUM(quantity * price), 2) AS monetary
            FROM transactions
            WHERE quantity > 0 AND price > 0 AND customer_id IS NOT NULL
            GROUP BY customer_id
        ),
        scored AS (
            SELECT *,
                CASE WHEN recency <= 30 THEN 3 WHEN recency <= 90 THEN 2 ELSE 1 END AS r_score,
                CASE WHEN frequency >= 10 THEN 3 WHEN frequency >= 4 THEN 2 ELSE 1 END AS f_score,
                CASE WHEN monetary >= 1000 THEN 3 WHEN monetary >= 300 THEN 2 ELSE 1 END AS m_score
            FROM rfm
        )
        SELECT *,
            CASE 
                WHEN r_score=3 AND f_score=3 AND m_score=3 THEN 'Champions'
                WHEN r_score>=2 AND f_score>=2 THEN 'Loyal Customers'
                WHEN r_score=3 AND f_score=1 THEN 'New Customers'
                WHEN r_score=1 AND f_score>=2 THEN 'At Risk'
                ELSE 'Lost/Others'
            END AS segment
        FROM scored
    """,

    "segment_summary": """
        WITH rfm AS (
            SELECT
                customer_id,
                CAST(julianday('2011-12-31') - julianday(MAX(invoice_date)) AS INTEGER) AS recency,
                COUNT(DISTINCT invoice) AS frequency,
                ROUND(SUM(quantity * price), 2) AS monetary
            FROM transactions
            WHERE quantity > 0 AND price > 0 AND customer_id IS NOT NULL
            GROUP BY customer_id
        ),
        scored AS (
            SELECT *,
                CASE WHEN recency <= 30 THEN 3 WHEN recency <= 90 THEN 2 ELSE 1 END AS r_score,
                CASE WHEN frequency >= 10 THEN 3 WHEN frequency >= 4 THEN 2 ELSE 1 END AS f_score,
                CASE WHEN monetary >= 1000 THEN 3 WHEN monetary >= 300 THEN 2 ELSE 1 END AS m_score
            FROM rfm
        ),
        segmented AS (
            SELECT *,
                CASE 
                    WHEN r_score=3 AND f_score=3 AND m_score=3 THEN 'Champions'
                    WHEN r_score>=2 AND f_score>=2 THEN 'Loyal Customers'
                    WHEN r_score=3 AND f_score=1 THEN 'New Customers'
                    WHEN r_score=1 AND f_score>=2 THEN 'At Risk'
                    ELSE 'Lost/Others'
                END AS segment
            FROM scored
        )
        SELECT 
            segment,
            COUNT(*) AS customer_count,
            ROUND(AVG(monetary), 2) AS avg_spend,
            ROUND(AVG(frequency), 1) AS avg_orders
        FROM segmented
        GROUP BY segment
        ORDER BY customer_count DESC
    """,

    "country_sales": """
        SELECT 
            country,
            ROUND(SUM(quantity * price), 2) AS revenue,
            COUNT(DISTINCT customer_id) AS customers
        FROM transactions
        WHERE quantity > 0 AND price > 0 AND customer_id IS NOT NULL
        GROUP BY country
        ORDER BY revenue DESC
    """,

    "churn_risk": """
        SELECT
            customer_id,
            CAST(julianday('2011-12-31') - julianday(MAX(invoice_date)) AS INTEGER) AS days_since_last_order,
            COUNT(DISTINCT invoice) AS total_orders,
            ROUND(SUM(quantity * price), 2) AS total_spend
        FROM transactions
        WHERE quantity > 0 AND price > 0 AND customer_id IS NOT NULL
        GROUP BY customer_id
        HAVING days_since_last_order > 90
        ORDER BY days_since_last_order DESC
    """,

    "basket_analysis": """
        SELECT 
            a.description AS product_a,
            b.description AS product_b,
            COUNT(*) AS times_bought_together
        FROM transactions a
        JOIN transactions b 
            ON a.invoice = b.invoice AND a.description < b.description
        WHERE a.quantity > 0 AND b.quantity > 0
        GROUP BY product_a, product_b
        ORDER BY times_bought_together DESC
        LIMIT 30
    """
}

for name, query in queries.items():
    cursor.execute(query)
    rows = cursor.fetchall()
    headers = [desc[0] for desc in cursor.description]
    filepath = os.path.join(EXPORT_DIR, f"{name}.csv")
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    print(f" Exported {name}.csv ({len(rows)} rows)")

conn.close()
print("\nAll CSVs exported to /exports folder!")