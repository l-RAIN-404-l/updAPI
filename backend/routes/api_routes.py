from flask import Blueprint, request, jsonify
from bson import ObjectId
from models.api_model import APIModel
from utils.helpers import json_response
from db import db

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/search", methods=["GET"])
def search_apis():
    query = request.args.get("query", "")
    results = APIModel.search_apis(query)
    return json_response(results)

@api_routes.route("/categories", methods=["GET"])
def get_categories():
    categories = APIModel.get_all_categories()
    return json_response(categories)


@api_routes.route("/apis/<string:api_id>", methods=["GET"])
def get_api_by_id(api_id):
    try:
        # Retrieve API by ID
        api_data = db.apis.find_one({"_id": ObjectId(api_id)})

        if not api_data:
            return jsonify({"error": "API not found"}), 404

        # Serialize ObjectId to string for JSON
        api_data["_id"] = str(api_data["_id"])

        return jsonify(api_data), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
