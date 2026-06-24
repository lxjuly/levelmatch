---
id: levelmatch-current-plan
type: plan
status: active
projection: task-planning
---

# LevelMatch Current Plan

## Active

### Deploy to Cloudflare Pages + Railway

- id: deploy-stack
- status: active
- why: The dashboard and API need to be publicly reachable for the portfolio.
- next action: Repo is deploy-ready (railway.toml, configurable CORS, asyncpg URL
  rewrite, DEPLOY.md runbook). Remaining steps need account access:
  1. Railway: create project, add Postgres plugin, set ANTHROPIC_API_KEY /
     JSEARCH_API_KEY / CORS_ORIGINS, deploy, capture API URL
  2. Cloudflare Pages: root `web`, build `npm run build`, output
     `.svelte-kit/cloudflare`, set PUBLIC_API_BASE to the Railway URL
  3. Set CORS_ORIGINS to the Pages URL on Railway, redeploy backend
- related memory:
  - decision: hosting-decision
  - claim: dev-origin-needs-cors
  - claim: sveltekit-adapter-in-vite-config
  - constraint: q3-timeline

## Proposed

### Canonical skill dictionary

- id: canonical-skill-dictionary
- status: proposed
- why: Title-Case normalization fixes the case split but degrades camelCase product names (LangChain → Langchain). A curated alias map would give correct display labels.
- next action: Build an alias/canonical map for common product names and apply it after normalization.
- related memory:
  - claim: normalization-loses-product-casing
  - episode: implement-skill-normalization

### Extend market aggregate view

- id: build-market-aggregate
- status: proposed
- why: The Insights view covers skill + tech-stack frequency; a fuller view could add role_type trends and user-relative gaps (market demand vs. the active profile).
- next action: Add role_type frequency and a "your top missing skills across the market" panel.
- related memory:
  - alternatives: gap-analyzer (Option E)
  - episode: implement-dashboard

## Done

### Normalize skills

- id: normalize-skills
- status: done
- why: Inconsistent skill casing split Insights aggregates and weakened gap matching.
- related memory:
  - claim: skill-casing-splits-aggregates
  - episode: implement-skill-normalization
  - transition: implement-skill-normalization

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
