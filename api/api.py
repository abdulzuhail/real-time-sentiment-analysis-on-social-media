import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_FILE = "data/emotion_analysis_results.csv"
ALERT_FILE = "data/alert_flag.txt"
ANOMALY_CSV = "data/anomaly_detection_results.csv"  # ✅ Updated

@app.get("/get_emotion_distribution")
def get_emotion_distribution():
    try:
        df = pd.read_csv(CSV_FILE)
        if "emotion" not in df.columns:
            return {"error": "Missing 'emotion' column in CSV"}
        
        emotion_counts = df["emotion"].value_counts().to_dict()
        return emotion_counts
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_top_locations")
def get_top_locations():
    try:
        df = pd.read_csv(CSV_FILE)
        if "location" not in df.columns:
            return {"error": "Missing 'location' column in CSV"}
        
        location_counts = df["location"].value_counts().head(10).to_dict()
        return location_counts
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_recent_posts")
def get_recent_posts():
    """Fetch the last 10 recent sentiment posts"""
    try:
        df = pd.read_csv(CSV_FILE)
        if "text" not in df.columns or "emotion" not in df.columns:
            return {"error": "Missing required columns in CSV"}
        
        df = df[['text', 'emotion', 'timestamp', 'location']].dropna().tail(10)

        posts = df.to_dict(orient="records")
        return {"posts": posts}
    except Exception as e:
        return {"error": str(e)}

@app.get("/get_sentiment_alert")
def get_sentiment_alert():
    """Returns an alert message if sentiment anomalies are detected"""
    if os.path.exists(ALERT_FILE):
        with open(ALERT_FILE, "r", encoding="utf-8") as f:
            message = f.read().strip()
            return {"alert": True, "message": message}
    return {"alert": False, "message": ""}

@app.get("/get_anomalous_posts")
def get_anomalous_posts():
    """Returns all anomalous posts with score (no limit)"""
    try:
        df = pd.read_csv("data/anomaly_detection_results.csv")
        
        if "text" not in df.columns or "emotion" not in df.columns:
            return {"error": "Missing 'text' or 'emotion' columns in anomaly CSV"}

        # Detect score column
        if "score" in df.columns:
            pass
        elif "sentiment_score" in df.columns:
            df.rename(columns={"sentiment_score": "score"}, inplace=True)
        elif "anomaly_score" in df.columns:
            df.rename(columns={"anomaly_score": "score"}, inplace=True)
        else:
            return {"error": "No valid score column"}

        df = df[['text', 'emotion', 'score']].dropna().sort_values(by="score", ascending=False)

        return {"posts": df.to_dict(orient="records")}
    except Exception as e:
        return {"error": str(e)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8005)
