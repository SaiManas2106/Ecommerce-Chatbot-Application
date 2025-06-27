# app/routes/auth.py

from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user,logout_user
from app.models import User
from app.extensions import db

bp = Blueprint("auth", __name__, url_prefix="/api")


@bp.route("/register", methods=["POST"])
def register():
    data = request.json
    hashed_pw = generate_password_hash(data["password"])
    user = User(username=data["username"], password_hash=hashed_pw)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Registered successfully"}), 201



@bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(username=data["username"]).first()
    if user and check_password_hash(user.password_hash, data["password"]):
        login_user(user)  # flask_login
        return jsonify({"message": "Login successful"}), 200
    return jsonify({"error": "Invalid credentials"}), 401

 

@bp.route("/logout", methods=["POST"])
def logout():
    logout_user()
    return jsonify({"message": "Logged out successfully"}), 200
