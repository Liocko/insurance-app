from flask import Blueprint, flash, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

auth_bp = Blueprint("auth", __name__)

# Хардкодированные учетные данные
hardcoded_username = "test"
hardcoded_password = generate_password_hash("test")

# Маршрут для отображения страницы логина
@auth_bp.route("/login", methods=["GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Username and password are required.")
            return redirect(url_for("auth.login"))

        if username == hardcoded_username and check_password_hash(hardcoded_password, password):
            return redirect(url_for("auth.clients_page"))
        else:
            flash("Invalid credentials.")
            return redirect(url_for("auth.login"))

    return render_template("login.html")

@auth_bp.route("/clients")
def clients_page():
    return render_template("clients.html")

