---
id: levelmatch-current-checkpoint
type: checkpoint
status: handed-off
actor: Claude
updated: 2026-06-22
episode: implement-dashboard
---

# Current Checkpoint

## Focus

Dashboard shipped and skills normalized. Next: deploy or extended aggregates.

## Progress

- July MVP backend complete (ingestion, extraction, gap analyzer)
- SvelteKit dashboard built under `web/` (Svelte 5 runes, Cloudflare Pages adapter)
- Four views: Jobs (list + match scores), Job detail (gap report), Profile, Insights (aggregates)
- CORS enabled on the API for the SvelteKit dev origin
- Skill normalization: canonicalization at ingest, existing rows backfilled, verified in Insights
- First use of the Chronelle Claim primitive: 3 FE claims + 1 normalization-limitation claim
- Verified end-to-end in a real browser against the local API (10 ingested postings)

## Next Action

Pick from the plan's Proposed items: deploy-stack (Cloudflare Pages + Railway),
build-market-aggregate (role trends + user-relative gaps), or canonical-skill-dictionary
(curated product-name labels).

## Open Loops

- Product-name casing degraded by Title Case (claim: normalization-loses-product-casing) — canonical-skill-dictionary proposed
- Not yet deployed (Cloudflare Pages + Railway)
- PYTHONPATH=src workaround for alembic — could be cleaned up with a proper alembic config

## Working Context

- `src/levelmatch/` — FastAPI backend; `web/` — SvelteKit dashboard
- Backend: `PYTHONPATH=src uv run uvicorn levelmatch.main:app --reload`
- Frontend: `cd web && npm run dev` (Vite on :5173, expects API on :8000)
- `PYTHONPATH=src uv run alembic upgrade head` for migrations; `docker compose up -d` for Postgres
- Frontend API base set via `web/.env` PUBLIC_API_BASE

## Promotion Notes

Episode (implement-dashboard) and transition (implement-dashboard) written.
plan-dashboard episode marked completed. Plan updated: build-dashboard and
plan-dashboard done; normalize-skills, deploy-stack, and build-market-aggregate
proposed.
