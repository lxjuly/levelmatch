---
id: implement-skill-normalization
type: transition
episode: implement-skill-normalization
operation: create
target_type: milestone
target_id: normalize-skills
---

# Implement Skill Normalization

## Rationale

Resolves the consequence of the `skill-casing-splits-aggregates` claim: canonical
skill strings stop the same skill being counted twice and tighten gap matching.

## Before

Skills stored as Claude emitted them, with inconsistent casing splitting aggregates.

## After

Skills are canonicalized at ingest time and the existing rows were backfilled.
Aggregates merge correctly (verified in Insights). The underlying claim that raw
extraction is inconsistent remains true; normalization mitigates its effect.

## Evidence

- `src/levelmatch/extraction/normalize.py`
- `src/levelmatch/ingestion/pipeline.py`
