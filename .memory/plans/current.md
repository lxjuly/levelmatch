---
id: levelmatch-current-plan
type: plan
status: active
projection: task-planning
---

# LevelMatch Current Plan

## Active

### Define product scope and architecture

- id: define-product-scope
- status: active
- why: Repo is empty; before writing code, the data source, LLM extraction schema, stack, and gap analyzer definition need to be decided.
- next action: Work through the four open loops in the current checkpoint (data source, stack, extraction schema, gap definition).
- related memory:
  - goal: ship-levelmatch-mvp
  - constraint: q3-timeline
  - checkpoint: current

## Proposed

### Implement data pipeline

- id: implement-data-pipeline
- status: proposed
- why: MVP requires ingesting job postings before anything else can run.
- next action: Depends on data source decision above.
- related memory:
  - goal: ship-levelmatch-mvp

### Implement LLM extraction

- id: implement-llm-extraction
- status: proposed
- why: Raw postings need to become structured records (skills, level, tech stack, compensation) for the gap analyzer to work.
- next action: Define extraction schema first, then implement.
- related memory:
  - assumption: foundational-assumptions (LLM extraction is sufficient)

### Build dashboard and gap analyzer

- id: build-dashboard-gap-analyzer
- status: proposed
- why: August deliverable; turns extracted data into a useful product surface.
- next action: Scope after MVP ships.
- related memory:
  - goal: ship-levelmatch-mvp
  - constraint: q3-timeline

## Done

### Bootstrap project memory

- id: bootstrap-levelmatch-memory
- status: done
- why: Starting with Chronelle-compatible memory ensures decisions and context are legible across sessions.
- related memory:
  - episode: bootstrap-levelmatch-memory
  - transition: bootstrap-memory
