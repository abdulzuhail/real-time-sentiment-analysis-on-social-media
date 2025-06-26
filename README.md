# 💬 Real-Time Sentiment Analysis Using Social Media

A full-stack, real-time sentiment and emotion analysis system that collects, analyzes, and visualizes social media data—primarily from Reddit—to uncover public opinion, emotional trends, and anomalies. This project uses cutting-edge **transformer models (BERT, RoBERTa)** along with **FastAPI**, **Streamlit**, and **Power BI** to deliver real-time insights for businesses, researchers, and analysts.

---

## 📌 Project Objective

The goal of this project is to monitor social media conversations in real-time and:
- Detect **sentiment** (positive, negative, neutral)
- Recognize **emotions** (joy, anger, fear, sadness, etc.)
- Identify **anomalies or emotional spikes**
- Forecast sentiment trends
- Visualize all results in an interactive dashboard

---

## 🧠 Key Features

- 🔁 **Live Reddit Streaming**  
  Continuously fetches posts using Reddit’s API filtered by geography and keywords.

- 🧹 **NLP Preprocessing Pipeline**  
  Includes tokenization, translation (if needed), stopword removal, and text normalization.

- 💬 **Sentiment & Emotion Detection**  
  Uses fine-tuned **BERT** and **RoBERTa** models to classify text into sentiment and emotion categories.

- 🚨 **Anomaly Detection**  
  Detects emotional surges using statistical and ML-based methods.

- 📉 **Forecasting**  
  Predicts future sentiment trends using **ARIMA/LSTM**.

- 🌍 **Geo-Based Analysis**  
  Maps sentiment/emotion trends across locations.

- 📊 **Interactive Dashboards**  
  Built using **Streamlit**, **Power BI**, and **React** for real-time visualization.

- 📤 **Automated Reporting**  
  Scheduled scripts generate sentiment reports every 10 minutes.

---

## 🧱 Tech Stack

| Component        | Tool/Tech Used                         |
|------------------|----------------------------------------|
| Backend          | FastAPI, Python                        |
| NLP Models       | BERT, RoBERTa (via Hugging Face)       |
| Frontend         | Streamlit, React.js                    |
| Dashboard        | Power BI                               |
| Data Collection  | Reddit API (PRAW / Pushshift)          |
| Forecasting      | ARIMA, LSTM                            |
| Scheduler        | Cron / APScheduler                     |
| Visualization    | Plotly, Altair, Power BI               |

---

## 🗂️ Project Structure

├── api/
│ ├── sentiment_api.py
│ ├── emotion_api.py
│ └── geo_api.py
├── app/
│ └── dashboard.py
├── frontend/
│ ├── components/
│ ├── pages/
│ └── styles/
├── data/
│ ├── emotion_analysis_results.csv
│ ├── sentiment_trends.csv
│ └── ...
├── scripts/
│ ├── data_collection.py
│ ├── sentiment_analysis.py
│ ├── emotion_detection.py
│ ├── anomaly_detection.py
│ └── sentiment_forecasting.py
├── requirements.txt
└── README.md

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
git clone https://github.com/abdulzuhail/Real-Time-Sentiment-Analysis.git
cd Real-Time-Sentiment-Analysis
### 2️⃣ Create Virtual Environment
python -m venv sentiment_env
source sentiment_env/bin/activate  # On Windows: sentiment_env\Scripts\activate
pip install -r requirements.txt
### 3️⃣ Run Streamlit App
cd app
streamlit run dashboard.py
### 4️⃣ Run Data Collection & Analysis Scripts
You can schedule these using cron or APScheduler
python scripts/data_collection.py
python scripts/sentiment_analysis.py
python scripts/emotion_detection.py
python scripts/anomaly_detection.py
python scripts/sentiment_forecasting.py

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

### 🚀 Future Enhancements
Add Twitter and YouTube integration
Deploy mobile-friendly dashboard
Real-time notifications via email/Slack
Support multilingual sentiment detection

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


