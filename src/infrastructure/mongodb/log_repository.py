from extensions import mongo_client
from datetime import datetime

# Connect to the MongoDB database
mongo_db = mongo_client["auth_logs"]

def log_attempt(username, success):
    """
    Logs a login attempt to MongoDB with timestamp and success status.
    """
    mongo_db.login_attempts.insert_one({
        "username": username,
        "success": success,
        "timestamp": datetime.utcnow()
    })