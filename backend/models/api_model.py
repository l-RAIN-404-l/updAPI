from pymongo import MongoClient
from utils.helpers import serialize_objectid

client = MongoClient("mongodb://mongodb:27017/")
db = client['updapi']

class APIModel:
    @staticmethod
    def add_api(api_data):
        db.apis.insert_one(api_data)

    @staticmethod
    def search_apis(query):
        results = list(APIModel.db.apis.find({"name": {"$regex": query, "$options": "i"}}))
        return serialize_objectid(results)

    @staticmethod
    def get_all_categories():
        return db.apis.distinct("category")
