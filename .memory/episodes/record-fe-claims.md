---
id: record-fe-claims
type: episode
status: completed
---

# Record Frontend Claims

This Episode records truth-apt findings from the dashboard build as first-class
Claims, now that the Chronelle ontology has a Claim primitive.

## Context

When the dashboard was built (`implement-dashboard`), several truth-apt findings
were captured only as Episode prose and commit messages because Claim did not yet
exist. With Claim added to the ontology, those findings are promoted to first-class
Claims so they have identity, can be linked, and can be reopened if they change.

## Participants

- project steward
- Claude (claude-opus-4-8)

## Inputs

- `implement-dashboard` episode (where the findings were discovered)
- The Claim primitive newly added to the Chronelle ontology

## Outputs

- Settled Claims: `skill-casing-splits-aggregates`,
  `sveltekit-adapter-in-vite-config`, `dev-origin-needs-cors`

## Transitions

- settle-fe-claims
