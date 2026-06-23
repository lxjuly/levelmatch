---
id: implement-data-pipeline
type: transition
episode: implement-mvp
operation: create
target_type: milestone
target_id: implement-data-pipeline
---

# Implement Data Pipeline

## Rationale

First MVP milestone. Job postings need to be ingested and stored before extraction or gap analysis can run.

## Before

No data pipeline. Empty repo.

## After

JSearch client (`src/levelmatch/ingestion/jsearch.py`) fetches from OpenWebNinja API. Pipeline (`ingestion/pipeline.py`) deduplicates by external_id and stores raw postings. PostgreSQL schema via async SQLAlchemy + Alembic. Docker Compose for local Postgres.

API endpoint: POST /ingest — accepts query + num_pages, returns {created, skipped, total_fetched}.

## Evidence

- `src/levelmatch/ingestion/jsearch.py`
- `src/levelmatch/ingestion/pipeline.py`
- `src/levelmatch/db/models.py`
- `docker-compose.yml`, `alembic/`
