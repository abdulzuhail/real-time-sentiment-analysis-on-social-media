import re
import pandas as pd
from deep_translator import GoogleTranslator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load data
def load_data(file_path="data/geo_sentiment.csv"):
    """Loads the collected Reddit data from CSV with UTF-8 encoding."""
    df = pd.read_csv(file_path, encoding="utf-8")
    return df

# Text Cleaning
def preprocess_text(text):
    """Cleans text by removing URLs, mentions, hashtags, punctuation, and numbers."""
    if pd.isna(text):
        return ""  # Handle missing values safely
    text = re.sub(r'http\S+', '', text)  # Remove URLs
    text = re.sub(r'@\w+', '', text)     # Remove mentions
    text = re.sub(r'#\w+', '', text)     # Remove hashtags
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    text = re.sub(r'\d+', '', text)      # Remove numbers
    text = text.lower().strip()          # Convert to lowercase
    return text

# Language Translation
def translate_text(text, target_lang='en'):
    """Translates text to English for uniform sentiment analysis."""
    try:
        return GoogleTranslator(source='auto', target=target_lang).translate(text)
    except:
        return text  # If translation fails, return the original text

# Sarcasm Detection using VADER
analyzer = SentimentIntensityAnalyzer()

def detect_sarcasm(text):
    """Detects sarcasm based on sentiment score thresholds."""
    score = analyzer.polarity_scores(text)['compound']
    return "sarcastic" if score > 0.8 or score < -0.8 else "not_sarcastic"

# Process entire dataset
def preprocess_dataset(df):
    """Applies preprocessing steps on the dataset."""
    df['text'] = df['text'].astype(str).apply(preprocess_text)
    df['translated_text'] = df['text'].apply(lambda x: translate_text(x, 'en'))
    df['sarcasm_label'] = df['translated_text'].apply(detect_sarcasm)

    # Ensure timestamp, location, and optionally source are retained
    columns = ['text', 'translated_text', 'sarcasm_label', 'timestamp', 'location']
    if 'source' in df.columns:
        columns.append('source')

    return df[columns]

# Save Preprocessed Data
def save_preprocessed_data(df, file_path="data/processed_sentiment_data.csv"):
    """Saves the preprocessed dataset as CSV with UTF-8 encoding."""
    df.to_csv(file_path, index=False, encoding="utf-8")
    print(f"✅ Preprocessed data saved to {file_path}")

# Execute script
if __name__ == "__main__":
    print("🔄 Loading raw data...")
    df = load_data()
    
    print("🛠️ Preprocessing text...")
    df = preprocess_dataset(df)
    
    print("💾 Saving preprocessed data...")
    save_preprocessed_data(df)
    
    print("✅ Preprocessing completed successfully!")
    print(df.head())  # Show preview
