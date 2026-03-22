import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "StudyHours": [1,2,3,4,5,6,7,8,2.5,3.5,4.5,5.5,6.5,7.5,8.5,1.5,2.2,3.8,4.2,5.8,6.2,7.8,8.2,9,9.5,10],
    "Marks": [30,35,45,50,60,65,75,80,40,48,55,63,70,78,85,32,38,52,58,68,72,82,86,88,92,95]
}

df = pd.DataFrame(data)

X = df[["StudyHours"]]
y = df["Marks"]

model = LinearRegression()
model.fit(X, y)

predicted = model.predict([[9]])

print("Dataset:")
print(df)

print("\nPredicted Marks for 9 Study Hours:", predicted[0])
