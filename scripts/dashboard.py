import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

#connect to the database
conn = sqlite3.connect('data/sales.db')

#SQL QUERY
query = """
SELECT 
    payment_method,
    COUNT(*) AS transactions,
    SUM(total_amount) AS revenue
FROM sales
GROUP BY payment_method
ORDER BY transactions DESC;
"""

#READ QUERY RESULTS INTO A DATAFRAME
df = pd.read_sql_query(query, conn)

#CREATE CHART
plt.figure(figsize=(8, 5))
plt.bar(df['payment_method'], df['transactions'])

plt.title('Transactions by Payment Method')
plt.xlabel('Payment Method')        
plt.ylabel('transactions')

plt.xticks(rotation=45)
plt.tight_layout()

#SAVE CHART AS IMAGE
plt.savefig('dashboard/transactions_by_payment_method.png')

print("Dashboard saved successfully")
conn.close()