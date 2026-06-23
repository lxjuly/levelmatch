---
id: implement-dashboard
type: episode
status: completed
---

# Implement Dashboard

This Episode records building the LevelMatch SvelteKit dashboard.

## Context

With the planning decisions made (hosting, frontend framework), the dashboard
was scaffolded and built against the existing MVP API.

## Participants

- project steward
- Claude (claude-opus-4-8)

## Inputs

- Decisions: frontend-sveltekit, hosting-decision
- MVP API: /ingest, /jobs, /profiles, /gap

## Outputs

- SvelteKit 2 + Svelte 5 (runes) app under `web/`, Cloudflare Pages adapter
- API client (`web/src/lib/api.js`) and localStorage-backed active profile
- Jobs view: ingest box + posting list with per-role match scores
- Job detail: composite gap report (score, missing skills, seniority fit, summary)
- Profile page: create/manage candidate profile
- Insights page: aggregated skill demand + tech stack frequency
- Backend: CORS enabled for the SvelteKit dev origin
- Verified end-to-end against the local API (10 ingested postings)

## Transitions

- implement-dashboard

## Lessons

- This SvelteKit version configures the adapter inside `vite.config.js`, not a
  separate `svelte.config.js`; runes mode is forced by default.
- Skill aggregation surfaced a normalization gap: "Machine Learning" and
  "Machine learning" count as separate skills. Captured as a proposed plan item.
