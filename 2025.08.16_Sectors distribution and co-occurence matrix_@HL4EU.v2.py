import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- #
# Load Excel file
# -------------------- #
file_path = r"C:/Users/User/OneDrive - Universidad Nacional de Colombia/Desktop/Trabajo/EIEIM/HL4EU/Database/v2/2025.08.16._Good practices database_descriptive stats_@HL4EU.xlsx"
sheet_name = "sectors"

# Read the sheet: Column A = project codes, Columns B–K = sectors
df = pd.read_excel(file_path, sheet_name=sheet_name, usecols="A:K")

# Drop project codes (column A) and keep only sector columns
sector_df = df.iloc[:, 1:]  

# Clean column names
sector_df.columns = [col.strip() for col in sector_df.columns]

# Total number of Good Practices
total_gp = len(sector_df)


# -------------------- #
# 1. Sector Distribution (Bar Chart)
# -------------------- #
sector_totals = sector_df.sum().sort_values()
sector_percent = (sector_totals / total_gp * 100).round(1)

plt.figure(figsize=(10, 7))

# Use same colormap as heatmap (YlGnBu)
colors = sns.color_palette("YlGnBu", len(sector_totals))
bars = plt.barh(sector_totals.index, sector_totals.values, color=colors)

# Add count + percentage labels
for i, bar in enumerate(bars):
    width = bar.get_width()
    label = f"{int(width)} ({sector_percent[i]}%)"
    plt.text(width + 0.5, bar.get_y() + bar.get_height() / 2,
             label, va='center', fontsize=12)

# Clean borders
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.title(f"Sectors distribution in the HL4EU Database (N={total_gp})", fontsize=16)
plt.xlabel("Number of Good Practices", fontsize=12)
plt.tight_layout()
#plt.figtext(0.5, -0.05,
#            "Visualization by Luz Divina DE LA CRUZ LASTRE in Python 3.12",
#            wrap=True, horizontalalignment='center', fontsize=8, style='italic')
plt.show()


# -------------------- #
# 2. Sector Co-occurrence Matrix (Absolute Counts)
# -------------------- #
co_occurrence = sector_df.T.dot(sector_df)
mask = np.triu(np.ones_like(co_occurrence, dtype=bool))  # Keep lower triangle

plt.figure(figsize=(10, 8))
sns.heatmap(co_occurrence, mask=mask, annot=True, fmt="d", cmap="YlGnBu", cbar=False,
            linewidths=0.5, square=True, annot_kws={"fontsize": 10})

plt.title("Sector Co-occurrence Matrix (Count of good practices)", fontsize=16)
plt.tight_layout()
#plt.figtext(0.5, -0.05,
#            "Visualization by Luz Divina DE LA CRUZ LASTRE in Python 3.12",
#            wrap=True, horizontalalignment='center', fontsize=8, style='italic')
plt.show()


# -------------------- #
# 3. Sector Co-occurrence Matrix (Percentages of Total)
# -------------------- #
co_occurrence_pct = (co_occurrence / total_gp) * 100

plt.figure(figsize=(10, 8))
sns.heatmap(co_occurrence_pct, mask=mask, annot=True, fmt=".1f", cmap="YlGnBu",
            cbar_kws={'label': f'% of Good Practices (N={total_gp})'},
            linewidths=0.5, square=True, annot_kws={"fontsize": 10})

plt.title("Sector Co-occurrence Matrix (% of Good Practices)", fontsize=16)
plt.tight_layout()
#plt.figtext(0.5, -0.05,
#            "Visualization by Luz Divina DE LA CRUZ LASTRE in Python 3.12",
#            wrap=True, horizontalalignment='center', fontsize=8, style='italic')
plt.show()
