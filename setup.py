import pandas as pd
import sqlite3
import os

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "retail.db")
EXCEL_PATH = os.path.join(BASE_DIR, "data", "online_retail_II.xlsx")

# Load Excel (it has 2 sheets - Year 2009-2010 and 2010-2011)
print("Reading Excel file... (this may take 30-60 seconds)")
df1 = pd.read_excel(EXCEL_PATH, sheet_name="Year 2009-2010")
df2 = pd.read_excel(EXCEL_PATH, sheet_name="Year 2010-2011")
df = pd.concat([df1, df2], ignore_index=True)
print(f"Total rows loaded: {len(df)}")

# Clean data
df.columns = ["invoice", "stock_code", "description", "quantity", 
              "invoice_date", "price", "customer_id", "country"]
df = df.dropna(subset=["customer_id"])         # remove rows with no customer
df = df[df["quantity"] > 0]                    # remove returns/cancellations
df = df[df["price"] > 0]                       # remove free/error items
df["customer_id"] = df["customer_id"].astype(int)
df["invoice_date"] = df["invoice_date"].astype(str)
print(f"Rows after cleaning: {len(df)}")

# Load into SQLite
conn = sqlite3.connect(DB_PATH)
df.to_sql("transactions", conn, if_exists="replace", index=False)
conn.close()

print("✅ Done! Data loaded into retail.db → table: transactions")