import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_FILE = "data/emotion_analysis_results.csv"  # Ensure correct path

@app.get("/get_geo_data")
def get_geo_data():
    try:
        df = pd.read_csv(CSV_FILE)

        if "location" not in df.columns or "emotion" not in df.columns:
            return {"error": "CSV file missing required columns"}

        latest_data = df[["location", "emotion","source"]].dropna().to_dict(orient="records")
        return {"data": latest_data}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)
