from flask import Blueprint, request, jsonify
from app.models import db, ChatLog
from datetime import datetime
from flask_login import current_user, login_required
from app.models import Product

bp = Blueprint('chat', __name__, url_prefix='/api/chat')


@bp.route("/log", methods=["POST"])
@login_required
def log_chat():
    data = request.get_json()
    if not all(k in data for k in ("sender", "message", "timestamp")):
        return jsonify({"error": "Missing fields"}), 400

    try:
        parsed_timestamp = datetime.fromisoformat(data["timestamp"].replace("Z", "+00:00"))
    except ValueError:
        return jsonify({"error": "Invalid timestamp format"}), 400

    new_entry = ChatLog(
        sender=data["sender"],
        message=data["message"],
        timestamp=parsed_timestamp,
        user_id=current_user.id
    )
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Chat logged successfully"}), 201


@bp.route("/logs", methods=["GET"])
@login_required
def chat_history():
    logs = ChatLog.query.filter_by(user_id=current_user.id).order_by(ChatLog.timestamp).all()
    history = [
        {
            "sender": log.sender,
            "message": log.message,
            "timestamp": log.timestamp.isoformat()
        }
        for log in logs
    ]
    return jsonify(history), 200


@bp.route("/bot", methods=["POST"])
@login_required
def chatbot_response():
    data = request.get_json()
    query = data.get("message", "").lower()

    if not query:
        return jsonify({"message": "Please ask about a product.", "products": []}), 200

    # Search Product table
    results = Product.query.filter(
        (Product.name.ilike(f"%{query}%")) |
        (Product.description.ilike(f"%{query}%")) |
        (Product.category.ilike(f"%{query}%"))
    ).all()

    if results:
        product_data = [
            {
                "name": p.name,
                "description": p.description,
                "price": p.price,
                "category": p.category
            }
            for p in results
        ]
        return jsonify({
            "message": f"Here are some products related to '{query}':",
            "products": product_data
        }), 200
    else:
        return jsonify({
            "message": f"No products found for '{query}'.",
            "products": []
        }), 200


