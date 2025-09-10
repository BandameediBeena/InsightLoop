def calculate_weekly_consistency(df, goals):
    df['date'] = df['date'].dt.date  # Ensure date only
    daily_summary = df.groupby(['date', 'activity'])['duration_hrs'].sum().unstack(fill_value=0)

    consistency = {}
    for activity, target in goals.items():
        achieved_days = (daily_summary[activity] >= target).sum() if activity in daily_summary else 0
        total_days = len(daily_summary)
        percentage = round((achieved_days / total_days) * 100, 2) if total_days > 0 else 0
        consistency[activity] = {
            "achieved_days": int(achieved_days),
            "total_days": int(total_days),
            "consistency": percentage
        }

    return consistency
