from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["lexisnexis"]
collection = db["cases"]

print("=" * 50)

# SQL: SELECT * FROM cases LIMIT 1
result = collection.find_one()
print("1. First document:")
print(result)

print("=" * 50)

# SQL: SELECT * FROM cases WHERE status = 'open'
results = collection.find({"status": "open"})
print("2. All open cases:")
for case in results:
    print(f"  {case['case_id']} — {case['title']}")

print("=" * 50)

# SQL: SELECT * FROM cases WHERE court = 'US Supreme Court' AND status = 'closed'
results = collection.find({
    "court": "US Supreme Court",
    "status": "closed"
})
print("3. Closed Supreme Court cases:")
for case in results:
    print(f"  {case['case_id']} — {case['title']}")

print("=" * 50)

# SQL: SELECT COUNT(*) FROM cases WHERE status = 'pending'
count = collection.count_documents({"status": "pending"})
print(f"4. Number of pending cases: {count}")

print("=" * 50)

# SQL: SELECT * FROM cases WHERE date_filed >= '2023-01-01'
results = collection.find({"date_filed": {"$gte": "2023-01-01"}})
print("5. Cases filed in 2023 or later:")
for case in results:
    print(f"  {case['case_id']} — {case['date_filed']}")
