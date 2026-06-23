---
id: hosting-decision
type: decision
status: accepted
---

# Hosting — Cloudflare Pages + Railway

| Layer | Host |
|---|---|
| Domain + DNS + SSL | Cloudflare (existing account) |
| Next.js dashboard | Cloudflare Pages (free, fast, git-push deploys) |
| FastAPI backend | Railway (~$5/month, Python-native) |
| PostgreSQL | Railway (managed, auto-injects DATABASE_URL) |

Cloudflare handles the edge and frontend. Railway handles the Python runtime and database. The split is clean — no rewriting the existing FastAPI backend, no new accounts, and the existing Cloudflare domain setup covers DNS and SSL for both services.

Cloudflare Workers considered but ruled out: Python Workers run on Pyodide (no TCP = no asyncpg/SQLAlchemy). Workers remain useful later as a thin proxy for rate limiting or auth middleware in front of Railway.

R2 deferred: only relevant if LevelMatch stores files (resumes, exports, PDFs).

See [[hosting-alternatives]] for options considered.
