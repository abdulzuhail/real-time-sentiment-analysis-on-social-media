import React, { useState, useEffect } from "react";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";
import L from "leaflet";
import "leaflet/dist/leaflet.css";

// Import your custom marker image
import customMarker from "./marker.png"; // Adjusted relative import

// Create custom Leaflet icon
const markerIcon = new L.Icon({
    iconUrl: customMarker,
    iconSize: [35, 45],
    iconAnchor: [17, 45],
    popupAnchor: [0, -45],
});

// Inline Styles
const styles = {
    geoContainer: {
        textAlign: "center",
        padding: "20px",
        maxWidth: "1200px",
        margin: "0 auto",
        backgroundColor: "#f9f9f9",
        borderRadius: "8px",
        boxShadow: "0 4px 8px rgba(0, 0, 0, 0.1)",
    },
    heading: {
        fontSize: "2rem",
        marginBottom: "20px",
        color: "#333",
    },
    loadingContainer: {
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        height: "300px",
    },
    loadingSpinner: {
        border: "4px solid #f3f3f3",
        borderTop: "4px solid #3498db",
        borderRadius: "50%",
        width: "50px",
        height: "50px",
        animation: "spin 2s linear infinite",
        marginBottom: "10px",
    },
    errorState: {
        color: "red",
        fontSize: "1.2rem",
        margin: "20px",
    },
    retryButton: {
        backgroundColor: "#3498db",
        color: "white",
        padding: "10px 20px",
        border: "none",
        borderRadius: "5px",
        cursor: "pointer",
    },
    retryButtonHover: {
        backgroundColor: "#2980b9",
    },
    mapContainer: {
        marginTop: "20px",
    },
    popupContent: {
        fontSize: "1rem",
    },
    popupTitle: {
        color: "#3498db",
    },
};

// Keyframes for spinner animation
const keyframes = `
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
`;

const GeoAnalysis = () => {
    const [geoData, setGeoData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetch("http://127.0.0.1:8002/get_geo_data")
            .then(response => response.json())
            .then(data => {
                if (data.error) throw new Error(data.error);
                setGeoData(data.data);
            })
            .catch(error => {
                setError(error.message);
                console.error("Error fetching data:", error);
            })
            .finally(() => setLoading(false));
    }, []);

    return (
        <div style={styles.geoContainer}>
            <h2 style={styles.heading}>Geographical Emotion Analysis</h2>
            {loading ? (
                <div style={styles.loadingContainer}>
                    <div style={styles.loadingSpinner}></div>
                    <p>Loading map...</p>
                </div>
            ) : error ? (
                <div style={styles.errorState}>
                    <p>Failed to load data: {error}</p>
                    <button
                        onClick={() => window.location.reload()}
                        style={styles.retryButton}
                        onMouseEnter={e => e.target.style.backgroundColor = styles.retryButtonHover.backgroundColor}
                        onMouseLeave={e => e.target.style.backgroundColor = styles.retryButton.backgroundColor}
                    >
                        Retry
                    </button>
                </div>
            ) : geoData.length === 0 ? (
                <p>No geographical data available.</p>
            ) : (
                <MapContainer center={[20, 0]} zoom={2} style={{ height: "500px", width: "100%" }}>
                    <TileLayer url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png" />
                    {geoData.map((item, index) => {
                        const lat = item.latitude || Math.random() * 160 - 80;
                        const lng = item.longitude || Math.random() * 360 - 180;

                        return (
                            <Marker key={index} position={[lat, lng]} icon={markerIcon}>
                                <Popup style={styles.popupContent}>
                                    <strong style={styles.popupTitle}>Location:</strong> {item.location || "Unknown"} <br />
                                    <strong style={styles.popupTitle}>Emotion:</strong> {item.emotion || "Not Available"}
                                </Popup>
                            </Marker>
                        );
                    })}
                </MapContainer>
            )}
            <style>{keyframes}</style>
        </div>
    );
};

export default GeoAnalysis;
