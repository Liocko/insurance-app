import os
import psycopg2
from dotenv import load_dotenv
from flask import Flask

load_dotenv()

CREATE_CLIENTS_TABLE = (
    "CREATE TABLE IF NOT EXISTS clients "
    "(id SERIAL PRIMARY KEY, "
    "first_name VARCHAR(100) NOT NULL, "
    "last_name VARCHAR(100) NOT NULL, "
    "email VARCHAR(100) NOT NULL, "
    "phone VARCHAR(100) NOT NULL, "
    "address TEXT, "
    "created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, "
    "updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP"
    ");"
)

CREATE_USERS_TABLE = (
    "CREATE TABLE IF NOT EXISTS users "
    "(id SERIAL PRIMARY KEY, "
    "username VARCHAR(15) UNIQUE NOT NULL, "
    "password TEXT NOT NULL"
    ");"
)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host=os.environ['POSTGRES_HOST'],
            database=os.environ['POSTGRES_DB'],
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD']
        )
        return conn
    except Exception as e:
        print("Ошибка при подключении к базе данных:", e)
        return None



def init_db(): 
    conn = get_db_connection()
    if conn is None:
        print("Error connectig db")
        return
    
    try:
        with conn:
            with conn.cursor() as cur:
                # Создаем таблицы
                cur.execute(CREATE_CLIENTS_TABLE)
                print("Таблица 'clients' успешно создана (или уже существует).")

                cur.execute(CREATE_USERS_TABLE)
                print("Таблица 'users' успешно создана (или уже существует).")
    except psycopg2.Error as e:
        print("Ошибка при инициализации базы данных:", e)
    finally:
        conn.close()

    # cur.execute("SELECT datname FROM pg_database WHERE datistemplate = false;")
    # databases = cur.fetchall()
    # if databases:
    #     print("Доступные базы данных:", databases)
    # else:
    #     print("Нет доступных баз данных.")

    # cur.execute(CREATE_CLIENTS_TABLE)
    # print("Таблица 'clients' успешно создана (или уже существует).")
    # cur.execute(CREATE_USERS_TABLE)
    # print("Таблица 'users' успешно создана (или уже существует).")

    # conn.commit()

    # cur.close()
    # conn.close()


