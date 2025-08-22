import pandas as pd
from upsetplot import UpSet, from_indicators
import matplotlib.pyplot as plt

# Load Excel file
file_path = r"C:/Users/User/OneDrive - Universidad Nacional de Colombia/Desktop/Trabajo/EIEIM/HL4EU/Database/v2/2025.08.16._Good practices database_descriptive stats_@HL4EU.xlsx"
sheet_name = "geo_EU"

# Read the sheet: Columns L–BC contain countries, row 1 = headers, data from row 2
countries_df = pd.read_excel(file_path, sheet_name=sheet_name, usecols="L:BB")

# Set project codes as index (assuming first column in sheet is project codes)
countries_df.set_index(countries_df.columns[0], inplace=True)

# Clean column names (remove spaces if any)
countries_df.columns = [col.strip() for col in countries_df.columns]

# Convert to boolean indicators (1 = True, 0 or NaN = False)
countries_bool = countries_df.notna() & (countries_df != 0)

# Build UpSet data
country_names = countries_bool.columns.tolist()
upset_data = from_indicators(country_names, countries_bool)

# Create bigger figure
plt.figure(figsize=(14, 10))

# Create UpSet plot
upset = UpSet(
    upset_data,
    show_counts=True,
    sort_by='cardinality',
    intersection_plot_elements=20
)
upset.plot()

# Recolor bars in intersection plot (left axis) to black
bar_ax = [ax for ax in plt.gcf().axes if ax.get_ylabel() == 'Intersection size'][0]
for patch in bar_ax.patches:
    patch.set_facecolor('black')

# Expert-level: attach title to the intersection bars axes
bar_ax.set_title(
    "European countries intersection size distribution in HL4EU Database N(108)",
    fontsize=16,
    pad=20  # distance above the bars; adjust as needed
)

# Adjust layout slightly to avoid clipping
plt.tight_layout()

plt.show()
