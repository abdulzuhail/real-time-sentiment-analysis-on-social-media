import pandas as pd
from transformers import pipeline
from tqdm import tqdm

# Load Preprocessed Data
def load_data(file_path="data/processed_sentiment_data.csv"):
    df = pd.read_csv(file_path)
    if "translated_text" not in df.columns:
        raise ValueError("❌ 'translated_text' column missing in dataset!")
    return df

# Load Sentiment Analysis Model (Multilingual BERT-based)
print("🔁 Loading sentiment analysis model...")
sentiment_model = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Mapping Function for Star Ratings
def map_sentiment_label(label):
    mapping = {
        "1 star": "NEGATIVE",
        "2 stars": "NEGATIVE",
        "3 stars": "NEUTRAL",
        "4 stars": "POSITIVE",
        "5 stars": "POSITIVE",
    }
    return mapping.get(label, "UNKNOWN")

# Batch Sentiment Prediction
def predict_sentiment_batch(texts):
    results = []
    for result in sentiment_model(texts, truncation=True):
        label = result['label']
        results.append(map_sentiment_label(label))
    return results

# Process Entire Dataset
def analyze_sentiment(df):
    texts = df["translated_text"].astype(str).fillna("")
    sentiments = []
    batch_size = 32

    print("🧠 Predicting sentiment in batches...")
    for i in tqdm(range(0, len(texts), batch_size)):
        batch = texts[i:i + batch_size].tolist()
        try:
            sentiments.extend(predict_sentiment_batch(batch))
        except Exception as e:
            print(f"❌ Batch error at index {i}: {e}")
            sentiments.extend(["UNKNOWN"] * len(batch))

    df["sentiment"] = sentiments
    return df

# Save Sentiment Data
def save_sentiment_data(df, file_path="data/sentiment_analysis_results.csv"):
    df.to_csv(file_path, index=False)
    print(f"✅ Sentiment analysis results saved to {file_path}")

# Execute script
if __name__ == "__main__":
    print("📂 Loading preprocessed data...")
    df = load_data()

    print("📊 Analyzing sentiment...")
    df = analyze_sentiment(df)

    print("💾 Saving results...")
    save_sentiment_data(df)

    print(df.head())
    print("✅ Sentiment analysis completed successfully!")
