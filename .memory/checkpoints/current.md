---
id: levelmatch-current-checkpoint
type: checkpoint
status: active
actor: Claude
updated: 2026-06-22
episode: bootstrap-levelmatch-memory
---

# Current Checkpoint

## Focus

Bootstrap LevelMatch project memory and prepare to define MVP product scope and architecture.

## Progress

- Scaffolded `.memory/` using Chronelle ontology
- Recorded goals, assumptions, constraints, and levelmatch-is-job-analyzer decision
- Decided on JSearch (RapidAPI) as primary ingestion API; Adzuna as fallback; US-only MVP scope
- Alternatives recorded in `.memory/alternatives/data-ingestion-api.md`

## Next Action

Define the LLM extraction schema: what fields to pull from a raw job posting.

## Open Loops

- LLM extraction schema not defined (what fields to extract from a raw posting)
- Gap analyzer feature scope not defined (what does "gap" mean relative to user background?)

## Working Context

- `levelmatch/.memory/` — project memory root
- `/workspace/chronelle/ontology/` — ontology reference
- Q3 plan: MVP (pipeline + extraction) by end of July; dashboard + gap analyzer by end of August

## Promotion Notes

Bootstrap episode and transition already written. This checkpoint moves to `handed-off` once product scope is decided and implementation begins.
