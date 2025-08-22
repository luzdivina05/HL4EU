import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import matplotlib.patches as mpatches
import seaborn as sns

# Apply Seaborn theme
sns.set_theme(style="white")

# Data
total = 122  # sum of all categories including overlaps and none
subsets = (5, 18, 1, 20, 0, 40, 16)
none_count = 22  # None category
none_pct = none_count / total * 100

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
        label.set_text(f"{value}\n({pct:.1f}%)")
        label.set_fontsize(label_fontsize)

# Title
plt.title("Type of Innovation Distribution in the HL4EU database (N=122)", fontsize=16, pad=20)

# Legend
tech_patch = mpatches.Patch(color=colors["Technological"], label='Technological')
meth_patch = mpatches.Patch(color=colors["Methodological"], label='Methodological')
soc_patch  = mpatches.Patch(color=colors["Social"], label='Social')

plt.legend(handles=[tech_patch, meth_patch, soc_patch],
           loc='upper right', fontsize=10, frameon=False)

# Add 'None' category box in bottom-right corner
plt.text(
    0.9, -0.15, f"None: {none_count} ({none_pct:.1f}%)",
    transform=plt.gca().transAxes,
    fontsize=12,
    va='bottom', ha='left',
    bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1)
)

# Remove spines
sns.despine()

plt.tight_layout()
plt.show()


