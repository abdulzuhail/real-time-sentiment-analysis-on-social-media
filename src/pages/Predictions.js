// src/pages/Predictions.js
import React from "react";
import SentimentTrends from "../components/SentimentTrends";
import { Link } from "react-router-dom";
import "../styles/Predictions.css";

function Predictions() {
  return (
    <div className="predictions-container">
      <div className="back-button-container">
        <Link to="/" className="back-button">← Back to Home</Link>
      </div>

      <h2>Predictive Sentiment Insights</h2>
      <p>Future trends and sentiment peak predictions.</p>
      <SentimentTrends />
    </div>
  );
}

export default Predictions;
