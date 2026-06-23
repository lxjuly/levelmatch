---
id: plan-dashboard
type: episode
status: active
---

# Plan Dashboard (August Scope)

This Episode records planning decisions for the LevelMatch dashboard.

## Context

With the July MVP complete (ingestion, extraction, gap analyzer), the August
scope is a dashboard. Planning began with hosting, then the frontend framework.

## Participants

- project steward
- Claude (claude-opus-4-8)

## Inputs

- MVP backend (FastAPI + PostgreSQL on the way to Railway)
- Project steward's existing Cloudflare usage
- Project steward's stated dislike of React/Next.js complexity

## Outputs

- Hosting decision: Cloudflare Pages + Railway
- Frontend decision: SvelteKit (refines the Next.js choice in stack-decision)

## Transitions

- choose-hosting
- choose-sveltekit
