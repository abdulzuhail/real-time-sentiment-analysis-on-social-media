// src/App.js
import React from "react";
import { BrowserRouter as Router, Route, Routes, Link } from "react-router-dom";
import Home from "./Home";
import Analysis from "./Analysis";
import Charts from "./charts";
import Predictions from "./Predictions";
import "../styles/App.css";

function App() {
  return (
    <Router>
      <div className="app-container">
        <nav className="navbar">
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/analysis">Analysis</Link></li>
            <li><Link to="/charts">Charts</Link></li>
            <li><Link to="/predictions">Predictions</Link></li>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/analysis" element={<Analysis />} />
          <Route path="/charts" element={<Charts />} />
          <Route path="/predictions" element={<Predictions />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
