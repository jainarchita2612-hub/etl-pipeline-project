import pandas as pd
df = pd.read_csv('data/sales_data.csv')

print ("Number of rows with missing values:")
print (df.isnull().sum())

df = df.fillna("Unknown")

print("Number of rows after imputing missing values:")
print(df.isnull().sum())

df.to_csv('data/imputed_sales_data.csv', index=False)
print("Missing values successfully imputed")
print("Imputed data saved to 'data/imputed_sales_data.csv'")

