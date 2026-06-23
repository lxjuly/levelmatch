---
id: stack-alternatives
type: alternative
status: resolved
resolved_by: stack-decision
---

# Stack Alternatives

Alternatives considered for the LevelMatch technical stack.

## Backend

### Python + FastAPI — accepted

Natural home for LLM/AI work. OpenAI and Anthropic SDKs are first-class. Async support built in. Best ecosystem fit for a data pipeline + LLM extraction backend.

### Node.js + Express/Fastify

Viable for full-stack JS consistency, but LLM ecosystem is weaker than Python. No strong reason to prefer it here.

### Next.js API routes

Works for simple APIs but awkward for a data pipeline backend.

## Database

### PostgreSQL — accepted

Structured job posting records, full-text search, scales past MVP. Solid default for relational data with known schema.

### SQLite

Zero infrastructure, good for solo dev MVP. Acceptable fallback but PostgreSQL is the better long-term choice.

### MongoDB

Flexible schema isn't needed — job postings are uniform enough that a document store adds complexity without benefit.

## Frontend

### Next.js — deferred to August

Best choice for a dashboard: most recognizable to hiring managers, strong ecosystem. Deferred because MVP scope is pipeline + LLM extraction only.

### SvelteKit

Lighter weight but less recognizable to hiring managers reviewing the portfolio.

### Defer entirely (MVP scope)

Chosen for July MVP. Pipeline and extraction ship first; dashboard follows in August.

## LLM

### Claude API — accepted

Structured output support, cost-effective at scale (Haiku for extraction, Sonnet for complex reasoning), and already in the project steward's ecosystem.

### OpenAI GPT-4o-mini

Also capable and cheap for structured extraction. Valid alternative if Claude API has issues.

### Local / Ollama

Too much setup overhead for a July MVP deadline.
