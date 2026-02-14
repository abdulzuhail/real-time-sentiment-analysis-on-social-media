import React, { useState, useEffect } from "react";
import { Line } from "react-chartjs-2";
import "chart.js/auto";

const SentimentChart = () => {
    const [chartData, setChartData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const fetchData = () => {
            fetch("http://127.0.0.1:8001/get_sentiment_data")
                .then(response => response.json())
                .then(data => {
                    if (data.error) {
                        console.error("Error fetching data:", data.error);
                        setLoading(false);
                    } else {
                        const timestamps = data.data.map(d => new Date(d.timestamp * 1000).toLocaleTimeString());
                        const sentimentScores = data.data.map(d => d.sentiment === "POSITIVE" ? 1 : d.sentiment === "NEGATIVE" ? -1 : 0);

                        setChartData({
                            labels: timestamps,
                            datasets: [
                                {
                                    label: "Sentiment Score",
                                    data: sentimentScores,
                                    borderColor: "blue",
                                    fill: false
                                }
                            ]
                        });
                        setLoading(false);
                    }
                })
                .catch(error => {
                    console.error("Error fetching data:", error);
                    setLoading(false);
                });
        };

        fetchData();
        const interval = setInterval(fetchData, 5000); // Auto-refresh every 5 seconds
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="chart-container">
            <h2>Sentiment Trends</h2>
            {loading ? <p>Loading chart...</p> : <Line data={chartData} />}
        </div>
    );
};

export default SentimentChart;
