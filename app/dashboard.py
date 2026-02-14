import streamlit as st
import pandas as pd
import plotly.express as px

# Load anomaly detection results
@st.cache_data
def load_data():
    return pd.read_csv("data/anomaly_detection_results.csv")

# Streamlit UI Config
st.set_page_config(
    page_title="Sentiment Dashboard",
    layout="wide",
    page_icon="📊"
)

# Custom CSS
st.markdown("""
    <style>
    /* Global Background */
    .stApp {
        background-color: #0e1117;
        color: #ffffff;
        font-family: 'Segoe UI', sans-serif;
    }

    /* Header Styling */
    h1, h2, h3, h4, h5 {
        color: #f1f1f1;
    }

    /* Sidebar */
    .stSidebar {
        background-color: #1c1e24;
    }

    /* Card-like section style */
    .card {
        background-color: #1e1e2f;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0 4px 8px rgba(255, 255, 255, 0.08);
        margin-bottom: 25px;
    }

    /* Button */
    .stButton>button {
        background-color: #ff6f61;
        color: white;
        padding: 0.5rem 1.5rem;
        border-radius: 8px;
        font-weight: bold;
        transition: background 0.3s;
    }

    .stButton>button:hover {
        background-color: #e25b4d;
    }

    /* Filter widgets */
    .stSelectbox, .stDateInput {
        background-color: #222;
        color: white;
    }

    /* Plot background */
    .css-1y0tads, .css-1r6slb0 {
        background-color: #1e1e2f !important;
    }
    </style>
""", unsafe_allow_html=True)

# Page Title
st.title("📊 Real-Time Sentiment Analysis Dashboard")
st.markdown("Explore real-time trends, anomalies, and insights derived from live Reddit data.")

# Load data
df = load_data()

# Date formatting
df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')

# Sidebar Filters
st.sidebar.title("🔧 Filter Settings")
min_date, max_date = df['timestamp'].min(), df['timestamp'].max()
selected_range = st.sidebar.date_input("Select Date Range", [min_date, max_date])

# Filter data
filtered_df = df[(df['timestamp'] >= pd.to_datetime(selected_range[0])) &
                 (df['timestamp'] <= pd.to_datetime(selected_range[1]))]

# Card: Sentiment Score Distribution
with st.container():
    st.markdown("### 📌 Sentiment Score Distribution")
    fig = px.histogram(filtered_df, x="sentiment_score", nbins=50,
                       title="Distribution of Sentiment Scores",
                       color_discrete_sequence=["#1f77b4"])
    fig.update_layout(template="plotly_dark", paper_bgcolor="#0e1117")
    st.plotly_chart(fig, use_container_width=True)

# Card: Sentiment Over Time
with st.container():
    st.markdown("### 📈 Sentiment Score Over Time")
    fig = px.line(filtered_df, x="timestamp", y="sentiment_score",
                  title="Sentiment Trend",
                  color_discrete_sequence=["#2ca02c"])
    fig.update_layout(template="plotly_dark", paper_bgcolor="#0e1117")
    st.plotly_chart(fig, use_container_width=True)

# Card: Sarcasm Detection
with st.container():
    st.markdown("### 🎭 Sarcasm Label Distribution")
    fig = px.histogram(filtered_df, x="sarcasm_label",
                       title="Sarcasm Distribution",
                       color_discrete_sequence=["#ff7f0e"])
    fig.update_layout(template="plotly_dark", paper_bgcolor="#0e1117")
    st.plotly_chart(fig, use_container_width=True)

# Card: Anomaly Detection
with st.container():
    st.markdown("### 🚨 Detected Anomalies in Sentiment")
    fig = px.scatter(filtered_df, x="timestamp", y="sentiment_score",
                     color="anomaly", title="Anomalous Points",
                     color_discrete_sequence=["#d62728", "#17becf"])
    fig.update_layout(template="plotly_dark", paper_bgcolor="#0e1117")
    st.plotly_chart(fig, use_container_width=True)

# Card: Data View
with st.expander("🔍 View Sample Data"):
    st.dataframe(filtered_df.head(10), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("🚀 **Auto-updated every few minutes!**" )
st.markdown("⚡Powered by Transformers + Prophet + Reddit API.")
st.markdown( "  Built with ❤️ using Streamlit and Plotly.") 