from flask import Blueprint, jsonify, request, session
from utils.decorators import login_required
from users.services import (
    get_user_profile,
    update_user_profile,
    delete_user
)

users_bp = Blueprint("users", __name__)

@users_bp.route("/me", methods=["GET"])
@login_required
def profile():
    return jsonify(get_user_profile(session["user_id"]))


@users_bp.route("/me", methods=["PUT"])
@login_required
def update_profile():
    data = request.json
    update_user_profile(
        session["user_id"],
        data["username"],
        data["email"]
    )
    return jsonify({"message": "Perfil actualizado"})


@users_bp.route("/me", methods=["DELETE"])
@login_required
def remove_account():
    delete_user(session["user_id"])
    session.clear()
    return jsonify({"message": "Cuenta eliminada"})
