def generate_weekly_report(consistency_data, filename="weekly_report.txt"):
    with open(filename, "w") as file:
        file.write("📈 Weekly Consistency Report\n\n")
        for activity, stats in consistency_data.items():
            file.write(f"{activity}:\n")
            file.write(f"  - Achieved on: {stats['achieved_days']} out of {stats['total_days']} days\n")
            file.write(f"  - Consistency: {stats['consistency']}%\n\n")
