import pandas as pd
df = pd.DataFrame({
    "name": ["Asha", "Ravi", "Priya", "Karan", "Meena"],
    "age": [20, 21, 19, 22, 20],
    "city": ["Chennai", "Delhi", "Mumbai", "Hyderabad", "Pune"],
    "marks": [85, 45, 78, 92, 50]
})
print("Head:")
print(df.head())
print("\nShape:")
print(df.shape)
print("\nData Types:")
print(df.dtypes)
df["result"] = df["marks"].apply(
    lambda x: "Pass" if x >= 50 else "Fail"
)
print("\nUpdated DataFrame:")
print(df)