---
id: implement-llm-extraction
type: transition
episode: implement-mvp
operation: create
target_type: milestone
target_id: implement-llm-extraction
---

# Implement LLM Extraction

## Rationale

Raw job posting descriptions need to become structured records for gap analysis to work.

## Before

Postings stored with raw description only.

## After

Claude Haiku extraction pipeline (`src/levelmatch/extraction/claude.py`) converts raw descriptions into the 12-field standard schema: title, company, location, seniority_level, role_type, required_skills, preferred_skills, tech_stack, years_experience, salary_range, remote_type, company_stage.

Extraction is called inline in the ingestion pipeline — each posted job is extracted at ingest time.

## Evidence

- `src/levelmatch/extraction/claude.py`
- `src/levelmatch/extraction/schema.py`
