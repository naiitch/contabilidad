from flask import Blueprint, request, jsonify, session
from utils.decorators import login_required
from categories.services import create_category

categories_bp = Blueprint("categories", __name__)

@categories_bp.route("/", methods=["POST"])
@login_required
def create():
    data = request.json
    create_category(session["user_id"], data["name"], data["type"])
    return jsonify({"message": "Categoría creada"}), 201
