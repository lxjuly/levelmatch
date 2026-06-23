---
id: choose-stack
type: transition
episode: define-product-scope
operation: create
target_type: decision
target_id: stack-decision
---

# Choose LevelMatch Stack

## Rationale

Python + FastAPI gives the best LLM ecosystem fit for the data pipeline and extraction work. PostgreSQL is the right default for structured, schema-stable job posting data. Frontend is deferred to August to keep July MVP scope tight. Claude API is chosen for structured extraction — cost-effective and already in the steward's ecosystem.

## Before

No stack chosen.

## After

Python + FastAPI backend, PostgreSQL database, Next.js frontend deferred to August, Claude API for LLM extraction.

## Evidence

- `.memory/alternatives/stack.md`
- `.memory/decisions/stack-decision.md`
