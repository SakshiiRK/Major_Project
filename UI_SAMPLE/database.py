from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb+srv://Sakshi12:admin123@finaldestination.xgrf41r.mongodb.net/?appName=FinalDestination")
db = client["lesson_app"]
users = db["users"]

# Create user
def create_user(name, email, password):
    if users.find_one({"email": email}):
        return False
    users.insert_one({
        "name": name,
        "email": email,
        "password": password
    })
    return True

# Login user
def login_user(email, password):
    return users.find_one({"email": email, "password": password})