from flask import Blueprint, jsonify, request

user_bp = Blueprint("user", __name__)

# Пример данных для демонстрации
users = [
    {"id": 1, "username": "user1"},
    {"id": 2, "username": "user2"},
]

@user_bp.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

@user_bp.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"message": "User not found."}), 404

@user_bp.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted successfully."})
