---
id: implement-skill-normalization
type: episode
status: completed
---

# Implement Skill Normalization

This Episode records fixing the skill-casing aggregation gap.

## Context

The `skill-casing-splits-aggregates` claim established that inconsistent skill
casing splits Insights aggregates and weakens gap matching. The `normalize-skills`
plan item addressed it.

## Participants

- project steward
- Claude (claude-opus-4-8)

## Inputs

- Claim: skill-casing-splits-aggregates
- Insights view (where the split was visible)

## Outputs

- `src/levelmatch/extraction/normalize.py`: Title-Case canonicalization with a
  known-acronym uppercase set and case-insensitive dedup
- Applied at ingest time in `pipeline.py`
- Backfilled the 10 existing postings
- Verified in Insights: "Machine Learning" merged from two bars into one (count 4)
- Surfaced a new settled claim: `normalization-loses-product-casing`

## Transitions

- implement-skill-normalization
- settle-normalization-casing-claim
