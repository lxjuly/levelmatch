---
id: deploy-to-production
type: transition
episode: deploy-to-production
operation: create
target_type: milestone
target_id: deploy-stack
---

# Deploy To Production

## Rationale

Realizes the hosting decision: the dashboard and API are now publicly reachable,
which the portfolio goal requires.

## Before

LevelMatch ran only locally.

## After

Backend live on Railway (FastAPI + Postgres, migrations applied), dashboard live on
Cloudflare Pages, CORS wired to the Pages origin, verified end-to-end.

## Evidence

- https://levelmatch.pages.dev
- https://levelmatch-api-production.up.railway.app/health
- `railway.toml`, `web/wrangler.toml`, `DEPLOY.md`
