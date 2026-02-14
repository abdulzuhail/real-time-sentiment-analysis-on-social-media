import pandas as pd
from prophet import Prophet
import numpy as np

def load_data(file_path="data/sentiment_analysis_results.csv"):
    df = pd.read_csv(file_path)

    if "sentiment" not in df.columns:
        raise ValueError("❌ 'sentiment' column missing in dataset!")

    # Convert timestamps (handle seconds or ms)
    try:
        df["timestamp"] = pd.to_datetime(df["timestamp"], unit="s")
    except:
        df["timestamp"] = pd.to_datetime(df["timestamp"])

    sentiment_map = {"POSITIVE": 1, "NEUTRAL": 0, "NEGATIVE": -1}
    df["sentiment_score"] = df["sentiment"].map(sentiment_map)
    df.dropna(subset=["sentiment_score"], inplace=True)

    # 🗓️ Group by day to smooth noise
    df["date"] = df["timestamp"].dt.date
    daily_df = df.groupby("date")["sentiment_score"].mean().reset_index()
    daily_df.columns = ["ds", "y"]

    print(f"✅ Loaded & grouped data: {len(daily_df)} daily points")
    return daily_df

def train_forecast_model(df, periods=10):
    if len(df) < 10:
        raise ValueError("❌ Not enough data for forecasting! At least 10 days required.")

    model = Prophet(daily_seasonality=True)
    model.fit(df)

    future = model.make_future_dataframe(periods=periods, freq="D")
    forecast = model.predict(future)

    return forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]]

if __name__ == "__main__":
    print("🔍 Loading data...")
    df = load_data()

    print("📈 Training forecasting model...")
    forecast = train_forecast_model(df, periods=7)

    forecast.to_csv("data/sentiment_trends.csv", index=False)
    print("✅ Forecast saved to data/sentiment_trends.csv")
    print(forecast.head())
