import matplotlib.pyplot as plt
import pandas as pd

# Path data engagement
data_path = "../data/engagement_report.csv"

# Membaca data engagement
data = pd.read_csv(data_path)

# Persiapkan data untuk grafik
platforms = data["platform"]
likes = data["likes"]
comments = data["comments"]
shares = data["shares"]

# Grafik 1: Bar Chart untuk Likes, Comments, Shares
fig, ax = plt.subplots(figsize=(10, 6))

ax.bar(platforms, likes, width=0.2, label="Likes", align='center')
ax.bar(platforms, comments, width=0.2, label="Comments", align='edge')
ax.bar(platforms, shares, width=0.2, label="Shares", align='edge')

ax.set_xlabel('Platform')
ax.set_ylabel('Count')
ax.set_title('Social Media Engagement by Platform')
ax.legend()

plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("../logs/social_engagement_bar_chart.png")  # Save the chart
plt.show()

# Grafik 2: Pie Chart untuk Engagement
total_engagement = likes + comments + shares
fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(total_engagement, labels=platforms, autopct='%1.1f%%', startangle=90)
ax.set_title('Social Media Engagement Distribution')
plt.savefig("../logs/social_engagement_pie_chart.png")  # Save the pie chart
plt.show()
