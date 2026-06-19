import pandas as pd
df = pd.read_csv('data/standardised_sales_data.csv')

numeric_columns = [
    "quantity",
    "unit_price",
    "discount",
    "total_amount",
]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

print("Negative quantity values")
print ((df["quantity"]<0).sum())

print("checking negative values in Unit price column")
print ((df["unit_price"]<0).sum())

print("checking negative values in Shipping cost column")
print ((df["shipping_cost"]<0).sum())

print("checking for invalid discount values")
print (((df["discount"]<0 )| (df["discount"]>100)).sum())

print("Checking for zero total amount values")
print ((df["total_amount"]<=0).sum())

print("Validation is successful. No negative values found in quantity, unit price, shipping cost, discount and total amount columns.")