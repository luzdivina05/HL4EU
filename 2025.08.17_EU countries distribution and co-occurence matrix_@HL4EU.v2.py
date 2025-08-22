import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- #
# Load Excel file
# -------------------- #
file_path = r"C:/Users/User/OneDrive - Universidad Nacional de Colombia/Desktop/Trabajo/EIEIM/HL4EU/Database/v2/2025.08.16._Good practices database_descriptive stats_@HL4EU.xlsx"
sheet_name = "geo_EU"

# Read the sheet: Columns L–BB = countries (L is column 12 in 0-based indexing)
df = pd.read_excel(file_path, sheet_name=sheet_name, usecols="L:BB")

# Clean column names (country names from first row)
df.columns = [col.strip() for col in df.columns]

# Remove the first row if it contains country names (assuming data starts from row 2)
# If the first row contains country names and you want to keep it as headers, skip this line
# If the first row contains data, keep this line commented
# countries_df = df.iloc[1:].reset_index(drop=True)
countries_df = df

# Total number of Good Practices
total_gp = len(countries_df)

# -------------------- #
# 1. Country Distribution (Bar Chart)
# -------------------- #
country_totals = countries_df.sum().sort_values()
country_percent = (country_totals / total_gp * 100).round(1)

plt.figure(figsize=(12, 8))  # Slightly larger for country names
# Use same colormap as heatmap (YlGnBu)
colors = sns.color_palette("YlGnBu", len(country_totals))
bars = plt.barh(country_totals.index, country_totals.values, color=colors)

# Add count + percentage labels
for i, bar in enumerate(bars):
    width = bar.get_width()
    label = f"{int(width)} ({country_percent[i]}%)"
    plt.text(width + 0.5, bar.get_y() + bar.get_height() / 2, 
             label, va='center', fontsize=10)

# Clean borders
ax = plt.gca()
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

plt.title(f"European Countries Distribution in the HL4EU Database (N={total_gp})", fontsize=16)
plt.xlabel("Number of Good Practices", fontsize=12)
plt.ylabel("Countries", fontsize=12)
plt.tight_layout()
plt.show()

# -------------------- #
# 2. Country Co-occurrence Matrix (Absolute Counts)
# -------------------- #
co_occurrence = countries_df.T.dot(countries_df)
mask = np.triu(np.ones_like(co_occurrence, dtype=bool))  # Keep lower triangle

plt.figure(figsize=(14, 12))  # Larger figure for country names
sns.heatmap(co_occurrence, mask=mask, annot=True, fmt="d", 
            cmap="YlGnBu", cbar=False, linewidths=0.5, square=True, 
            annot_kws={"fontsize": 8})  # Smaller font for readability

plt.title("European Countries Co-occurrence Matrix (Count of good practices)", fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# -------------------- #
# 3. Country Co-occurrence Matrix (Percentages of Total)
# -------------------- #
co_occurrence_pct = (co_occurrence / total_gp) * 100

plt.figure(figsize=(14, 12))  # Larger figure for country names
sns.heatmap(co_occurrence_pct, mask=mask, annot=True, fmt=".1f", 
            cmap="YlGnBu", cbar_kws={'label': f'% of Good Practices (N={total_gp})'},
            linewidths=0.5, square=True, annot_kws={"fontsize": 8})

plt.title("European Countries Co-occurrence Matrix (% of Good Practices)", fontsize=16)
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# -------------------- #
# Optional: Display basic statistics
# -------------------- #
print(f"Total Good Practices analyzed: {total_gp}")
print(f"Number of European countries: {len(countries_df.columns)}")
print(f"\nCountries in dataset:")
print(list(countries_df.columns))
print(f"\nTop 5 countries by number of good practices:")
print(country_totals.tail().to_string())
