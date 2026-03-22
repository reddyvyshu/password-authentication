import pandas as pd

data = {
    "Name": ["Alice", "Bob", "alice", "Charlie", "Bob"],
    "Age": [20, None, 20, 22, None],
    "City": ["Bangalore", "Hyderabad", "bangalore", "Chennai", "Hyderabad"],
    "Marks": [85, 90, 85, None, 90]
}

df = pd.DataFrame(data)

df = df.drop_duplicates()

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

df["Name"] = df["Name"].str.title()
df["City"] = df["City"].str.title()

print("Cleaned Dataset:")
print(df)
