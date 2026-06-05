import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv(r"c:\Users\chokk\Downloads\dataset.csv")

# Target Distribution
plt.figure(figsize=(6,4))
df["Target"].value_counts().plot(kind="bar")
plt.title("Student Outcome Distribution")
plt.savefig("target_distribution.png")

# Age Distribution
plt.figure(figsize=(6,4))
plt.hist(df["Age at enrollment"])
plt.title("Age Distribution")
plt.savefig("age_distribution.png")

# Correlation Heatmap
plt.figure(figsize=(12,8))
sns.heatmap(df.corr(numeric_only=True))
plt.savefig("correlation_heatmap.png")

print("Charts Saved")