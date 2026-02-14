import React, { useEffect, useState, useRef } from "react";
import SentimentChart from "../components/SentimentChart";
import EmotionDistribution from "../components/EmotionDistribution";
import TopLocations from "../components/TopLocations";
import AnomalousPosts from "../components/AnomalousPosts";
import { Link } from "react-router-dom";
import "../styles/Charts.css";

function Charts() {
  const [anomalyPosts, setAnomalyPosts] = useState([]);
  const anomalySectionRef = useRef(null);

  useEffect(() => {
    const fetchAnomalyPosts = async () => {
      try {
        const response = await fetch("http://localhost:8005/get_anomalous_posts");
        const data = await response.json();
        if (data.posts) {
          setAnomalyPosts(data.posts);
        }
      } catch (error) {
        console.error("Failed to fetch anomaly posts:", error);
      }
    };

    fetchAnomalyPosts();
  }, []);

  useEffect(() => {
    if (window.location.hash === "#anomalies" && anomalySectionRef.current) {
      setTimeout(() => {
        anomalySectionRef.current.scrollIntoView({ behavior: "smooth" });
      }, 200); // delay ensures DOM is ready
    }
  }, []);

  const downloadCSV = () => {
    if (!anomalyPosts.length) return;

    const headers = Object.keys(anomalyPosts[0]);
    const csvRows = [
      headers.join(","), // header row
      ...anomalyPosts.map((row) =>
        headers.map((field) => `"${(row[field] ?? "").toString().replace(/"/g, '""')}"`).join(",")
      ),
    ];

    const csvContent = csvRows.join("\n");
    const blob = new Blob([csvContent], { type: "text/csv;charset=utf-8;" });
    const url = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = url;
    link.setAttribute("download", "anomalous_posts.csv");
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  };

  return (
    <div className="charts-container">
      <div className="back-button-container">
        <Link to="/" className="back-button">← Back to Home</Link>
      </div>

      <h1>Charts and Visualizations</h1>
      <SentimentChart />
      <EmotionDistribution />
      <TopLocations />

      <div className="anomaly-section" ref={anomalySectionRef} id="anomalies">
        <h2>⚠️ Anomalous Posts</h2>
        <AnomalousPosts posts={anomalyPosts} />
        <button className="download-btn" onClick={downloadCSV}>
          ⬇️ Download Anomalies (CSV)
        </button>
      </div>
    </div>
  );
}

export default Charts;
