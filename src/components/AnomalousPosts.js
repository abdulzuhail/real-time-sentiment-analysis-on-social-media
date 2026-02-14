import React, { useEffect, useState } from "react";
import "../styles/AnomalousPosts.css";

function AnomalousPosts({ posts: incomingPosts }) {
  const [posts, setPosts] = useState([]);
  const [visibleCount, setVisibleCount] = useState(3);
  const [filter, setFilter] = useState("All");
  const [expanded, setExpanded] = useState(false);

  // Define negative emotions with associated colors
  const negativeEmotions = {
    anger: { label: "Anger", color: "#ff5252" },
    fear: { label: "Fear", color: "#ff9800" },
    disgust: { label: "Disgust", color: "#4caf50" },
    sadness: { label: "Sadness", color: "#2196f3" }
  };

  useEffect(() => {
    if (Array.isArray(incomingPosts)) {
      setPosts(incomingPosts);
    }
  }, [incomingPosts]);

  const handleLoadMore = () => {
    setVisibleCount(posts.length);
  };

  const toggleExpand = () => {
    setExpanded(!expanded);
  };

  // Extract unique negative emotions
  const uniqueEmotions = [
    "All",
    ...new Set(
      posts
        .map((p) => p.emotion)
        .filter((e) => e && negativeEmotions[e.toLowerCase()])
    ),
  ];

  // Filter posts by negative emotions
  const filteredPosts = posts
    .filter((post) => negativeEmotions[post.emotion?.toLowerCase()])
    .filter((post) => filter === "All" || post.emotion === filter);

  const visiblePosts = filteredPosts.slice(0, visibleCount);

  return (
    <div className={`anomaly-container ${expanded ? "expanded" : ""}`}>
      <div className="anomaly-header" onClick={toggleExpand}>
        <div className="title-container">
          <span className="warning-icon">⚠️</span>
          <h2>Anomalous Posts</h2>
          <span className="collapse-icon">
            {expanded ? "▼" : "►"}
          </span>
        </div>
      </div>

      {expanded && (
        <>
          {uniqueEmotions.length > 1 && (
            <div className="filter-control">
              <label htmlFor="emotion-filter" className="filter-label">
                Filter by Emotion
              </label>
              <div className="select-wrapper">
                <select
                  id="emotion-filter"
                  value={filter}
                  onChange={(e) => {
                    setFilter(e.target.value);
                    setVisibleCount(3);
                  }}
                  className="emotion-select"
                >
                  {uniqueEmotions.map((emotion, idx) => (
                    <option key={idx} value={emotion}>
                      {emotion}
                    </option>
                  ))}
                </select>
                <span className="select-arrow">▼</span>
              </div>
            </div>
          )}

          {/* Posts Table */}
          {visiblePosts.length > 0 ? (
            <div className="table-wrapper">
              <table className="anomaly-table">
                <thead>
                  <tr>
                    <th className="text-column">Text</th>
                    <th className="emotion-column">Emotion</th>
                    <th className="score-column">Score</th>
                  </tr>
                </thead>
                <tbody>
                  {visiblePosts.map((post, index) => {
                    const emotionData = negativeEmotions[post.emotion?.toLowerCase()] || 
                                      { label: post.emotion || "Unknown", color: "#9e9e9e" };
                    return (
                      <tr 
                        key={index} 
                        className={`${index % 2 === 0 ? "even-row" : "odd-row"} fade-in`}
                        style={{ animationDelay: `${index * 0.1}s` }}
                      >
                        <td className="post-text">{post.text}</td>
                        <td>
                          <span
                            className="emotion-pill"
                            style={{
                              backgroundColor: emotionData.color,
                              boxShadow: `0 0 8px ${emotionData.color}80`
                            }}
                          >
                            {emotionData.label}
                          </span>
                        </td>
                        <td className="score-value">
                          {typeof post.score === "number"
                            ? post.score.toFixed(2)
                            : post.score
                            ? Number(post.score).toFixed(2)
                            : "N/A"}
                        </td>
                      </tr>
                    );
                  })}
                </tbody>
              </table>
            </div>
          ) : (
            <div className="empty-state">
              <p>No anomalies detected at the moment.</p>
            </div>
          )}

          {/* View More */}
          {visibleCount < filteredPosts.length && (
            <div className="load-more-container">
              <button className="load-more-btn" onClick={handleLoadMore}>
                View All {filteredPosts.length} Posts
                <span className="arrow-icon">→</span>
              </button>
            </div>
          )}
        </>
      )}
    </div>
  );
}

export default AnomalousPosts;