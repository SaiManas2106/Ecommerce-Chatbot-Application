from flask import Flask
from flask_cors import CORS
from .extensions import db, login_manager
from .models import User
from app.routes.auth import bp as auth_bp
from app.routes.chat import bp as chat_bp
from app.routes.chatbot import bp as chatbot_bp

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "secretkey"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ecommerce.db"

    db.init_app(app)
    login_manager.init_app(app)
    CORS(app, supports_credentials=True, origins=["https://ecommerce-chatbot-application-ffajeegxt-sai-manas-projects.vercel.app/"])

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(chat_bp)
    app.register_blueprint(chatbot_bp)

    return app
