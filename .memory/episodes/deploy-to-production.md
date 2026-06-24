---
id: deploy-to-production
type: episode
status: completed
---

# Deploy To Production

This Episode records deploying LevelMatch live: backend to Railway, dashboard to
Cloudflare Pages.

## Context

The repo was made deploy-ready (configurable CORS, asyncpg URL rewrite, railway.toml,
DEPLOY.md). This Episode executes the deploy via the Railway and Wrangler CLIs.

## Participants

- project steward (Railway + Cloudflare auth)
- Claude (claude-opus-4-8) (drove the CLIs)

## Inputs

- Decision: hosting-decision (Cloudflare Pages + Railway)
- railway.toml, web/wrangler.toml, DEPLOY.md

## Outputs

- Backend live: https://levelmatch-api-production.up.railway.app (FastAPI + Postgres,
  migrations applied via preDeployCommand, healthcheck /health)
- Dashboard live: https://levelmatch.pages.dev (SvelteKit, nodejs_compat enabled)
- CORS_ORIGINS on Railway set to the Pages origin
- End-to-end verified live: dashboard fetch → API → Postgres returns []
- Settled claim: sveltekit-cloudflare-needs-nodejs-compat

## Transitions

- deploy-to-production
- settle-nodejs-compat-claim

## Lessons

- Railway's `railway add` CLI prompts even with flags in a non-TTY; it created a
  duplicate Postgres that had to be deleted along with its detached volume.
- Railway hands out `postgresql://`; the asyncpg URL rewrite in config.py was
  necessary for the async engine to connect.
- Secrets were set via `railway variable set --stdin` piped from local .env so the
  values never appeared in any command.
