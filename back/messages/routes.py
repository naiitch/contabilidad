from flask import Blueprint, jsonify
from messages.services import get_random_message

messages_bp = Blueprint("messages", __name__)

@messages_bp.route("/random")
def random_message():
    msg = get_random_message()
    if not msg:
        return jsonify({"message": "Ahorra aunque sea 1€ hoy 😉"})
    return jsonify(msg)
