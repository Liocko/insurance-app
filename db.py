import psycopg2
from init_db import get_db_connection

# Клиенты
def get_all_clients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, last_name, email, phone, address FROM clients")
    clients = cursor.fetchall()
    cursor.close()
    conn.close()
    return clients

def add_client_to_db(first_name, last_name, email, phone, address):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO clients (first_name, last_name, email, phone, address)
        VALUES (%s, %s, %s, %s, %s)
    """, (first_name, last_name, email, phone, address))
    conn.commit()
    cursor.close()
    conn.close()

def delete_client_from_db(client_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM clients WHERE id = %s", (client_id,))
    conn.commit()
    cursor.close()
    conn.close()

# Полисы
def get_all_policies():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT policy_id, client_id, policy_number, policy_start_date, policy_end_date 
        FROM insurance_policies
    """)
    policies = cursor.fetchall()
    cursor.close()
    conn.close()
    return policies

# db.py

def add_policy_to_db(client_id, policy_number, policy_start_date, policy_end_date):
    # Логика добавления полиса в базу данных
    # Например, это может быть вставка в таблицу полисов
    try:
        # Пример вставки в базу данных
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO policies (client_id, policy_number, start_date, end_date)
            VALUES (%s, %s, %s, %s)
        """, (client_id, policy_number, policy_start_date, policy_end_date))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error adding policy to db: {e}")


# Страховые случаи
def get_all_cases():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT case_id, client_id, case_description, case_date 
        FROM insurance_cases
    """)
    cases = cursor.fetchall()
    cursor.close()
    conn.close()
    return cases

def add_case_to_db(client_id, policy_number, case_description, case_date):
    # Логика добавления случая в базу данных
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("""
            INSERT INTO insurance_cases (client_id, policy_number, case_description, case_date)
            VALUES (%s, %s, %s, %s)
        """, (client_id, policy_number, case_description, case_date))
        connection.commit()
        cursor.close()
        connection.close()
    except Exception as e:
        print(f"Error adding case to db: {e}")


def get_all_cases():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM insurance_cases")
    cases = cursor.fetchall()
    cursor.close()
    connection.close()
    return cases


def delete_case_from_db(case_id):
    connection = get_db_connection()
    cursor = connection.cursor()

    # Запрос для удаления записи о страховом случае по case_id
    cursor.execute("DELETE FROM insurance_cases WHERE case_id = %s", (case_id,))
    connection.commit()

    cursor.close()
    connection.close()


def get_client_by_id(client_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, last_name, email, phone, address FROM clients WHERE id = %s", (client_id,))
    client = cursor.fetchone()
    cursor.close()
    conn.close()
    return client

