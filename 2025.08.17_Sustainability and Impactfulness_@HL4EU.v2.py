import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------------
# Data
# ------------------------------
sustainable_counts = [50, 72]  # Sustainable / Non-sustainable
impact_counts = [111, 11]      # Impactful / Non-impactful

sustainable_labels = ["Sustainable", "Non-sustainable"]
impact_labels = ["Impactful", "Non-impactful"]

# ------------------------------
# Colors from Seaborn
# ------------------------------
colors_sust = sns.color_palette("YlGnBu", 2)
colors_impact = sns.color_palette("YlGnBu_r", 2)

# ------------------------------
# Plot
# ------------------------------
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

# Sustainable pie chart
axes[0].pie(sustainable_counts, 
            labels=sustainable_labels, 
            autopct=lambda p: f"{round(p*sum(sustainable_counts)/100)} ({p:.1f}%)",
            colors=colors_sust, startangle=90, counterclock=False, wedgeprops={"edgecolor":"white"})
axes[0].set_title("Sustainable Practices (N=122)", fontsize=14)

# Impactful pie chart
axes[1].pie(impact_counts, 
            labels=impact_labels, 
            autopct=lambda p: f"{round(p*sum(impact_counts)/100)} ({p:.1f}%)",
            colors=colors_impact, startangle=90, counterclock=False, wedgeprops={"edgecolor":"white"})
axes[1].set_title("Impactful Practices (N=122)", fontsize=14)

plt.tight_layout()
plt.show()

