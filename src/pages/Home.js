import React, { useEffect, useState } from "react";
import "../styles/App.css";
import { Link, useNavigate } from "react-router-dom"; // Updated

function Home() {
  const [alert, setAlert] = useState("");
  const [showAlert, setShowAlert] = useState(false);
  const navigate = useNavigate(); // Added for navigation

  useEffect(() => {
    fetch("http://localhost:8005/get_sentiment_alert")
      .then((res) => res.json())
      .then((data) => {
        if (data.alert) {
          setAlert(data.message);
          setShowAlert(true);
        }
      });
  }, []);

  const handleOkClick = () => {
    navigate("/charts#anomalies"); // Redirect to Anomalous Posts section
  };

  return (
    <div className="home-container">
      <h1>Welcome to Real-Time Sentiment Analysis</h1>
      <p>Monitor social media sentiment trends in real-time.</p>

      {showAlert && (
        <div className="alert-banner">
          {alert}
          <br />
          <button className="ok-button" onClick={handleOkClick}>
            OK
          </button>
        </div>
      )}

      <div className="button-group">
        <a
          href="http://localhost:8501/"
          target="_blank"
          rel="noopener noreferrer"
          className="dashboard-link"
        >
          Open Dashboard
        </a>
        <Link to="/charts" className="chart-link">
          View Charts
        </Link>
      </div>
    </div>
  );
}

export default Home;
