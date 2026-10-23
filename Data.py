import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(
    "AI_Usage_and_Impact_on_Students_and_Professionals_Cleaned.csv"
)

data["AI_Usage_Hours_Per_Day"] = pd.to_numeric(
    data["AI_Usage_Hours_Per_Day"], errors="coerce"
)

data["Productivity_Score"] = pd.to_numeric(
    data["Productivity_Score"], errors="coerce"
)

df = data[
    ["AI_Usage_Hours_Per_Day", "Productivity_Score"]
].dropna()

x = df["AI_Usage_Hours_Per_Day"]
y = df["Productivity_Score"]

correlation = x.corr(y)

slope, intercept = np.polyfit(x, y, 1)

x_sorted = np.sort(x)
y_trend = slope * x_sorted + intercept

plt.figure(figsize=(10, 6))

plt.scatter(
    x,
    y,
    color="#800020",
    alpha=0.75,
    s=65,
    edgecolors="white",
    linewidths=0.7,
    label="Data Points"
)

plt.plot(
    x_sorted,
    y_trend,
    color="#222222",
    linewidth=2.5,
    label=f"Trend Line (r = {correlation:.2f})"
)

plt.title(
    "AI Usage Hours vs Productivity Score",
    fontsize=17,
    fontweight="bold"
)

plt.xlabel("AI Usage Hours Per Day", fontsize=12)
plt.ylabel("Productivity Score", fontsize=12)

plt.grid(True, linestyle="--", alpha=0.25)
plt.legend(loc="upper left")

plt.tight_layout()
plt.show()

print("Records analyzed:", len(df))
print("Average AI usage:", round(x.mean(), 2), "hours/day")
print("Average productivity:", round(y.mean(), 2))
print("Correlation:", round(correlation, 3))