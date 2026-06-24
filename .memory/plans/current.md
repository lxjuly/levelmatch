---
id: levelmatch-current-plan
type: plan
status: active
projection: task-planning
---

# LevelMatch Current Plan

## Active

### Seed production data

- id: seed-production-data
- status: active
- why: The live dashboard is empty; a few ingested postings make it a real demo.
- next action: Run ingest against the production API for 1-2 queries (costs JSearch
  quota + Claude tokens — confirm with steward before spending).
- related memory:
  - episode: deploy-to-production

## Proposed

### Build the job-seeking loop (use cases 1–5)

- id: build-job-loop
- status: proposed
- why: The two-sided matching loop is the product vision; the five sequenced use
  cases extend the MVP from one-shot gap analysis to a closed candidate arc.
- next action: Use case 1 (resume-upload-matching) is built. Next is use case 2
  (resume-upgrade-suggestions). Steward also wants to explore implementation
  alternatives for the loop later (e.g. embedding-based matching vs LLM parse,
  agentic follow-through) — capture as Alternatives when each use case begins.
- related memory:
  - goal: two-sided-matching-loop
  - goal: resume-upgrade-suggestions
  - episode: implement-resume-upload-matching
  - episode: define-job-loop-use-cases

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

### Deploy to Cloudflare Pages + Railway

- id: deploy-stack
- status: done
- why: The dashboard and API are now publicly reachable for the portfolio.
- related memory:
  - episode: deploy-to-production
  - transition: deploy-to-production
  - decision: hosting-decision
  - claim: sveltekit-cloudflare-needs-nodejs-compat

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
