from flask import Blueprint, request, jsonify, session
from utils.decorators import login_required
from incomes.services import add_income

incomes_bp = Blueprint("incomes", __name__)

@incomes_bp.route("/", methods=["POST"])
@login_required
def create():
    data = request.json
    add_income(
        session["user_id"],
        data["category_id"],
        data["amount"],
        data["date"],
        data.get("description")
    )
    return jsonify({"message": "Ingreso añadido"}), 201
