# app/routes/chatbot.py

from flask import Blueprint, request, jsonify
from flask_login import login_required
from app.models import Product
from app.extensions import db

bp = Blueprint("chatbot", __name__, url_prefix="/api/chat")

@bp.route("/bot", methods=["POST"])
@login_required
def chatbot_reply():
    data = request.json
    user_message = data.get("message", "").lower()

    if not user_message.strip():
        return jsonify({"message": "Please enter a message.", "products": []}), 200

    # Search products by name, description or category
    matched_products = Product.query.filter(
        Product.name.ilike(f"%{user_message}%") |
        Product.description.ilike(f"%{user_message}%") |
        Product.category.ilike(f"%{user_message}%")
    ).all()

    if not matched_products:
        return jsonify({
            "message": "❌ No matching products found.",
            "products": []
        }), 200

    # Format products to send back
    product_list = [{
        "name": p.name,
        "description": p.description,
        "price": p.price,
        "category": p.category
    } for p in matched_products]

    return jsonify({
        "message": f"✅ Found {len(product_list)} matching product(s).",
        "products": product_list
    }), 200
