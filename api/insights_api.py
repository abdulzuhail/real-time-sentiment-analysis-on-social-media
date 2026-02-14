import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Enable CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CSV_FILE = "data/sentiment_analysis_results.csv"

@app.get("/get_sentiment_insights")
def get_sentiment_insights():
    try:
        df = pd.read_csv(CSV_FILE)
        
        # Count sentiment occurrences
        sentiment_counts = df["sentiment"].value_counts(normalize=True) * 100

        insights = {
            "positive": round(sentiment_counts.get("POSITIVE", 0), 2),
            "negative": round(sentiment_counts.get("NEGATIVE", 0), 2),
            "neutral": round(sentiment_counts.get("NEUTRAL", 0), 2),
            "total_posts": len(df)
        }
        
        return {"insights": insights}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8004)
