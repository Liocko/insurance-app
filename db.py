import psycopg2
from init_db import get_db_connection

def get_all_clients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, first_name, last_name, email, phone, address FROM clients")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

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

def edit_client_in_db(first_name, last_name, email, phone, address, client_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE clients
        SET first_name = %s, last_name = %s, email = %s, phone = %s, address = %s
        WHERE id = %s
    """,(first_name, last_name, email, phone, address, client_id))
    conn.commit()
    cursor.close()
    conn.close()
