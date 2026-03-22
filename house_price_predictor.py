import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Area": [500, 800, 1000, 1200, 1500, 1800, 2000, 2200],
    "Bedrooms": [1, 2, 2, 3, 3, 4, 4, 5],
    "Price": [2000000, 3500000, 4500000, 5000000, 6500000, 7500000, 8500000, 9500000]
}

df = pd.DataFrame(data)

X = df[["Area", "Bedrooms"]]
y = df["Price"]

model = LinearRegression()
model.fit(X, y)

prediction = model.predict([[1600, 3]])

print("Dataset:")
print(df)

print("\nPredicted Price:", prediction[0])
