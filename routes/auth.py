from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

# Хардкодированные учетные данные
hardcoded_username = "test"
hardcoded_password = generate_password_hash("test")

# Маршрут для отображения страницы регистрации
@auth_bp.route("/register", methods=["GET"])
def register_page():
    return render_template("register.html")

# Маршрут для отображения страницы логина
@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("login.html")

# Обработка данных регистрации
@auth_bp.route("/register", methods=["POST"])
def register():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    return jsonify({"message": "User registered successfully."}), 201

@auth_bp.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        return jsonify({"message": "Username and password are required."}), 400

    if username == hardcoded_username and check_password_hash(hardcoded_password, password):
        return redirect(url_for("auth.clients_page"))
    else:
        return jsonify({"message": "Invalid credentials"}), 401


@auth_bp.route("/clients")
def clients_page():
    return render_template("clients.html")

