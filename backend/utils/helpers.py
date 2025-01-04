from bson import ObjectId
from flask import jsonify

def serialize_objectid(data):
    """
    Recursively converts ObjectId to string in dictionaries or lists.
    """
    if isinstance(data, list):
        return [serialize_objectid(item) for item in data]
    elif isinstance(data, dict):
        return {key: serialize_objectid(value) for key, value in data.items()}
    elif isinstance(data, ObjectId):
        return str(data)
    return data

def json_response(data, status=200):
    """
    Returns a Flask JSON response with serialized data.
    """
    serialized_data = serialize_objectid(data)
    return jsonify(serialized_data), status
