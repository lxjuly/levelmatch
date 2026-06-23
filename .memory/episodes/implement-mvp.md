---
id: implement-mvp
type: episode
status: completed
---

# Implement LevelMatch MVP

This Episode records the implementation of the LevelMatch July MVP: data pipeline, LLM extraction, and gap analyzer.

## Context

All four scope decisions were resolved (data source, stack, extraction schema, gap analyzer definition). Implementation started from an empty repo and reached a working end-to-end pipeline in a single session.

## Participants

- project steward
- Claude (claude-sonnet-4-6)

## Inputs

- Decisions: use-jsearch-api, stack-decision, llm-extraction-schema-decision, gap-analyzer-decision
- OpenWebNinja JSearch API (api.openwebninja.com/jsearch/search-v2, X-API-Key auth)
- Claude Haiku for extraction and gap summaries
- PostgreSQL via Docker

## Outputs

- Python + FastAPI project scaffold (pyproject.toml, docker-compose, alembic)
- PostgreSQL models: JobPosting, UserProfile, GapReport
- JSearch ingestion client + dedup pipeline
- Claude Haiku extraction pipeline (12-field standard schema)
- Composite gap analyzer: match score, missing skills, seniority fit, role type match, summary
- REST API: POST /ingest, GET /jobs, POST /profiles, POST /gap/batch, POST /gap/{job_id}
- End-to-end verified: 10 AI Engineer postings ingested, extracted, gap-analyzed

## Transitions

- implement-data-pipeline
- implement-llm-extraction
- implement-gap-analyzer

## Lessons

- OpenWebNinja JSearch uses X-API-Key header (not RapidAPI headers); response nested under data.jobs
- FastAPI route ordering matters: static routes (/gap/batch) must precede parameterized (/gap/{job_id})
- PYTHONPATH=src required for alembic when using src layout
- Claude Haiku extraction quality is strong for structured job posting fields
