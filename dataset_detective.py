import pandas as pd

df = pd.read_csv("sales_data.csv")

print("Top Rows:")
print(df.head())

print("\nHighest Values:")
print(df.max(numeric_only=True))

print("\nMissing Values:")
print(df.isnull().sum())
