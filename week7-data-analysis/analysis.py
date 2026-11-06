import pandas as pd

data = {
    "Name": ["Amit", "Riya", "Neha", "Rahul", "Pooja"],
    "Age": [20, 21, 19, 22, 20],
    "Marks": [85, 90, 75, 80, 95]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

print("\nData Information:")
print(df.info())

print("\nBasic Statistics:")
print(df.describe())

print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nHighest Marks:")
print(df["Marks"].max())

print("\nLowest Marks:")
print(df["Marks"].min())
