from flask import Blueprint, request, jsonify, session
from auth.services import register_user, login_user

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.json
    register_user(data["username"], data["email"], data["password"])
    return jsonify({"message": "Usuario creado"}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    user = login_user(data["email"], data["password"])

    if not user:
        return jsonify({"error": "Credenciales inválidas"}), 401

    session["user_id"] = user["id"]
    return jsonify({"message": "Login correcto"})
