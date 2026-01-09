from flask import Blueprint, request, jsonify, session
from utils.decorators import login_required
from budgets.services import create_budget, get_budgets

budgets_bp = Blueprint("budgets", __name__)

@budgets_bp.route("/", methods=["POST"])
@login_required
def create():
    data = request.json
    create_budget(
        session["user_id"],
        data.get("category_id"),
        data["amount"],
        data["period"],
        data["start_date"]
    )
    return jsonify({"message": "Presupuesto creado"}), 201


@budgets_bp.route("/", methods=["GET"])
@login_required
def list_budgets():
    return jsonify(get_budgets(session["user_id"]))
