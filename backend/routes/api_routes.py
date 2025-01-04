from flask import Blueprint, request, jsonify
from models.api_model import APIModel
from utils.helpers import json_response

api_routes = Blueprint("api_routes", __name__)

@api_routes.route("/search", methods=["GET"])
def search_apis():
    query = request.args.get("query", "")
    results = APIModel.search_apis(query)
    return json_response(results)

@api_routes.route("/categories", methods=["GET"])
def get_categories():
    categories = APIModel.get_all_categories()
    return jsonify(categories)
