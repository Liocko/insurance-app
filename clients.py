from flask import Blueprint, flash, redirect, request, jsonify, render_template, url_for
from db import get_all_clients, add_client_to_db, delete_client_from_db

client_bp = Blueprint("client", __name__)

# Маршрут для отображения страницы клиентов
@client_bp.route("/clients", methods=["GET","POST"])
def clients_page():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")

        if not first_name or not last_name or not email or not phone:
            flash("All fields are required")
        else:
            add_client_to_db(first_name, last_name, email, phone, address)
            flash("Client added successfully")

        return redirect(url_for("client.clients_page"))
    clients = get_all_clients()
    return render_template("clients.html", clients=clients)

@client_bp.route("/client/delete<int:client_id>", methods = ["POST"])
def delete_client(client_id):
    delete_client_from_db(client_id)
    flash("Client deleted")
    return redirect(url_for("client.clients_page"))
