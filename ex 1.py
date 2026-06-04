import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(r"c:\Users\chokk\Downloads\student-mat.csv", sep=';')

# Bar Chart
plt.figure()
df.groupby('school')['G3'].mean().plot(kind='bar')
plt.title("Average Grade by School")
plt.savefig("bar.png")

# Scatter Plot
plt.figure()
plt.scatter(df['G1'], df['G3'])
plt.xlabel("G1")
plt.ylabel("G3")
plt.title("G1 vs G3")
plt.savefig("scatter.png")

# Histogram
plt.figure()
plt.hist(df['age'], bins=10)
plt.title("Age Distribution")
plt.savefig("histogram.png")

# Line Chart
avg_g1 = df['G1'].mean()
avg_g2 = df['G2'].mean()
avg_g3 = df['G3'].mean()

plt.figure()
plt.plot(['G1','G2','G3'], [avg_g1, avg_g2, avg_g3], marker='o')
plt.title("Average Grade Trend")
plt.savefig("line.png")

print("Charts saved successfully!")