---
id: use-jsearch-api
type: decision
status: accepted
---

# Use JSearch As The Job Posting Ingestion API

LevelMatch will use JSearch (via RapidAPI) as its primary data source for job postings.

JSearch aggregates LinkedIn, Indeed, and Glassdoor in a single API call, giving multi-source market breadth without multiple integrations. The 500 free requests/month is sufficient for MVP development and iteration.

Adzuna is the designated fallback if RapidAPI dependency becomes a problem.

The US market is the initial target. Global expansion is deferred.

See [[data-ingestion-api-alternatives]] for the full set of options considered.
