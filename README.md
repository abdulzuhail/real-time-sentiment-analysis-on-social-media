# 📊 Real-Time Sentiment Analysis on Social Media

This project is a real-time sentiment analysis system designed to monitor and analyze public opinion from Reddit. It leverages NLP, deep learning, and anomaly detection to extract meaningful insights from live social media data.

## 🚀 Project Overview

With the increasing volume of user-generated content on platforms like Reddit, understanding sentiment in real-time is crucial for businesses, researchers, and policymakers. This system collects live Reddit posts, classifies sentiment and emotions, detects anomalies, and visualizes insights through an interactive dashboard.

## 🧠 Features

- **Real-Time Data Collection** using Reddit API (PRAW)
- **Sentiment Classification** using BERT (Positive, Negative, Neutral)
- **Emotion Detection** using RoBERTa (Joy, Anger, Sadness, etc.)
- **Sarcasm Detection** using VADER
- **Anomaly Detection** with Isolation Forest
- **Time-Series Forecasting** using Prophet
- **Multilingual Translation** using Deep Translator
- **Geographical Analysis** from user-provided locations
- **Interactive Dashboard** built using Streamlit and React

## 🧰 Tech Stack

- **Backend**: Python, FastAPI, PRAW, Hugging Face Transformers, Scikit-learn, Prophet, Deep Translator
- **Frontend**: ReactJS, Streamlit
- **Visualization**: Plotly, Matplotlib
- **Deployment**: Scheduled scripts run every 10 minutes to update data and analysis

## 📂 Project Structure
---



## 🗂️ Project Structure


<pre>
├── api/
│ ├── api.py
│ ├── geo_api.py
│ ├── insights_api.py
│ ├── sentiment_data_api.py
│ └── trends_api.py
├── app/
│ └── dashboard.py
├── scripts/
│ ├── data_collection.py
│ ├── preprocessing.py
│ ├── emotion_detection.py
│ ├── sentiment_analysis.py
│ ├── anomaly_detection.py
│ └── sentiment_forecasting.py
├── frontend/
│ ├── components/
│ ├── pages/
│ ├── styles/
│ └── App.js
├── data/
│ └── [CSV and JSON output files]
├── logs/
├── requirements.txt
└── README.md
</pre>

---

## 📈 Dashboard Preview

The dashboard displays:
- Live sentiment and emotion trends
- Anomalous posts with filtering
- Geographical emotion mapping
- Recent posts and alerts
- Predictive sentiment trends

## 🧪 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/real-time-sentiment-analysis.git
cd real-time-sentiment-analysis
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Run backend scripts (schedule via cron or Task Scheduler)

```bash
python scripts/data_collection.py
python scripts/preprocessing.py
python scripts/emotion_detection.py
python scripts/sentiment_analysis.py
python scripts/anomaly_detection.py
python scripts/sentiment_forecasting.py
```

### 4. Start FastAPI
```bash
uvicorn api.api:app --reload --port 8005
```
### 5. Start the dashboard
```bash
cd app
streamlit run dashboard.py
```
### 6. Start React Frontend
```bash
cd frontend
npm install
npm start
```
### 📊 Dashboard Features
Live Sentiment Trends by time and location
Emotion Heatmaps
Top Posts with High Emotion Scores
Anomaly Alerts
Downloadable Reports & Charts
Filters by Platform, Emotion, and Date Range

### 📈 Sample Insights
🥇 Peak negative emotion spikes detected during major news events
🌍 Anger and fear often dominant in specific geo-regions
📅 Highest emotional engagement seen on weekends
🔔 Alerts triggered when sudden fear or anger levels rise


## Screenshots
### 🔔 Alert System  
![Homepage](https://github.com/abdulzuhail/real-time-sentiment-analysis-on-social-media/raw/main/Homepage.png)

### 📈 Sentiment Forecasting  
![Forecasting](https://github.com/abdulzuhail/real-time-sentiment-analysis-on-social-media/raw/main/Forecasting.png)

### 🌐 Streamlit Sentiment Dashboard  
![Streamlit Dashboard](https://github.com/abdulzuhail/real-time-sentiment-analysis-on-social-media/raw/main/Streamlit%20Dashboard.png)

### 🧨 Anomalous Posts  
![Anomalous Posts](https://github.com/abdulzuhail/real-time-sentiment-analysis-on-social-media/raw/main/Anomalous%20Post.png)

### 🎭 Emotion Distribution  
![Emotion Distribution](https://github.com/abdulzuhail/real-time-sentiment-analysis-on-social-media/raw/main/Emotion%20Distribution.png)

🎥 **[Live Demo Video](https://github.com/abdulzuhail/real-time-sentiment-analysis-on-social-media/blob/main/Live%20Demo.mp4)**
