import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import matplotlib.patches as mpatches
import seaborn as sns

# Apply Seaborn theme
sns.set_theme(style="white")

# Data
total = 122  # sum of all categories including overlaps and none
subsets = (5, 18, 1, 20, 0, 40, 16)

# Colors
colors = {
    "Technological": "#E69F00",  # Orange
    "Methodological": "#009E73", # Green
    "Social": "#56B4E9",         # Blue
}

# Plot
plt.figure(figsize=(10, 8))
venn = venn3(
    subsets=subsets,
    set_labels=("", "", ""),  # No internal labels
    set_colors=(colors["Technological"], colors["Methodological"], colors["Social"]),
    alpha=0.6
)

# Font size for numbers and %
label_fontsize = 12

# Add custom labels with counts and percentages
ids = ['100','010','110','001','101','011','111']
for i, vid in enumerate(ids):
    label = venn.get_label_by_id(vid)
    if label:
        value = subsets[i]
        pct = value / total * 100
        label.set_text(f"{value}\n({pct:.2f}%)")
        label.set_fontsize(label_fontsize)

# Title
plt.title("Type of Innovation Distribution (N=122)", fontsize=16, pad=20)

# Legend
tech_patch = mpatches.Patch(color=colors["Technological"], label='Technological')
meth_patch = mpatches.Patch(color=colors["Methodological"], label='Methodological')
soc_patch  = mpatches.Patch(color=colors["Social"], label='Social')

plt.legend(handles=[tech_patch, meth_patch, soc_patch],
           loc='upper right', fontsize=12, frameon=False)

# Remove spines
sns.despine()

plt.tight_layout()
plt.show()
