import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime
import os

# Create output folder if it doesn't exist
if not os.path.exists("charts"):
    os.makedirs("charts")

# Simulated weekly activity data
data = {
    'Date': pd.date_range(start='2025-06-24', periods=7, freq='D'),
    'Study': [2, 1.5, 2.5, 0, 2, 2, 1],
    'Exercise': [1, 0.5, 1, 1, 1, 0.5, 1],
    'Sleep': [7, 6.5, 8, 7, 7.5, 8, 6],
}

df = pd.DataFrame(data)
df.set_index('Date', inplace=True)

# Bar Chart: Study Hours Over the Week
plt.figure(figsize=(10, 5))
plt.bar(df.index.strftime('%a %d-%b'), df['Study'], color='skyblue')
plt.title('Study Hours Over the Week')
plt.xlabel('Day')
plt.ylabel('Hours Spent')
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True, axis='y')
plt.savefig("charts/study_hours_bar_chart.png")
plt.show()  # <-- This will open the chart window

# Pie Chart: Weekly Activity Distribution
total_time = df.sum()
plt.figure(figsize=(6, 6))
plt.pie(total_time, labels=total_time.index, autopct='%1.1f%%', startangle=140,
        colors=['lightgreen', 'orange', 'purple'])
plt.title('Weekly Activity Distribution')
plt.savefig("charts/weekly_activity_pie_chart.png")
plt.show()  # <-- This will open the chart window
