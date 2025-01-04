from flask import Blueprint, request, jsonify
from models.user_model import UserModel

user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/subscribe", methods=["POST"])
def subscribe_to_api():
    data = request.json
    user_email = data.get("email")
    api_name = data.get("api_name")
    UserModel.subscribe_to_api(user_email, api_name)
    return jsonify({"message": "Subscription successful"})

@user_routes.route("/subscriptions", methods=["GET"])
def get_subscriptions():
    user_email = request.args.get("email")
    subscriptions = UserModel.get_subscriptions(user_email)
    return jsonify(subscriptions)
