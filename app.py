from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.user import user_bp
from init_db import init_db
from clients import client_bp

app = Flask(__name__)
app.register_blueprint(client_bp)

# Настройка CORS
CORS(app, resources={r"/*": {"origins": "*"}})

# Инициализация базы данных
init_db()

# Регистрация блюпринтов
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(user_bp, url_prefix="/user")

@app.route('/')
def home():
    return "Welcome to the Flask app!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
