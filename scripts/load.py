import pandas as pd
import sqlite3

#read csv
df = pd.read_csv("data/standardised_sales_data.csv")

#connect to sqlite database
conn = sqlite3.connect("data/sales.db")

#Load data into sales table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Data loaded successfully into the sales table in sales.db")
conn.close()