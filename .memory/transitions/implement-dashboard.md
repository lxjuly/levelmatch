---
id: implement-dashboard
type: transition
episode: implement-dashboard
operation: create
target_type: milestone
target_id: build-dashboard
---

# Implement Dashboard

## Rationale

The August deliverable: a frontend surface for browsing postings, viewing
per-posting gap reports, and seeing aggregate market demand.

## Before

Backend-only MVP. No frontend; results only accessible via raw API calls.

## After

SvelteKit dashboard under `web/` with four views (Jobs, Job detail, Profile,
Insights), wired to the MVP API with CORS enabled. The Insights view also covers
most of the proposed market-aggregate work (skill + tech-stack frequency).

## Evidence

- `web/src/routes/+page.svelte`, `web/src/routes/jobs/[id]/+page.svelte`
- `web/src/routes/profile/+page.svelte`, `web/src/routes/insights/+page.svelte`
- `web/src/lib/api.js`, `web/src/lib/profile.svelte.js`
- `src/levelmatch/main.py` (CORS)
