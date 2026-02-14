import React, { useEffect, useState } from "react";
import "../styles/RecentPosts.css";

const RecentPosts = () => {
    const [recentPosts, setRecentPosts] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchRecentPosts = async () => {
            try {
                const response = await fetch("http://127.0.0.1:8005/get_recent_posts");
                
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                
                const data = await response.json();
                
                if (data.error) {
                    throw new Error(data.error);
                }
                
                setRecentPosts(data.posts || []);
                
            } catch (err) {
                console.error("Error fetching recent posts:", err);
                setError(err.message);
            } finally {
                setLoading(false);
            }
        };

        fetchRecentPosts();
    }, []);

    const getEmotionIcon = (emotion) => {
        switch(emotion.toLowerCase()) {
            case 'positive': return '😊';
            case 'negative': return '😞';
            case 'neutral': return '😐';
            default: return '❓';
        }
    };

    return (
        <div className="recent-posts-card">
            <div className="posts-header">
                <h3 className="posts-title">Recent Sentiment Analysis</h3>
                <p className="posts-subtitle">Latest posts with emotional sentiment</p>
            </div>
            
            <div className="posts-content">
                {loading ? (
                    <div className="loading-state">
                        <div className="loading-spinner"></div>
                        <p>Loading recent posts...</p>
                    </div>
                ) : error ? (
                    <div className="error-state">
                        <span className="error-icon">⚠️</span>
                        <p>Failed to load posts</p>
                        <p className="error-message">{error}</p>
                    </div>
                ) : recentPosts.length === 0 ? (
                    <div className="empty-state">
                        <span className="empty-icon">📭</span>
                        <p>No recent posts available</p>
                    </div>
                ) : (
                    <ul className="posts-list">
                        {recentPosts.map((post, index) => (
                            <li key={index} className={`post-card post-${post.emotion.toLowerCase()}`}>
                                <div className="post-content">
                                    <span className="emotion-icon">
                                        {getEmotionIcon(post.emotion)}
                                    </span>
                                    <p className="post-text">
                                        {post.text.length > 120 
                                            ? `${post.text.substring(0, 120)}...` 
                                            : post.text}
                                    </p>
                                </div>
                                <div className="post-footer">
                                    <span className="post-emotion">
                                        {post.emotion}
                                    </span>
                                    <span className="post-time">
                                        {new Date(post.timestamp || Date.now()).toLocaleTimeString()}
                                    </span>
                                </div>
                            </li>
                        ))}
                    </ul>
                )}
            </div>
            
            {!loading && !error && recentPosts.length > 0 && (
                <div className="posts-footer">
                    <span className="posts-count">
                        Showing {recentPosts.length} most recent posts
                    </span>
                    <button 
                        className="refresh-button"
                        onClick={() => window.location.reload()}
                    >
                        Refresh
                    </button>
                </div>
            )}
        </div>
    );
};

export default RecentPosts;