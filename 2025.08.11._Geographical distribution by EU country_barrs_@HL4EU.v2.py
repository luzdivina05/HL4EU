import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ------------------------------
# Data
# ------------------------------
data = {
    "Country": [
        "Albania","Austria","Belgium","Bosnia","Bulgaria","Coratia","Croatia","Cyprus","Czechia",
        "Denmark","Egypt","England","Estonia","Europewide","Finland","France","Genova","Germany",
        "Greece","Herzegovina","Hungary","Israel","Italy","Japan","Latvia","Lithuania","Montenegro",
        "Netherland","Norway","Poland","Portugal","Republic of Ireland","Romania","Scotland","Serbia",
        "Slovakia","Slovenia","Spain","Sweden","Switzerland","The Netherlands","Turkey","Türkiye",
        "United Kingdom"
    ],
    "Count": [
        1,4,10,1,2,1,3,4,1,4,1,2,3,1,5,6,1,10,11,1,4,1,14,1,2,1,1,1,4,3,7,5,2,1,1,2,5,10,3,1,7,5,2,9
    ]
}

df = pd.DataFrame(data)
df["Percent"] = df["Count"] / df["Count"].sum() * 100

# Sort ascending for horizontal bar chart
df = df.sort_values("Count", ascending=True)

# ------------------------------
# Colors (YlGnBu like other plots)
# ------------------------------
n = len(df)
base_colors = sns.color_palette("YlGnBu", n_colors=n)
colors = np.array(base_colors)[np.argsort(df["Count"].values)]

# Highlight special category
special = ["Europewide"]
colors[df["Country"].isin(special)] = sns.color_palette("YlGnBu_r", n_colors=n)[-2]

# ------------------------------
# Plot
# ------------------------------
sns.set_theme(style="whitegrid")
plt.figure(figsize=(12, 10))

bars = plt.barh(df["Country"], df["Count"], color=colors, height=0.6)

# Annotate each bar: "count (percent%)"
for bar, count, pct in zip(bars, df["Count"], df["Percent"]):
    width = bar.get_width()
    if count > 0:  # skip annotations for zero values
        plt.text(width + max(df["Count"])*0.01,
                 bar.get_y() + bar.get_height()/2,
                 f"{count} ({pct:.1f}%)",
                 va='center', fontsize=10)

# Labels and title
plt.xlabel("Number of Good Practices", fontsize=12)
plt.title("Geographical distribution of good practices by European country in the HL4EU Database (N=122)",
          fontsize=16)

# Clean axes (consistent with other plots)
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

# Proper x limit
plt.xlim(0, max(df["Count"])*1.15)

plt.tight_layout()
plt.show()


