import pandas as pd
from sklearn.cluster import KMeans

data = {
    "CustomerID": [1,2,3,4,5,6,7,8,9,10],
    "Age": [19,21,20,23,31,22,35,23,64,30],
    "Income": [15,16,17,18,40,42,60,62,80,85],
    "SpendingScore": [39,81,6,77,40,76,6,94,3,72]
}

df = pd.DataFrame(data)

X = df[["Income", "SpendingScore"]]

model = KMeans(n_clusters=3)
df["Cluster"] = model.fit_predict(X)

print(df)
