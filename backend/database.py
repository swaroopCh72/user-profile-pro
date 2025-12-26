
import os
from pymongo import MongoClient

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")
MONGO_HOST = os.getenv("MONGO_HOST")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")

if not all([MONGO_USERNAME, MONGO_PASSWORD, MONGO_HOST]):
    raise RuntimeError("MongoDB environment variables are not set correctly")

MONGO_URI = (
    f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}"
    f"@{MONGO_HOST}:{MONGO_PORT}/admin"
)

client = MongoClient(MONGO_URI)
db = client["login_app"]
users_collection = db["users"]
