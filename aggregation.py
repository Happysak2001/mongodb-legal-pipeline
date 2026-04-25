from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["lexisnexis"]
collection = db["cases"]

print("=" * 50)

# SQL: SELECT status, COUNT(*) FROM cases GROUP BY status
pipeline = [
    {"$group": {"_id": "$status", "count": {"$sum": 1}}}
]
results = collection.aggregate(pipeline)
print("1. Case count by status:")
for r in results:
    print(f"  {r['_id']}: {r['count']}")

print("=" * 50)

# SQL: SELECT court, COUNT(*) FROM cases GROUP BY court ORDER BY COUNT(*) DESC
pipeline = [
    {"$group": {"_id": "$court", "total_cases": {"$sum": 1}}},
    {"$sort": {"total_cases": -1}}
]
results = collection.aggregate(pipeline)
print("2. Cases per court (sorted):")
for r in results:
    print(f"  {r['_id']}: {r['total_cases']}")

print("=" * 50)

# SQL: SELECT court, COUNT(*) FROM cases WHERE status = 'open' GROUP BY court
# $match is like WHERE — always put it first so MongoDB filters early
pipeline = [
    {"$match": {"status": "open"}},
    {"$group": {"_id": "$court", "open_cases": {"$sum": 1}}},
    {"$sort": {"open_cases": -1}}
]
results = collection.aggregate(pipeline)
print("3. Open cases per court:")
for r in results:
    print(f"  {r['_id']}: {r['open_cases']}")

print("=" * 50)

# $unwind — flattens an array into separate documents (one per array element)
# This is how you "join" nested data for aggregation
# SQL equivalent: think of it like unnesting a one-to-many relationship
pipeline = [
    {"$unwind": "$documents"},
    {"$group": {"_id": "$documents.type", "count": {"$sum": 1}}},
    {"$sort": {"count": -1}}
]
results = collection.aggregate(pipeline)
print("4. Document type frequency across all cases:")
for r in results:
    print(f"  {r['_id']}: {r['count']}")

print("=" * 50)

# SQL: SELECT court, COUNT(*) as total FROM cases GROUP BY court HAVING COUNT(*) > 15
pipeline = [
    {"$group": {"_id": "$court", "total": {"$sum": 1}}},
    {"$match": {"total": {"$gt": 15}}},   # $match after $group = HAVING in SQL
    {"$sort": {"total": -1}}
]
results = collection.aggregate(pipeline)
print("5. Courts with more than 15 cases (HAVING equivalent):")
for r in results:
    print(f"  {r['_id']}: {r['total']}")
