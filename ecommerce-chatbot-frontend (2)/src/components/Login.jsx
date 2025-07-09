import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

// Use environment variable or fallback to Render backend URL
const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "https://ecommerce-chatbot-application.onrender.com";

// Always send session cookies
axios.defaults.withCredentials = true;

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post(
        `${API_BASE_URL}/api/login`,
        { username, password },
        { withCredentials: true }
      );
      localStorage.setItem("token", res.data.token);
      navigate("/chat");
    } catch (err) {
      alert("Invalid credentials");
      console.error(err);
    }
  };

  return (
    <div className="auth-container">
      <h2>Login</h2>
      <form onSubmit={handleLogin} className="auth-form">
        <input
          type="text"
          placeholder="Username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
        />
        <input
          type="password"
          placeholder="Password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
        <button type="submit">Login</button>
      </form>
      <p>
        Don’t have an account? <a href="/register">Register here</a>
      </p>
    </div>
  );
};

export default Login;
