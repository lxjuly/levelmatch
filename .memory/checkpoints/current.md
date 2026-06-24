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

Building the two-sided loop. Use case 1 (resume upload → parse → match) built locally,
pending deploy. Next: deploy it, then use case 2 (resume-upgrade-suggestions).

## Live URLs

- Dashboard: https://levelmatch.pages.dev (Cloudflare Pages)
- API: https://levelmatch-api-production.up.railway.app (Railway, FastAPI + Postgres)

## Progress

- July MVP backend complete (ingestion, extraction, gap analyzer)
- SvelteKit dashboard built under `web/` (Svelte 5 runes, Cloudflare Pages adapter)
- Four views: Jobs (list + match scores), Job detail (gap report), Profile, Insights (aggregates)
- CORS enabled on the API for the SvelteKit dev origin
- Skill normalization: canonicalization at ingest, existing rows backfilled, verified in Insights
- First use of the Chronelle Claim primitive: 3 FE claims + 1 normalization-limitation claim
- Verified end-to-end in a real browser against the local API (10 ingested postings)

## Next Action

Seed production data (ingest a couple of queries against the live API — costs JSearch
quota + Claude tokens, confirm first). Then build-market-aggregate or canonical-skill-dictionary.

## Open Loops

- Production DB is empty — live demo needs seeding
- Product-name casing degraded by Title Case (claim: normalization-loses-product-casing) — canonical-skill-dictionary proposed
- Per-deployment Pages preview URLs aren't in CORS_ORIGINS (only the stable levelmatch.pages.dev is)

## Working Context

- `src/levelmatch/` — FastAPI backend; `web/` — SvelteKit dashboard
- Backend: `PYTHONPATH=src uv run uvicorn levelmatch.main:app --reload`
- Frontend: `cd web && npm run dev` (Vite on :5173, expects API on :8000)
- `uv run alembic upgrade head` for migrations (prepend_sys_path=src); `docker compose up -d` for Postgres
- Deploy: `railway up --service levelmatch-api`; `cd web && npm run build && npx wrangler pages deploy` (see DEPLOY.md)
- Frontend API base set via `web/.env` PUBLIC_API_BASE

## Promotion Notes

Episode (implement-dashboard) and transition (implement-dashboard) written.
plan-dashboard episode marked completed. Plan updated: build-dashboard and
plan-dashboard done; normalize-skills, deploy-stack, and build-market-aggregate
proposed.
