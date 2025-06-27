# Product API route for searching products
from flask import Blueprint, request, jsonify
from app.models import Product

bp = Blueprint("products", __name__, url_prefix="/api")

@bp.route("/products", methods=["GET"])
def get_products():
    # Search for products by name
    query = request.args.get("query", "")
    products = Product.query.filter(Product.name.ilike(f"%{query}%")).all()
    result = [{
        "id": p.id,
        "name": p.name,
        "description": p.description,
        "price": p.price,
        "category": p.category
    } for p in products]
    return jsonify(result)
