from flask import Blueprint, flash, redirect, request, render_template, url_for
from db import get_all_clients, add_client_to_db, delete_client_from_db, add_policy_to_db, add_case_to_db, get_all_cases, delete_case_from_db, get_client_by_id
#Файл содержащий маршруты
client_bp = Blueprint("client", __name__)

@client_bp.route("/clients", methods=["GET", "POST"])
def clients_page():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        address = request.form.get("address")

        if not first_name or not last_name or not email or not phone:
            flash("All fields are required", "error")
        else:
            add_client_to_db(first_name, last_name, email, phone, address)
            flash("Client added successfully", "success")

        return redirect(url_for("client.clients_page"))

    clients = get_all_clients()
    return render_template("clients.html", clients=clients)

@client_bp.route("/client/delete<int:client_id>", methods=["POST"])
def delete_client(client_id):
    delete_client_from_db(client_id)
    flash("Client deleted", "success")
    return redirect(url_for("client.clients_page"))

@client_bp.route("/clients/<int:client_id>/add_policy", methods=["POST"])
def add_policy(client_id):
    policy_number = request.form.get("policy_number")
    policy_start_date = request.form.get("policy_start_date")
    policy_end_date = request.form.get("policy_end_date")
    
    if policy_number and policy_start_date:
        add_policy_to_db(client_id, policy_number, policy_start_date, policy_end_date)
        flash(f"Policy {policy_number} added successfully for client {client_id}", "success")
    else:
        flash("Please provide all the required details for the policy", "error")
    
    return redirect(url_for("client.clients_page"))

@client_bp.route("/client/<int:client_id>/add_case", methods=["POST"])
def add_case(client_id):
    policy_number = request.form.get("policy_number")
    case_description = request.form.get("case_description")
    case_date = request.form.get("case_date")

    if not policy_number or not case_description or not case_date:
        flash("All fields are required")
    else:
        add_case_to_db(client_id, policy_number, case_description, case_date)
        flash("Case added successfully")

    return redirect(url_for("client.cases_page", client_id=client_id))



@client_bp.route("/cases/<int:client_id>", methods=["GET", "POST"])
def cases_page(client_id):
    if request.method == "POST":
        case_description = request.form.get("case_description")
        case_date = request.form.get("case_date")

        if not case_description or not case_date:
            flash("All fields are required")
        else:
            add_case_to_db(client_id, case_description, case_date)
            flash("Insurance case added successfully")

        return redirect(url_for("client.cases_page", client_id=client_id))

    cases = get_all_cases()
    client = get_client_by_id(client_id)  
    return render_template("cases.html", cases=cases, client=client)


@client_bp.route("/case/delete/<int:case_id>", methods=["POST"])
def delete_case(case_id):
    delete_case_from_db(case_id)
    flash("Case deleted")
    return redirect(url_for("client.cases_page", client_id=request.form.get('client_id')))




