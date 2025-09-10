from modules.input_handler import read_logs
from modules.goal_tracker import load_goals, evaluate_goals
from modules.chart_generator import generate_bar_chart, generate_comparison_chart
from modules.chart_generator import generate_bar_chart, generate_comparison_chart

import pandas as pd

# Load data
log_path = "logs/sample_log.csv"
goal_path = "config/goals.json"
df = read_logs(log_path)
goals = load_goals(goal_path)

# Track goal results
results = evaluate_goals(df, goals)

# Show comparison chart
generate_comparison_chart(df, goals)

# Print report
print("\n📊 Daily Goal Report:")
for activity, data in results.items():
    print(f"{activity}: {data['actual']} hrs (Target: {data['target']} hrs) → {data['status']}")

# Check late logs
late_logs = df[df['is_late']]
if not late_logs.empty:
    print("\n⏱ Late Log Entries (not logged on the same day):")
    for _, row in late_logs.iterrows():
        print(f"{row['activity']} on {row['Date'].date()} → {row['late_reason']}")
else:
    print("\n✅ All activities were logged on the same day.")
