import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_FILE = "data/sentiment_analysis_results.csv"  # Update with your actual CSV path

@app.get("/get_sentiment_data")
def get_sentiment_data():
    """Fetches the last 20 sentiment data records."""
    if not os.path.exists(CSV_FILE):
        return {"error": f"File '{CSV_FILE}' not found"}

    try:
        df = pd.read_csv(CSV_FILE)

        # Ensure necessary columns exist
        required_columns = ["sentiment", "text", "timestamp"]
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            return {"error": f"Missing required columns: {', '.join(missing_columns)}"}

        # Get last 20 rows
        latest_data = df.tail(20).to_dict(orient="records")
        return {"data": latest_data}
    
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
