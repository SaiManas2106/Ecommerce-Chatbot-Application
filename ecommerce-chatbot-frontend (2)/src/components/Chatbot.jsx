import React, { useState, useRef, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";
import "../App.css";

// Use environment variable for backend URL (fallback to Render link)
const API_BASE_URL =
  import.meta.env.VITE_API_BASE_URL || "https://ecommerce-chatbot-application.onrender.com";

// Ensure credentials (cookies/session) are sent
axios.defaults.withCredentials = true;

const Chatbot = () => {
  const [input, setInput] = useState("");
  const [chat, setChat] = useState([]);
  const chatEndRef = useRef(null);
  const navigate = useNavigate();

  const scrollToBottom = () => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [chat]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const timestamp = new Date().toISOString();

    const userMessage = {
      role: "user",
      text: input,
      timestamp: new Date(timestamp).toLocaleTimeString(),
    };
    setChat((prev) => [...prev, userMessage]);

    try {
      await axios.post(
        `${API_BASE_URL}/api/chat/log`,
        {
          sender: "user",
          message: input,
          timestamp,
        },
        { withCredentials: true }
      );

      const res = await axios.post(
        `${API_BASE_URL}/api/chat/bot`,
        { message: input },
        { withCredentials: true }
      );

      const { message, products } = res.data;

      const productDetails = products
        .map(
          (p) =>
            `📦 ${p.name} (${p.category})\n💬 ${p.description}\n💰 Rs.${p.price}`
        )
        .join("\n\n");

      const botReply = products.length
        ? `${message}\n\n${productDetails}`
        : message;

      const botMessage = {
        role: "bot",
        text: botReply,
        timestamp: new Date().toLocaleTimeString(),
      };
      setChat((prev) => [...prev, botMessage]);

      await axios.post(
        `${API_BASE_URL}/api/chat/log`,
        {
          sender: "bot",
          message: botReply,
          timestamp: new Date().toISOString(),
        },
        { withCredentials: true }
      );
    } catch (err) {
      console.error("Chatbot error:", err);
      const errorMsg = {
        role: "bot",
        text: "❌ Error fetching product details.",
        timestamp: new Date().toLocaleTimeString(),
      };
      setChat((prev) => [...prev, errorMsg]);
    }

    setInput("");
  };

  const fetchChatHistory = async () => {
    try {
      const res = await axios.get(`${API_BASE_URL}/api/chat/logs`, {
        withCredentials: true,
      });
      if (res.data && res.data.length > 0) {
        const formatted = res.data.map((log) => ({
          role: log.sender,
          text: log.message,
          timestamp: new Date(log.timestamp).toLocaleTimeString(),
        }));
        setChat(formatted);
      } else {
        alert("No chat history found.");
      }
    } catch (err) {
      console.error("History fetch error:", err);
      alert("Error fetching chat history.");
    }
  };

  const resetConversation = () => setChat([]);

  const handleLogout = () => {
    axios
      .post(`${API_BASE_URL}/api/logout`, {}, { withCredentials: true })
      .finally(() => navigate("/login"));
  };

  return (
    <div className="app-background">
      <div className="chatbot-card">
        <h2>Electronics Assistant</h2>
        <div className="chat-window">
          {chat.map((msg, idx) => (
            <div key={idx} className={`message ${msg.role}`}>
              <span className="timestamp">[{msg.timestamp}]</span>{" "}
              <strong>{msg.role === "user" ? "You" : "Bot"}:</strong>{" "}
              <pre style={{ whiteSpace: "pre-wrap", margin: 0 }}>
                {msg.text}
              </pre>
            </div>
          ))}
          <div ref={chatEndRef} />
        </div>

        <div className="input-area">
          <input
            type="text"
            placeholder="Ask about electronics..."
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
          />
          <button onClick={sendMessage}>Send</button>
          <button className="reset-btn" onClick={resetConversation}>
            Reset
          </button>
          <button className="history-btn" onClick={fetchChatHistory}>
            View Chat History
          </button>
        </div>

        <div style={{ marginTop: "1rem", textAlign: "right" }}>
          <button className="logout-btn" onClick={handleLogout}>
            Logout
          </button>
        </div>
      </div>
    </div>
  );
};

export default Chatbot;
