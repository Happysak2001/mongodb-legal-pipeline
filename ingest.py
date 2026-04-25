import json
from pymongo import MongoClient

# Connect to local MongoDB
client = MongoClient("mongodb://localhost:27017")

# This is our database - like a schema in SQL
db = client["lexisnexis"]

# This is our collection - like a table in SQL
collection = db["cases"]

# Load the JSON file (simulating a bulk data dump from a court system)
with open("cases.json", "r") as f:
    cases = json.load(f)

# Insert all 100 cases into MongoDB in one shot
result = collection.insert_many(cases)

print(f"Inserted {len(result.inserted_ids)} cases into MongoDB")
