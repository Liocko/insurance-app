from flask import Blueprint, request, jsonify, render_template
from db import get_all_clients, add_client_to_db, delete_client_from_db, edit_client_in_db

client_bp = Blueprint("client", __name__)

# Маршрут для отображения страницы клиентов
@client_bp.route("/clients", methods=["GET"])
def clients_page():
    return render_template("clients.html")

# Маршрут для получения списка клиентов (возвращает JSON)
@client_bp.route("/clients/list", methods=["GET"])
def get_clients():
    clients = get_all_clients()
    result = [
        {
            "id": row[0],
            "first_name": row[1],
            "last_name": row[2],
            "email": row[3],
            "phone": row[4],
            "address": row[5]
        }
        for row in clients
    ]
    return jsonify(result)

# Маршрут для добавления нового клиента
@client_bp.route("/client/add", methods=["POST"])
def add_client():
    data = request.get_json()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    phone = data.get("phone")
    address = data.get("address")

    if not first_name or not last_name or not email or not phone:
        return jsonify({"message": "All fields are required"}), 400

    add_client_to_db(first_name, last_name, email, phone, address)
    return jsonify({"message": "Client added successfully"}), 201

@client_bp.route("/client/delete<int:client_id>", methods = ["DELETE"])
def delete_client(client_id):
    delete_client_from_db(client_id)
    return jsonify({"message: " f"Client with ID {client_id} deleted succecsfully"}), 200

@client_bp.route("/client/edit/<int:client_id>", methods=["PUT"])
def edit_client(client_id):
    data = request.get_json()
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    email = data.get("email")
    phone = data.get("phone")
    address = data.get("address")

    if not first_name or not last_name or not email or not phone: 
        return jsonify({"message": "All fields are required"}), 400
    
    edit_client_in_db(client_id, first_name, last_name, email, phone, address)
    return jsonify({"message": f"Client with ID {client_id} updated succesfully"}), 200