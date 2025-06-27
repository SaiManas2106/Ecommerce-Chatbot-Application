// src/App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";
import Login from "./components/Login";
import Register from "./components/Register";
import Chatbot from "./components/Chatbot";

const App = () => {
  return (
    <Router>
      <div className="app-background">
        <Routes>
          <Route path="/" element={<Navigate to="/login" />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/chat" element={<Chatbot />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
