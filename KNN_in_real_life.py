import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data = {
    "User": ["A", "B", "C", "D", "E"],
    "Action": [5, 4, 1, 2, 5],
    "Comedy": [4, 5, 2, 1, 4],
    "Drama": [1, 2, 5, 4, 1],
    "Label": ["Action", "Action", "Drama", "Drama", "Action"]
}

df = pd.DataFrame(data)

X = df[["Action", "Comedy", "Drama"]]
y = df["Label"]

model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

prediction = model.predict([[4, 4, 2]])

print("Dataset:")
print(df)

print("\nRecommended Genre:", prediction[0])
