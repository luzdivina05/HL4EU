import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ------------------------------
# Data
# ------------------------------
data = {
    "Category": ["Africa", "Antarctica", "Asia", "Europe", "North America",
                 "Oceania", "South America", "Worldwide", "Asia, Africa, Europe"],
    "Count": [0, 0, 0, 107, 3, 1, 1, 9, 1]
}
df = pd.DataFrame(data)
df["Percent"] = df["Count"] / df["Count"].sum() * 100

# Sort ascending for horizontal bar chart
df = df.sort_values("Count", ascending=True)

# ------------------------------
# Colors (same style as first script)
# ------------------------------
n = len(df)
base_colors = sns.color_palette("YlGnBu", n_colors=n)
colors = np.array(base_colors)[np.argsort(df["Count"].values)]

# Highlight special categories
special = ["Worldwide", "Asia, Africa, Europe"]
colors[df["Category"].isin(special)] = sns.color_palette("YlGnBu_r", n_colors=n)[-2]

# ------------------------------
# Plot
# ------------------------------
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 6))

bars = plt.barh(df["Category"], df["Count"], color=colors, height=0.6)

# Annotate each bar: "raw (percent%)"
for bar, count, pct in zip(bars, df["Count"], df["Percent"]):
    width = bar.get_width()
    if count > 0:  # avoid clutter for 0 values
        plt.text(width + max(df["Count"])*0.01,
                 bar.get_y() + bar.get_height()/2,
                 f"{count} ({pct:.1f}%)",
                 va='center', fontsize=11)

# Labels and title
plt.xlabel("Number of Good Practices", fontsize=12)
plt.title("Geographical distribution of good practices by continent in the HL4EU Database (N=122)",
          fontsize=16)

# Clean axes (same style as your sector chart)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Proper x limit
plt.xlim(0, max(df["Count"])*1.15)

plt.tight_layout()
plt.show()
