from flask import Blueprint, jsonify, request, session
from utils.decorators import login_required
from stats.services import expenses_by_category, expenses_over_time

stats_bp = Blueprint("stats", __name__)

@stats_bp.route("/expenses/categories")
@login_required
def by_category():
    return jsonify(expenses_by_category(session["user_id"]))


@stats_bp.route("/expenses/time")
@login_required
def by_time():
    year = int(request.args.get("year"))
    month = request.args.get("month")

    return jsonify(
        expenses_over_time(
            session["user_id"],
            year,
            int(month) if month else None
        )
    )
