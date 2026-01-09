from flask import Blueprint, request, jsonify, session
from utils.decorators import login_required
from expenses.services import add_expense

expenses_bp = Blueprint("expenses", __name__)

@expenses_bp.route("/", methods=["POST"])
@login_required
def create():
    data = request.json
    add_expense(
        session["user_id"],
        data["category_id"],
        data["amount"],
        data["date"],
        data.get("note")
    )
    return jsonify({"message": "Gasto añadido"}), 201
