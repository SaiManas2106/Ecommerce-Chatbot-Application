import axios from "axios";

const instance = axios.create({
  baseURL: "https://ecommerce-chatbot-application.onrender.com/api",
  withCredentials: true, // ✅ send session cookie
});

export default instance;
