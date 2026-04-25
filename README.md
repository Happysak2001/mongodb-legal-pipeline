# Legal Document Ingestion & Search Pipeline

An end-to-end data pipeline to ingest, store, query, and analyze legal documents using **Python** and **MongoDB** — designed to mirror how large-scale legal data platforms operate.

---

## Overview

Legal documents are semi-structured by nature. A court case can have a variable number of parties, attorneys, and attached documents — data that fits poorly into rigid SQL tables but maps naturally to MongoDB's document model.

This project covers the full data engineering lifecycle:

- Simulating bulk data ingestion from court systems
- Storing nested, variable-structure documents in MongoDB
- Querying nested data without JOINs
- Building aggregation pipelines for analytical reporting
- Indexing for performance and full-text search

---

## Project Structure

| File | Purpose |
|------|---------|
| `generate_data.py` | Generates 100 realistic court case records as JSON |
| `ingest.py` | ETL pipeline — loads JSON data into MongoDB |
| `queries.py` | Basic queries — filtering, counting, projections |
| `nested_queries.py` | Querying inside nested arrays without JOINs |
| `aggregation.py` | Aggregation pipelines for analytical reporting |
| `indexing.py` | Index creation, performance comparison, full-text search |

---

## Tech Stack

- **Python 3.12**
- **MongoDB** (local instance)
- **PyMongo** — Python driver for MongoDB
- **MongoDB Compass** — GUI for exploring the database

---

## Pipeline Stages

### 1. Data Modeling
Designed a document schema to store court cases with nested parties, attorneys, and documents — chosen over a relational model to handle variable-length, semi-structured data without JOIN overhead.

### 2. Data Ingestion (ETL)
Simulates receiving a bulk JSON data dump from a court system. Loads 100 court case documents into a MongoDB collection using `insert_many()`.

### 3. Querying
Queries the dataset using MongoDB's query language. Demonstrates dot notation for searching inside nested arrays and `$elemMatch` for multi-condition array matching — both without any JOINs.

### 4. Aggregation Pipeline
Multi-stage pipelines to answer analytical business questions:
- Case count by status
- Filings per court ranked by volume
- Open cases per court
- Document type frequency across all cases
- Courts exceeding a case threshold (HAVING equivalent)

### 5. Indexing & Full-Text Search
- Proved performance impact using execution stats: **COLLSCAN vs FETCH**
- Created single-field, compound, and text indexes
- Implemented full-text search on document summaries using MongoDB's `$text` operator

---

## Key Concepts Demonstrated

| SQL Concept | MongoDB Equivalent |
|-------------|-------------------|
| Table | Collection |
| Row | Document |
| JOIN | Dot notation / $elemMatch |
| WHERE | $match |
| GROUP BY | $group |
| HAVING | $match (after $group) |
| ORDER BY | $sort |
| CREATE INDEX | create_index() |
| FULLTEXT INDEX | TEXT index + $text |

---

## How to Run

**1. Install dependencies**
```bash
pip install pymongo
```

**2. Generate data**
```bash
python generate_data.py
```

**3. Ingest into MongoDB**
```bash
python ingest.py
```

**4. Run queries**
```bash
python queries.py
python nested_queries.py
```

**5. Run aggregations**
```bash
python aggregation.py
```

**6. Run indexing & search**
```bash
python indexing.py
```

> MongoDB must be running locally on `mongodb://localhost:27017`
