---
id: hosting-alternatives
type: alternative
status: resolved
resolved_by: hosting-decision
---

# Hosting Alternatives

Alternatives considered for hosting the LevelMatch stack.

## Vercel + Railway

Vercel for Next.js, Railway for FastAPI + Postgres. Standard portfolio stack, strong DX. Ruled out because the project steward already uses Cloudflare — adding Vercel is redundant.

## All-in-one Railway

Frontend, backend, and Postgres all on Railway. Simpler infra but loses Cloudflare's edge network and CDN benefits.

## Vercel + Render

Render's free tier has cold starts, which kills demos. Ruled out.

## Vercel + Fly.io + Neon

Good at scale, too much config overhead for MVP. Ruled out.

## Full Cloudflare (Workers + Pages + D1)

Cloudflare Workers don't support FastAPI — Python Workers run on Pyodide (WebAssembly), which lacks TCP connections needed for asyncpg/SQLAlchemy. Would require rewriting the backend in TypeScript. Ruled out to avoid rewriting working code.

## Cloudflare Pages + Railway — accepted

Cloudflare owns the edge and frontend; Railway owns the Python runtime and database. Natural split that leverages the project steward's existing Cloudflare account.
