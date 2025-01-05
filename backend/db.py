from pymongo import MongoClient
from config import Config

# Initialize MongoClient directly with the URI from Config
client = MongoClient(Config.MONGO_URI, tls=True, tlsAllowInvalidCertificates=False)

# Access the database
db = client.get_database('updapi')

print("Database connection successful!")
