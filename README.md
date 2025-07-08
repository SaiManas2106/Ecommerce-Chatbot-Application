# 🛍️ Ecommerce Chatbot Application

## 📌 Project Overview  
This is a full-stack e-commerce chatbot system that provides intelligent, interactive product browsing and purchasing support through a conversational interface. It allows users to chat with a smart assistant to explore product options, filter based on preferences, and proceed through a simulated purchase flow. Admins can manage inventory through a mock backend, and users must log in to access their chat history and personalize their experience.

## 🚀 Features  
- ✨ Modern, professional frontend with TailwindCSS and React  
- 💬 Conversational chatbot UI for product discovery and FAQs  
- 🔐 Secure user authentication (register/login/logout)  
- 💾 User-specific chat history with automatic logging  
- 📂 Frontend-backend integration using RESTful APIs  
- 🧠 Server-side chatbot logic using NLP heuristics  
- 📊 Admin-accessible product database (mocked with SQLite)  
- 🔁 Reset chat, clear history, and session-based message storage  
- 🌐 Responsive design for all screen sizes  
- 🔍 Product suggestions with icon-rich formatting  

## 🛠️ Tech Stack  

### Frontend:  
- React (with Vite)  
- Tailwind CSS  
- React Router  
- Axios  
- LocalStorage (for session)  

### Backend:  
- Python Flask  
- Flask-Login (authentication)  
- Flask-SQLAlchemy  
- SQLite (mock database)  
- Flask-Migrate  
- CORS  
- RESTful APIs  

## 📁 Project Structure  
ecommerce-chatbot/  
├── ecommerce-chatbot-backend/  
│   ├── app/  
│   │   ├── routes/  
│   │   ├── models/  
│   │   ├── templates/  
│   │   ├── static/  
│   │   └── init.py  
│   ├── instance/  
│   │   └── ecommerce.db  
│   ├── run.py  
│   └── requirements.txt  
│  
├── ecommerce-chatbot-frontend/  
│   ├── src/  
│   │   ├── components/  
│   │   │   ├── Chatbot.jsx  
│   │   │   ├── Login.jsx  
│   │   │   ├── Register.jsx  
│   │   │   ├── ProtectedRoute.jsx  
│   │   │   └── ChatMessage.jsx  
│   │   ├── App.jsx  
│   │   ├── index.js  
│   │   └── main.jsx  
│   ├── public/  
│   ├── tailwind.config.js  
│   ├── postcss.config.js  
│   ├── vite.config.js  
│   ├── package.json  
│   └── README.md  

## 🔧 Setup Instructions  

### Backend:  
1. Navigate to backend folder:  
cd ecommerce-chatbot-backend  

2. Create and activate virtual environment:  
python -m venv .venv  
.venv\Scripts\activate  

3. Install dependencies:  
pip install -r requirements.txt  

4. Run database migrations:  
flask db init  
flask db migrate  
flask db upgrade  

5. Run the server:  
python run.py  

### Frontend:  
1. Navigate to frontend folder:  
cd ecommerce-chatbot-frontend  

2. Install dependencies:  
npm install  

3. Run the frontend:  
npm run dev  

## 🧪 Sample Queries  
- “Show me smartphones under 30,000”  
- “I’m looking for headphones”  
- “What are the latest laptops?”  
- “Do you have any offers?”  

## 🔐 Authentication  
- New users can register using their email and password  
- Existing users can log in to access personalized chat history  
- Session persists across reloads  
- Logout clears session  

## 🗃️ API Endpoints  

### User:  
- POST /register – Register new user  
- POST /login – Authenticate user  
- GET /logout – Logout user  

### Chat:  
- POST /api/chatbot – Send user message and receive chatbot response  
- GET /api/chat/history – Fetch previous chat messages  
- DELETE /api/chat/clear – Clear user chat history  

## 🎯 Architecture Diagram  
[User Interface - React]  
  |  
  v  
[Frontend Axios Requests]  
  |  
  v  
[Flask REST API]  
  |  
+--> [Auth Routes] ----> [User DB]  
|  
+--> [Chatbot Logic] --> [Product DB]  

## 💡 Challenges Faced  
- Managing chat context across sessions  
- Securing API routes using session-based auth  
- Handling race conditions when resetting chat  
- Styling messages dynamically with tailwind and scroll behavior  
- Implementing role-based access cleanly on both frontend/backend  
- Ensuring RESTful architecture while maintaining UI responsiveness  

## 📈 Results and Learnings  
- ✅ Seamless chat interface with login support  
- ✅ Modular, production-ready code for both frontend/backend  
- ✅ Understood real-world auth session handling  
- ✅ Applied REST API and SPA integration using modern tools  

## 📘 Future Improvements  
- Integrate with real payment and cart system  
- Add product image support with rich cards  
- Support voice-to-text for chatbot input  
- Use real NLP engine like Dialogflow or Rasa  
- Multi-language support  
- Admin dashboard to manage inventory  

## 📄 License  
This project is for academic and demonstration purposes only.  

## ✍️ Author  
**Masetty Sai Manas**  
[GitHub](https://github.com/SaiManas2106)
