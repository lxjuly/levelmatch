---
id: choose-hosting
type: transition
episode: plan-dashboard
operation: create
target_type: decision
target_id: hosting-decision
---

# Choose Hosting Stack

## Rationale

Project steward already uses Cloudflare. Cloudflare Pages is the natural home for Next.js — free, fast, no cold starts. Railway is the right host for FastAPI + Postgres since Python Workers on Cloudflare can't run asyncpg/SQLAlchemy due to Pyodide's lack of TCP support.

## Before

No hosting decision.

## After

Cloudflare Pages for Next.js dashboard, Railway for FastAPI + Postgres. Cloudflare DNS routes the domain to both.

## Evidence

- `.memory/alternatives/hosting.md`
- `.memory/decisions/hosting-decision.md`
