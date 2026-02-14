import React, { useState, useEffect } from "react";
import { Bar } from "react-chartjs-2";
import "chart.js/auto";

const EmotionDistribution = () => {
    const [chartData, setChartData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch("http://127.0.0.1:8005/get_emotion_distribution")
            .then(response => response.json())
            .then(data => {
                setChartData({
                    labels: Object.keys(data),
                    datasets: [
                        {
                            label: "Emotion Distribution",
                            data: Object.values(data),
                            backgroundColor: ["#ff6384", "#36a2eb", "#ffce56", "#4bc0c0", "#9966ff", "#ff9f40"],
                        },
                    ],
                });
                setLoading(false);
            })
            .catch(error => {
                console.error("Error fetching emotion distribution data:", error);
                setLoading(false);
            });
    }, []);

    return (
        <div className="chart-container">
            <h2>Emotion Distribution</h2>
            {loading ? <p>Loading chart...</p> : <Bar data={chartData} />}
        </div>
    );
};

export default EmotionDistribution;
