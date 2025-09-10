import json

def load_goals(path='config/goals.json'):
    with open(path, 'r') as f:
        return json.load(f)

def evaluate_goals(df, goals):
    results = {}
    latest_date = df['Date'].max()
    day_data = df[df['Date'] == latest_date]

    for activity, target in goals.items():
        filtered = day_data[day_data['activity'].str.lower() == activity.lower()]
        total_duration = filtered['duration_hrs'].sum()
        status = "✅" if total_duration >= target else "❌"
        results[activity] = {
            "actual": round(total_duration, 2),
            "target": target,
            "status": status
        }

    return results
