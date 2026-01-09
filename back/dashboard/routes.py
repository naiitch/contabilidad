from flask import Blueprint, jsonify, session
from utils.decorators import login_required
from dashboard.services import get_balance

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route("/balance")
@login_required
def balance():
    return jsonify({"balance": get_balance(session["user_id"])})
