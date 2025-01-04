import os

class Config:
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://mongodb:27017/updapi")
    DEBUG = True
