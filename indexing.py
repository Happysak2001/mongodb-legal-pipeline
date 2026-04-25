from pymongo import MongoClient, TEXT

client = MongoClient("mongodb://localhost:27017")
db = client["lexisnexis"]
collection = db["cases"]

print("=" * 50)

# Check what indexes exist right now (only _id index exists by default)
print("1. Existing indexes:")
for index in collection.list_indexes():
    print(f"  {index['name']} — {index['key']}")

print("=" * 50)

# See how MongoDB executes a query WITHOUT an index
# executionStats shows us how many documents MongoDB had to scan
explain = db.command("explain", {"find": "cases", "filter": {"status": "open"}}, verbosity="executionStats")
stats = explain["executionStats"]
print("2. Query WITHOUT index on 'status':")
print(f"  Documents scanned : {stats['totalDocsExamined']}")
print(f"  Documents returned: {stats['nReturned']}")
print(f"  Winning plan      : {explain['queryPlanner']['winningPlan']['stage']}")

print("=" * 50)

# SQL: CREATE INDEX idx_status ON cases(status)
collection.create_index("status")
print("3. Created index on 'status'")

# Same query now — should scan far fewer documents
explain = db.command("explain", {"find": "cases", "filter": {"status": "open"}}, verbosity="executionStats")
stats = explain["executionStats"]
print("4. Same query WITH index on 'status':")
print(f"  Documents scanned : {stats['totalDocsExamined']}")
print(f"  Documents returned: {stats['nReturned']}")
print(f"  Winning plan      : {explain['queryPlanner']['winningPlan']['stage']}")

print("=" * 50)

# Compound index — SQL: CREATE INDEX ON cases(court, status)
# Useful when you frequently filter by both fields together
collection.create_index([("court", 1), ("status", 1)])
print("5. Created compound index on 'court' + 'status'")

print("=" * 50)

# Text index — enables full text search on the summary field
# SQL equivalent: FULLTEXT INDEX — used for searching inside text content
# This is core to what LexisNexis does — searching inside legal documents
collection.create_index([("summary", TEXT)])
print("6. Created text index on 'summary'")

# Search for cases mentioning "Houston" in the summary
results = collection.find({"$text": {"$search": "Houston"}})
print("\n   Cases mentioning 'Houston' in summary:")
for case in results:
    print(f"  {case['case_id']} — {case['summary']}")

print("=" * 50)

# Final index list
print("7. All indexes now:")
for index in collection.list_indexes():
    print(f"  {index['name']} — {index['key']}")
