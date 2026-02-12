import os
import pymongo


mongo_uri = os.getenv("MONGO_URI", "mongodb+srv://YehudaFreiman:3UJrKTTbwPWjuI60@cluster0.gmuqvbk.mongodb.net/?appName=Cluster0")
mongo_db = os.getenv("MONGO_DB", "test")
mongo_collection = os.getenv("MONGO_COLLECTION", "exam")


client = pymongo.MongoClient(mongo_uri)
db = client.get_database(mongo_db)
collection = db[mongo_collection]
