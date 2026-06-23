---
id: levelmatch-current-plan
type: plan
status: active
projection: task-planning
---

# LevelMatch Current Plan

## Active

### Implement data pipeline

- id: implement-data-pipeline
- status: active
- why: MVP requires ingesting job postings before anything else can run.
- next action: Scaffold Python + FastAPI project, set up PostgreSQL schema, wire up JSearch API ingestion.
- related memory:
  - goal: ship-levelmatch-mvp
  - decision: use-jsearch-api
  - decision: stack-decision

## Proposed

### Implement LLM extraction

- id: implement-llm-extraction
- status: proposed
- why: Raw postings need to become structured records (skills, level, tech stack, compensation) for the gap analyzer to work.
- next action: Implement extraction using the standard 12-field schema via Claude API.
- related memory:
  - decision: llm-extraction-schema-decision
  - decision: stack-decision

### Build gap analyzer

- id: build-gap-analyzer
- status: proposed
- why: August deliverable; composite gap report per posting powers the core product value.
- next action: Implement after LLM extraction is stable.
- related memory:
  - decision: gap-analyzer-decision
  - constraint: q3-timeline

### Build dashboard

- id: build-dashboard
- status: proposed
- why: August deliverable; market aggregate view and per-posting gap reports need a frontend surface.
- next action: Scope after gap analyzer ships. Next.js.
- related memory:
  - decision: stack-decision
  - constraint: q3-timeline

## Done

### Define product scope and architecture

- id: define-product-scope
- status: done
- why: All four scope decisions resolved before writing code.
- related memory:
  - decision: use-jsearch-api
  - decision: stack-decision
  - decision: llm-extraction-schema-decision
  - decision: gap-analyzer-decision

### Bootstrap project memory

- id: bootstrap-levelmatch-memory
- status: done
- why: Starting with Chronelle-compatible memory ensures decisions and context are legible across sessions.
- related memory:
  - episode: bootstrap-levelmatch-memory
  - transition: bootstrap-memory
