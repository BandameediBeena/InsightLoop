import pandas as pd

def read_logs(file_path):
    df = pd.read_csv(file_path)

    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    df['start_dt'] = pd.to_datetime(df['Date'].dt.strftime('%Y-%m-%d') + ' ' + df['time_start'], format='%Y-%m-%d %H:%M', errors='coerce')
    df['end_dt'] = pd.to_datetime(df['Date'].dt.strftime('%Y-%m-%d') + ' ' + df['time_end'], format='%Y-%m-%d %H:%M', errors='coerce')
    df['duration_hrs'] = (df['end_dt'] - df['start_dt']).dt.total_seconds() / 3600.0
    df = df.dropna(subset=['duration_hrs'])

    df['logged_at'] = pd.to_datetime(df['Date'].dt.strftime('%Y-%m-%d') + ' ' + df['logged_at'], format='%Y-%m-%d %H:%M', errors='coerce')
    df['is_late'] = df['logged_at'] > df['end_dt']
    df['late_reason'] = df['is_late'].apply(lambda x: "Logged next day or later" if x else "On time")

    return df
