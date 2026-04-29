import sqlite3
conn = sqlite3.connect('retail.db')
cols = conn.execute("PRAGMA table_info(transactions)").fetchall()
for col in cols:
    print(col)
conn.close()