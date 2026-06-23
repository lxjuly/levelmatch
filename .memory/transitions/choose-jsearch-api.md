---
id: choose-jsearch-api
type: transition
episode: define-product-scope
operation: create
target_type: decision
target_id: use-jsearch-api
---

# Choose JSearch As Data Ingestion API

## Rationale

LevelMatch needs multi-source job posting data to produce meaningful market signals. JSearch aggregates the three largest US boards in a single integration, which is the most efficient path to breadth at MVP scale.

## Before

No data source chosen.

## After

JSearch (RapidAPI) selected as primary ingestion API. Adzuna designated as fallback. US-only scope for MVP.

## Evidence

- `.memory/alternatives/data-ingestion-api.md`
- `.memory/decisions/use-jsearch-api.md`
