import pandas as pd
from transformers import pipeline
from tqdm import tqdm

# Load Preprocessed Data
def load_data(file_path="data/processed_sentiment_data.csv"):
    df = pd.read_csv(file_path)

    if "translated_text" not in df.columns:
        raise ValueError("❌ 'translated_text' column missing!")
    
    return df

# Load Emotion Detection Model (RoBERTa-based)
print("🔄 Loading emotion detection model...")
emotion_model = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base")

# Emotion Prediction Function
def predict_emotion_batch(texts):
    """Run emotion detection in batch with fallback handling."""
    results = []
    for result in emotion_model(texts, truncation=True):
        results.append(result['label'])
    return results

# Analyze Emotions
def analyze_emotions(df):
    print("🧠 Predicting emotions...")
    texts = df["translated_text"].astype(str).fillna("")

    # Break into batches of 32 for faster processing
    batch_size = 32
    emotions = []
    for i in tqdm(range(0, len(texts), batch_size)):
        batch = texts[i:i+batch_size].tolist()
        try:
            emotions.extend(predict_emotion_batch(batch))
        except Exception as e:
            print(f"❌ Batch error at index {i}: {e}")
            emotions.extend(["UNKNOWN"] * len(batch))

    df["emotion"] = emotions
    return df

# Save Results
def save_emotion_data(df, file_path="data/emotion_analysis_results.csv"):
    df.to_csv(file_path, index=False)
    print(f"✅ Emotion results saved to {file_path}")

# Execute
if __name__ == "__main__":
    print("📂 Loading preprocessed sentiment data...")
    df = load_data()

    df = analyze_emotions(df)

    print("💾 Saving updated emotion data...")
    save_emotion_data(df)

    print("✅ Emotion detection completed successfully!")
    print(df.head())
