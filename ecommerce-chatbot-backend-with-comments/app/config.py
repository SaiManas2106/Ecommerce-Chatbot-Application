# Configuration class for Flask app
class Config:
    SECRET_KEY = "your-secret-key"  # Used for session management
    SQLALCHEMY_DATABASE_URI = "sqlite:///ecommerce.db"  # SQLite DB for demo
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET = "jwt-secret"  # Used to sign JWT tokens
