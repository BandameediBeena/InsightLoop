# modules/chart_generator.py

import matplotlib.pyplot as plt
import os

# ✅ FUNCTION 1: Bar Chart (Actual duration per activity)
def generate_bar_chart(df):
    latest_date = df['Date'].max()
    day_data = df[df['Date'] == latest_date]

    activities = ['Study', 'Gym', 'Mobile']
    durations = []

    for activity in activities:
        filtered = day_data[day_data['activity'].str.lower() == activity.lower()]
        total_duration = filtered['duration_hrs'].sum()
        durations.append(round(total_duration, 2))

    if not os.path.exists("charts"):
        os.makedirs("charts")

    plt.bar(activities, durations, color=['skyblue', 'green', 'orange'])
    plt.title(f"Activity Duration on {latest_date.date()}")
    plt.ylabel("Hours")
    plt.tight_layout()
    plt.savefig(f"charts/bar_chart_{latest_date.date()}.png")
    plt.show()
    plt.close()

# ✅ FUNCTION 2: Comparison Chart (Actual vs Target)
def generate_comparison_chart(df, goals):
    latest_date = df['Date'].max()
    day_data = df[df['Date'] == latest_date]

    activities = list(goals.keys())
    actuals = []
    targets = []

    for activity in activities:
        filtered = day_data[day_data['activity'].str.lower() == activity.lower()]
        total_duration = filtered['duration_hrs'].sum()
        actuals.append(round(total_duration, 2))
        targets.append(goals[activity])

    x = range(len(activities))
    width = 0.35

    fig, ax = plt.subplots()
    ax.bar([i - width/2 for i in x], actuals, width, label='Actual Hours', color='skyblue')
    ax.bar([i + width/2 for i in x], targets, width, label='Target Hours', color='orange')

    ax.set_ylabel('Hours')
    ax.set_title(f"Actual vs Target on {latest_date.date()}")
    ax.set_xticks(x)
    ax.set_xticklabels(activities)
    ax.legend()

    if not os.path.exists("charts"):
        os.makedirs("charts")

    plt.tight_layout()
    plt.savefig(f"charts/comparison_chart_{latest_date.date()}.png")
    plt.show()
    plt.close()
