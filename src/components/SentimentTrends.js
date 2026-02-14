import React, { useState, useEffect } from "react";
import { Line } from "react-chartjs-2";
import "chart.js/auto";

const SentimentTrends = () => {
    const [trendData, setTrendData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch("http://127.0.0.1:8003/get_sentiment_trends")
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    console.error("Error fetching data:", data.error);
                } else {
                    const timestamps = data.data.map(d => d.ds);
                    const sentimentScores = data.data.map(d => d.yhat);

                    setTrendData({
                        labels: timestamps,
                        datasets: [
                            {
                                label: "Predicted Sentiment Trend",
                                data: sentimentScores,
                                borderColor: "green",
                                fill: false
                            }
                        ]
                    });
                }
                setLoading(false);
            })
            .catch(error => {
                console.error("Error fetching data:", error);
                setLoading(false);
            });
    }, []);

    return (
        <div className="trends-container">
            <h2>Sentiment Trend Forecasting</h2>
            {loading ? <p>Loading trend data...</p> : <Line data={trendData} />}
        </div>
    );
};

export default SentimentTrends;
