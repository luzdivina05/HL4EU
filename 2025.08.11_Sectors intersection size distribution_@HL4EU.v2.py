import pandas as pd
from upsetplot import UpSet, from_indicators
import matplotlib.pyplot as plt

# Load Excel file (same path as before)
file_path = r"C:/Users/User/OneDrive - Universidad Nacional de Colombia/Desktop/Trabajo/EIEIM/HL4EU/Database/v2/2025.08.16._Good practices database_descriptive stats_@HL4EU.xlsx"
sheet_name = "sectors"

# Read the sheet: Column A = project codes, Columns B–K = sectors
sectors_df = pd.read_excel(file_path, sheet_name=sheet_name, usecols="A:K")

# Set project codes as index
sectors_df.set_index(sectors_df.columns[0], inplace=True)

# Clean column names (remove spaces, if any)
sectors_df.columns = [col.strip() for col in sectors_df.columns]

# Convert to boolean indicators (1 = True, 0 or NaN = False)
sectors_bool = sectors_df.notna() & (sectors_df != 0)

# Reorder columns (B–K) to the original order
desired_order = sectors_df.columns.tolist()
sectors_bool = sectors_bool[desired_order]

# Build UpSet data
upset_data = from_indicators(desired_order, sectors_bool)

# Create bigger figure
plt.figure(figsize=(12, 9))

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

# Title and footer
plt.suptitle("Sectors intersection size distribution in the HL4EU database (N=122)", fontsize=16, y=1.02)
#plt.figtext(
#    0.5, 0.02,
#    "Visualization by Luz Divina DE LA CRUZ LASTRE in Python 3.12",
#    ha="center", fontsize=10, style="italic"
#)

# Adjust layout
plt.subplots_adjust(top=0.90, bottom=0.12)

plt.show()
