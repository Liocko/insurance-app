import os
from flask import Flask
from routes.auth import auth_bp
from init_db import init_db
from clients import client_bp

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')
app.register_blueprint(client_bp)




init_db()


app.register_blueprint(client_bp, url_prefix="/auth", name="clinet_auth")

@app.route('/')
def home():
    return "Welcome to the Flask app!"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5001)
