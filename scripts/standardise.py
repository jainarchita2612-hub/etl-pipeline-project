import pandas as pd
df = pd.read_csv('data/imputed_sales_data.csv')

print("Before standardisation:")
print(df.columns)

#adding underscore before capital letters in the column names using regex
df.columns = df.columns.str.replace(r'(?<!^)(?=[A-Z])', '_', regex=True)

#converting the column names to lowercase 
df.columns = df.columns.str.lower()

print("After standardisation:")
print(df.columns)

df.to_csv('data/standardised_sales_data.csv', index=False)
print("Standardised data saved to 'data/standardised_sales_data.csv'")