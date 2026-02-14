import React, { useState, useEffect } from "react";
import { Bar } from "react-chartjs-2";
import "chart.js/auto";

const TopLocations = () => {
    const [chartData, setChartData] = useState(null);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        fetch("http://127.0.0.1:8005/get_top_locations")
            .then(response => response.json())
            .then(data => {
                setChartData({
                    labels: Object.keys(data),
                    datasets: [
                        {
                            label: "Top Locations by Emotion Count",
                            data: Object.values(data),
                            backgroundColor: "#36a2eb",
                        },
                    ],
                });
                setLoading(false);
            })
            .catch(error => {
                console.error("Error fetching top locations data:", error);
                setLoading(false);
            });
    }, []);

    return (
        <div className="chart-container">
            <h2>Top Locations by Emotion</h2>
            {loading ? <p>Loading chart...</p> : <Bar data={chartData} />}
        </div>
    );
};

export default TopLocations;
