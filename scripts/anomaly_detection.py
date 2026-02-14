import pandas as pd
import numpy as np
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import MinMaxScaler
import os
import json
import time

ALERT_PATH = "data/alert_flag.txt"
CSV_INPUT = "data/emotion_analysis_results.csv"
CSV_OUTPUT = "data/anomaly_detection_results.csv"
JSON_OUTPUT = "data/anomaly_posts.json"

# Load Data
def load_data(file_path=CSV_INPUT):
    df = pd.read_csv(file_path)
    if "emotion" not in df.columns:
        raise KeyError("❌ Missing 'emotion' column!")
    print(f"✅ Loaded data: {df.shape}")
    return df

# Convert emotion to score
def emotion_to_score(emotion):
    emotion_map = {
        "joy": 1.0, "love": 0.8, "happy": 1.0,
        "surprise": 0.5, "neutral": 0.0,
        "sadness": -0.6, "anger": -1.0,
        "fear": -0.8, "disgust": -1.0
    }
    return emotion_map.get(str(emotion).lower(), 0.0)

# Detect anomalies
def detect_anomalies(df, contamination=0.05):
    df["sentiment_score"] = df["emotion"].apply(emotion_to_score)

    if df["sentiment_score"].var() == 0:
        print("⚠️ No variance in sentiment scores. Skipping IsolationForest.")
        df["anomaly"] = "normal"
        df["anomaly_score"] = 0.0
        return df

    model = IsolationForest(contamination=contamination, random_state=42)
    df["anomaly_raw"] = model.fit_predict(df[["sentiment_score"]])
    df["anomaly_score_raw"] = model.decision_function(df[["sentiment_score"]])

    scaler = MinMaxScaler()
    df["anomaly_score"] = 1 - scaler.fit_transform(df[["anomaly_score_raw"]])
    df["anomaly"] = df["anomaly_raw"].apply(lambda x: "anomalous" if x == -1 else "normal")

    return df

# Save results
def save_results(df, path=CSV_OUTPUT):
    df.to_csv(path, index=False)
    print(f"💾 Saved results to {path}")

# Save anomalies
def save_anomalous_posts(df, path=JSON_OUTPUT):
    df[df["anomaly"] == "anomalous"][["text", "emotion", "anomaly_score"]].to_json(
        path, orient="records", force_ascii=False
    )
    print(f"📤 Anomalous posts saved to {path}")

# Trigger alert
def trigger_alert(df, alert_path=ALERT_PATH, force=False):
    serious_threshold = -0.6
    anomalies = df[df["anomaly"] == "anomalous"]
    serious = anomalies[anomalies["sentiment_score"] <= serious_threshold]

    print(f"🔍 Total anomalies: {len(anomalies)}")
    print(f"🚨 Serious anomalies: {len(serious)}")

    if force or not anomalies.empty:
        alert_text = "🚨 Alert: "
        if force:
            alert_text += "Strong negative sentiment anomaly detected.\n"
        elif not serious.empty:
            alert_text += "Sudden spike in public *anger, fear, or disgust* detected.\n"
        else:
            alert_text += "Unusual sentiment activity detected.\n"

        timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        alert_text += f"Time: {timestamp}"

        with open(alert_path, "w", encoding="utf-8") as f:
            f.write(alert_text)
        print("⚠️ ALERT TRIGGERED & FILE WRITTEN ✅")
    else:
        if os.path.exists(alert_path):
            os.remove(alert_path)
            print("ℹ️ No alert file to remove.")

# Run all
if __name__ == "__main__":
    print("🔍 Loading data...")
    df = load_data()

    print("🧠 Running anomaly detection...")
    df = detect_anomalies(df)

    print("📢 Evaluating sentiment alert...")
    # 👇 Change force=True to test alert popup even without real anomaly
    trigger_alert(df, force=True)

    print("📁 Writing results...")
    save_results(df)
    save_anomalous_posts(df)

    print("✅ DONE")
