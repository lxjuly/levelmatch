---
id: implement-gap-analyzer
type: transition
episode: implement-mvp
operation: create
target_type: milestone
target_id: build-gap-analyzer
---

# Implement Gap Analyzer

## Rationale

Core product value: given a user's background, surface how well they match job postings and what's missing.

## Before

No gap analysis. Postings stored but not compared to candidate profiles.

## After

Composite gap analyzer (`src/levelmatch/gap/analyzer.py`) produces per-posting reports:
- match_score: % of required skills covered (fuzzy substring matching)
- missing_required / missing_preferred: skill gaps
- seniority_fit: above / match / below (mapped via rank table)
- role_type_match: whether posting role is in user's target roles
- summary: Claude Haiku one-liner

API endpoints:
- POST /profiles — create user profile (skills, level, target_roles)
- POST /gap/batch — analyze profile against N postings, sorted by match_score descending
- POST /gap/{job_id} — single posting gap report

End-to-end verified with a test profile against 5 AI Engineer postings.

## Evidence

- `src/levelmatch/gap/analyzer.py`
- `src/levelmatch/api/routes/gap.py`
- `src/levelmatch/api/routes/profiles.py`
