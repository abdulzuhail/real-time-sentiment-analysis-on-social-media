import praw
import pandas as pd
import os
import re
import spacy

# Load spaCy NLP model
nlp = spacy.load("en_core_web_trf")

# Define regions for location extraction
us_states = [
    "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida",
    "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine",
    "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska",
    "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio",
    "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas",
    "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"
]

countries = [
    "USA", "Canada", "UK", "Germany", "France", "Australia", "India", "China", 
    "Russia", "Brazil", "Japan", "Mexico", "Spain", "Italy", "South Korea"
]

# Function to extract location
def extract_location(text, flair):
    if flair:
        return flair

    doc = nlp(text)
    locations = [ent.text for ent in doc.ents if ent.label_ == "GPE"]
    if locations:
        return locations[0]

    for state in us_states:
        if re.search(rf"\b{state}\b", text, re.IGNORECASE):
            return state

    for country in countries:
        if re.search(rf"\b{country}\b", text, re.IGNORECASE):
            return country

    return "Unknown"

# Authenticate Reddit API
reddit = praw.Reddit(
    client_id="your reddit id",
    client_secret="your reddit secret key",
    user_agent="SentimentAnalyzer:v1.0 (by u/Beneficial_Trust_507)"
)

# Subreddits
country_subreddits = [
     "canada", "india", "germany", "china", "japan","usa"]

# Fetch posts from subreddit
def fetch_reddit_posts(subreddit_name, limit=100):
    try:
        subreddit = reddit.subreddit(subreddit_name)
        posts = []
        for post in subreddit.new(limit=limit):
            combined_text = (post.title or "") + " " + (post.selftext or "")
            location = extract_location(combined_text, post.link_flair_text)
            posts.append([combined_text.strip(), post.created_utc, location, subreddit_name])
        return pd.DataFrame(posts, columns=['text', 'timestamp', 'location', 'source'])
    except Exception as e:
        print(f"❌ Error in r/{subreddit_name}: {e}")
        return pd.DataFrame(columns=['text', 'timestamp', 'location', 'source'])

# Loop through all
def fetch_all_country_news(subreddits, limit=40):
    all_posts = []
    for subreddit in subreddits:
        print(f"🌍 Fetching from r/{subreddit}")
        df = fetch_reddit_posts(subreddit, limit)
        if not df.empty:
            all_posts.append(df)

    # ✅ Fix for pandas FutureWarning
    valid_posts = [df for df in all_posts if df is not None and not df.empty]
    return pd.concat(valid_posts, ignore_index=True) if valid_posts else pd.DataFrame(columns=['text', 'timestamp', 'location', 'source'])

# Main Execution
if __name__ == "__main__":
    df = fetch_all_country_news(country_subreddits, limit=100)
    os.makedirs("data", exist_ok=True)
    df.to_csv("data/geo_sentiment.csv", index=False, encoding="utf-8")
    print(f"✅ Saved {len(df)} posts to data/geo_sentiment.csv")
    print(df.head())

