from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["lexisnexis"]
collection = db["cases"]

print("=" * 50)

# Find cases where one of the parties is "John Smith"
# SQL equivalent: SELECT * FROM cases JOIN parties ON ... WHERE parties.name = 'John Smith'
# In MongoDB - no JOIN needed, just use dot notation to go inside the array
results = collection.find({"parties.name": "John Smith"})
print("1. Cases involving John Smith:")
for case in results:
    print(f"  {case['case_id']} — {case['title']}")

print("=" * 50)

# Find cases that have a 'judgment' document
# SQL: SELECT * FROM cases JOIN documents ON ... WHERE documents.type = 'judgment'
results = collection.find({"documents.type": "judgment"})
print("2. Cases that have a judgment document:")
for case in results:
    print(f"  {case['case_id']} — {case['title']}")

print("=" * 50)

# Find cases where John Smith is specifically the PLAINTIFF (matching multiple fields inside same object)
# SQL: WHERE parties.name = 'John Smith' AND parties.role = 'plaintiff'
results = collection.find({
    "parties": {
        "$elemMatch": {"name": "John Smith", "role": "plaintiff"}
    }
})
print("3. Cases where John Smith is the plaintiff:")
for case in results:
    print(f"  {case['case_id']} — {case['title']}")

print("=" * 50)

# SQL: SELECT case_id, title, status FROM cases (only return specific fields)
# In MongoDB - second argument to find() controls which fields to return (1 = include, 0 = exclude)
results = collection.find(
    {"status": "open"},
    {"case_id": 1, "title": 1, "status": 1, "_id": 0}
)
print("4. Open cases (only case_id, title, status):")
for case in results:
    print(f"  {case}")
