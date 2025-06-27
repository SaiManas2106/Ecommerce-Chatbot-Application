# 🛒 Ecommerce Chatbot 

A complete full-stack **E-commerce Chatbot** application built using **React** and **Flask** that allows users to explore products, interact with an intelligent chatbot, and manage chat history — all through a clean, professional interface with secure user authentication.


---

## 🚀 Features

✅ **Conversational Chatbot Interface**
- AI-driven chatbot to interactively explore products
- Fetches real data from backend based on user intent
- Clean UI with left/right chat bubbles and scroll behavior

🔐 **User Authentication**
- Secure register and login with session tracking
- Chat history is user-specific
- Session-based API protection

🧾 **Chat History**
- Stores and retrieves conversation logs from DB
- Reset and clear functionality supported

📦 **Product Search**
- Query products by name, category, price, brand
- Includes mock inventory of over 100 items
- Supports flexible product exploration via chat

🎨 **Modern UI**
- Tailwind CSS styling
- Responsive layout and form handling
- Polished chatbot, login/register, and product display

---

## 🛠️ Tech Stack

| Layer       | Technologies & Tools                              |
|------------|----------------------------------------------------|
| Frontend   | React, Tailwind CSS, React Router, Vite            |
| Backend    | Python, Flask, Flask-SQLAlchemy, Flask-Login       |
| Database   | SQLite (easy to switch to PostgreSQL/MySQL)        |
| APIs       | RESTful API (Flask Blueprint architecture)         |
| Auth       | Flask sessions + LoginManager                      |
| Tooling    | Git, pip, npm, virtualenv, VS Code                 |

---

## 🗂️ Project Structure

```bash
chatbot-app/
├── ecommerce-chatbot-backend/
│   ├── app/
│   │   ├── models/              # User, Product, Chat models
│   │   ├── routes/              # API endpoints (auth, chatbot, etc.)
│   │   ├── extensions.py        # DB and LoginManager config
│   │   └── __init__.py          # App factory setup
│   ├── instance/
│   │   └── ecommerce.db         # Preloaded SQLite mock database
│   ├── run.py                   # Main backend entry point
│   └── requirements.txt
├── ecommerce-chatbot-frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── Chatbot.jsx
│   │   │   ├── Login.jsx
│   │   │   ├── Register.jsx
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── tailwind.config.js
│   ├── package.json
│   └── vite.config.js
└── README.md
