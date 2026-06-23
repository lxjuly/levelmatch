---
id: levelmatch-current-plan
type: plan
status: active
projection: task-planning
---

# LevelMatch Current Plan

## Active

### Build dashboard

- id: build-dashboard
- status: active
- why: August deliverable; market aggregate view and per-posting gap reports need a frontend surface.
- next action: Scaffold Next.js app, design the main views (job list + gap report per posting, aggregate skills chart).
- related memory:
  - decision: stack-decision
  - constraint: q3-timeline

## Proposed

### Build market aggregate view

- id: build-market-aggregate
- status: proposed
- why: Surface what the market is asking for vs. what the user has across all ingested postings.
- next action: Aggregate required_skills + role_type frequency queries over job_postings table. Feed into dashboard.
- related memory:
  - alternatives: gap-analyzer (Option E deferred to August)
  - constraint: q3-timeline

## Done

### Implement gap analyzer

- id: build-gap-analyzer
- status: done
- related memory:
  - episode: implement-mvp
  - transition: implement-gap-analyzer
  - decision: gap-analyzer-decision

### Implement LLM extraction

- id: implement-llm-extraction
- status: done
- related memory:
  - episode: implement-mvp
  - transition: implement-llm-extraction
  - decision: llm-extraction-schema-decision

### Implement data pipeline

- id: implement-data-pipeline
- status: done
- related memory:
  - episode: implement-mvp
  - transition: implement-data-pipeline
  - decision: use-jsearch-api

### Define product scope and architecture

- id: define-product-scope
- status: done
- related memory:
  - decision: use-jsearch-api
  - decision: stack-decision
  - decision: llm-extraction-schema-decision
  - decision: gap-analyzer-decision

### Bootstrap project memory

- id: bootstrap-levelmatch-memory
- status: done
- related memory:
  - episode: bootstrap-levelmatch-memory
  - transition: bootstrap-memory
