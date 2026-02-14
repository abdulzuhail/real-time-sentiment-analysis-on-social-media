import React, { useState, useEffect } from "react";
import "../styles/Analysis.css";
import GeoAnalysis from "../components/GeoAnalysis";
import RecentPosts from "../components/RecentPosts";
import { Link } from "react-router-dom";

const Analysis = () => {
  const [insights, setInsights] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchInsights = async () => {
      try {
        const response = await fetch("http://127.0.0.1:8004/get_sentiment_insights");

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (data.error) {
          throw new Error(data.error);
        }

        setInsights(data.insights);
      } catch (err) {
        console.error("Error fetching sentiment insights:", err);
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchInsights();
  }, []);

  const renderSentimentMeter = (value) => (
    <div className="sentiment-meter">
      <div className="meter-fill" style={{ width: `${value}%` }}></div>
      <span className="meter-value">{value}%</span>
    </div>
  );

  return (
    <div className="analysis-dashboard">
      <div className="back-button-container">
        <Link to="/" className="back-button">← Back to Home</Link>
      </div>

      <div className="dashboard-header">
        <h1 className="dashboard-title">Sentiment Analysis Dashboard</h1>
        <p className="dashboard-subtitle">Real-time insights from social media data</p>
      </div>

      {/* Insights Section */}
      <div className="dashboard-card insights-card">
        <div className="card-header">
          <h2>Sentiment Overview</h2>
          <div className="card-actions">
            <button className="refresh-btn" onClick={() => window.location.reload()}>
              ↻ Refresh
            </button>
          </div>
        </div>

        {loading ? (
          <div className="loading-state">
            <div className="loading-spinner"></div>
            <p>Loading insights...</p>
          </div>
        ) : error ? (
          <div className="error-state">
            <span className="error-icon">⚠️</span>
            <p>Failed to load insights</p>
            <p className="error-detail">{error}</p>
          </div>
        ) : (
          <div className="insights-content">
            <div className="sentiment-breakdown">
              <div className="sentiment-item">
                <h4>Positive</h4>
                {renderSentimentMeter(insights.positive)}
              </div>
              <div className="sentiment-item">
                <h4>Negative</h4>
                {renderSentimentMeter(insights.negative)}
              </div>
              <div className="sentiment-item">
                <h4>Neutral</h4>
                {renderSentimentMeter(insights.neutral)}
              </div>
            </div>

            <div className="stats-grid">
              <div className="stat-item">
                <div className="stat-value">{insights.total_posts}</div>
                <div className="stat-label">Total Posts</div>
              </div>
              <div className="stat-item">
                <div className="stat-value">{Math.round(insights.positive)}%</div>
                <div className="stat-label">Positive</div>
              </div>
              <div className="stat-item">
                <div className="stat-value">{Math.round(insights.negative)}%</div>
                <div className="stat-label">Negative</div>
              </div>
              <div className="stat-item">
                <div className="stat-value">{Math.round(insights.neutral)}%</div>
                <div className="stat-label">Neutral</div>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Geo Analysis Section */}
      <div className="dashboard-card">
        <div className="card-header">
          <h2>Geographical Distribution</h2>
        </div>
        <div className="card-content">
          <GeoAnalysis />
        </div>
      </div>

      {/* Recent Posts Section */}
      <div className="dashboard-card">
        <div className="card-header">
          <h2>Recent Sentiment Posts</h2>
        </div>
        <div className="card-content">
          <RecentPosts />
        </div>
      </div>
    </div>
  );
};

export default Analysis;
