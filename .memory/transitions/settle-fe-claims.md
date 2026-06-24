---
id: settle-fe-claims
type: transition
episode: record-fe-claims
operation: create
target_type: claim
target_ids:
  - skill-casing-splits-aggregates
  - sveltekit-adapter-in-vite-config
  - dev-origin-needs-cors
---

# Settle The Frontend Claims

## Rationale

Three truth-apt findings from the dashboard build are recorded as settled Claims in
one multi-target Transition. They share a single origin (the dashboard work) and
recording activity, consistent with treating a Transition as a change to a
combination of primitives.

## Before

The findings existed only as Episode prose and commit messages from
`implement-dashboard`.

## After

Three settled Claims exist with identity and links: skill-casing aggregation gap,
SvelteKit adapter config location, and the dev-origin CORS requirement.

## Evidence

- `.memory/claims/skill-casing-splits-aggregates.md`
- `.memory/claims/sveltekit-adapter-in-vite-config.md`
- `.memory/claims/dev-origin-needs-cors.md`
