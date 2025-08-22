import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# Data
# ------------------------------
data = {
    "Category": ["Good", "Very Good", "Innovative"],
    "Count": [122, 44, 36],
    "Percent": [100.0, 36.07, 29.51]
}
df = pd.DataFrame(data)

# Ensure correct top-to-bottom order
df["Category"] = pd.Categorical(df["Category"], 
                                categories=["Good", "Very Good", "Innovative"], 
                                ordered=True)
df = df.sort_values("Category", ascending=False)  # top-to-bottom in horizontal bar

# ------------------------------
# Colors
# ------------------------------
colors = sns.color_palette("YlGnBu", n_colors=3)

# ------------------------------
# Plot
# ------------------------------
sns.set_theme(style="whitegrid")
plt.figure(figsize=(10, 4))

bars = plt.barh(df["Category"], df["Count"], color=colors, height=0.6)

# Annotate each bar with count and percent
for bar, count, pct in zip(bars, df["Count"], df["Percent"]):
    plt.text(count + max(df["Count"])*0.01,
             bar.get_y() + bar.get_height()/2,
             f"{count} ({pct:.2f}%)",
             va='center', fontsize=10)

# Labels and title
plt.xlabel("Number of Practices", fontsize=12)
plt.title("Distribution of Good, Very Good, and Innovative Practices (N=122)",
          fontsize=14)

# Clean axes
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.xlim(0, max(df["Count"])*1.15)

plt.tight_layout()
plt.show()


