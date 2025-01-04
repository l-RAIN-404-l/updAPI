# Initialize Database
from db import db
from models.api_model import APIModel
from models.user_model import UserModel
APIModel.db = db
UserModel.db = db

# Backend App
from flask import Flask
from routes.api_routes import api_routes
from routes.user_routes import user_routes
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.register_blueprint(api_routes, url_prefix="/api")
app.register_blueprint(user_routes, url_prefix="/user")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
