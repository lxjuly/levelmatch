---
id: levelmatch-current-plan
type: plan
status: active
projection: task-planning
---

# LevelMatch Current Plan

## Active

_None — dashboard shipped. Pick the next item from Proposed._

## Proposed

### Normalize skills

- id: normalize-skills
- status: proposed
- why: Extraction emits skills with inconsistent casing/wording ("Machine Learning" vs "Machine learning"), which splits aggregates in the Insights view and weakens gap matching.
- next action: Add a canonicalization pass (lowercase + alias map, or LLM-assisted) at extraction time, and/or aggregate case-insensitively.
- related memory:
  - episode: implement-dashboard
  - decision: llm-extraction-schema-decision

### Deploy to Cloudflare Pages + Railway

- id: deploy-stack
- status: proposed
- why: The dashboard and API need to be publicly reachable for the portfolio.
- next action: Deploy FastAPI + Postgres to Railway, dashboard to Cloudflare Pages, wire CORS + PUBLIC_API_BASE to production origins.
- related memory:
  - decision: hosting-decision
  - constraint: q3-timeline

### Extend market aggregate view

- id: build-market-aggregate
- status: proposed
- why: The Insights view covers skill + tech-stack frequency; a fuller view could add role_type trends and user-relative gaps (market demand vs. the active profile).
- next action: Add role_type frequency and a "your top missing skills across the market" panel.
- related memory:
  - alternatives: gap-analyzer (Option E)
  - episode: implement-dashboard

## Done

### Build dashboard

- id: build-dashboard
- status: done
- why: August deliverable; frontend surface for postings, gap reports, and market aggregates.
- related memory:
  - episode: implement-dashboard
  - transition: implement-dashboard
  - decision: frontend-sveltekit
  - decision: hosting-decision

### Plan dashboard

- id: plan-dashboard
- status: done
- related memory:
  - episode: plan-dashboard
  - decision: hosting-decision
  - decision: frontend-sveltekit

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
