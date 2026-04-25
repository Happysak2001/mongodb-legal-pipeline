import json
import random
from datetime import datetime, timedelta

courts = [
    "US District Court - Southern NY",
    "US District Court - Northern CA",
    "US District Court - Eastern TX",
    "US Court of Appeals - 2nd Circuit",
    "US Supreme Court"
]

statuses = ["open", "closed", "pending", "appealed"]

plaintiffs = ["John Smith", "Maria Garcia", "Tech Solutions Inc", "Green Energy LLC", "Robert Brown"]
defendants = ["Johnson Corp", "State of New York", "MegaBank NA", "PharmaCo Ltd", "City of Houston"]
attorneys = ["Alice Brown", "David Lee", "Sarah Johnson", "Michael Chen", "Emma Wilson"]

doc_types = ["complaint", "motion", "judgment", "appeal", "settlement"]


def random_date(start_year=2018, end_year=2024):
    start = datetime(start_year, 1, 1)
    end = datetime(end_year, 12, 31)
    delta = end - start
    return (start + timedelta(days=random.randint(0, delta.days))).strftime("%Y-%m-%d")


def generate_case(index):
    plaintiff = random.choice(plaintiffs)
    defendant = random.choice(defendants)

    num_docs = random.randint(1, 5)
    num_attorneys = random.randint(1, 3)

    return {
        "case_id": f"2024-CV-{str(index).zfill(5)}",
        "title": f"{plaintiff} vs. {defendant}",
        "court": random.choice(courts),
        "date_filed": random_date(),
        "status": random.choice(statuses),
        "parties": [
            {"name": plaintiff, "role": "plaintiff"},
            {"name": defendant, "role": "defendant"}
        ],
        "attorneys": [
            {"name": random.choice(attorneys), "represents": "plaintiff"}
            for _ in range(num_attorneys)
        ],
        "documents": [
            {"filename": f"{doc_type}.pdf", "type": doc_type, "date": random_date()}
            for doc_type in random.sample(doc_types, num_docs)
        ],
        "summary": f"Case involving {plaintiff} against {defendant} filed at {random.choice(courts)}."
    }


cases = [generate_case(i) for i in range(1, 101)]

with open("cases.json", "w") as f:
    json.dump(cases, f, indent=2)

print(f"Generated {len(cases)} cases and saved to cases.json")
