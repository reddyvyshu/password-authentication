import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Category": ["Electronics", "Fashion", "Accessories", "Electronics", "Fashion"],
    "Sales": [55000, 3000, 2500, 60000, 800],
    "City": ["Bangalore", "Mumbai", "Pune", "Chennai", "Hyderabad"]
}

df = pd.DataFrame(data)

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure()
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.show()

plt.figure()
category_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Sales Distribution by Category")
plt.ylabel("")
plt.show()

plt.figure()
df["Sales"].plot(kind="hist", bins=5)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()
