---
id: choose-gap-analyzer
type: transition
episode: define-product-scope
operation: create
target_type: decision
target_id: gap-analyzer-decision
---

# Choose Gap Analyzer Approach

## Rationale

The composite gap report (Option D) gives the user both an actionable score and a clear "what to fix" narrative. Per-posting fit score alone (Option C) lacks the skills diff; skills diff alone (Option A) lacks seniority context. The composite combines both at the cost of slightly more complexity in the output schema.

## Before

Gap analyzer scope undefined.

## After

Composite gap report per posting: match score, missing required/preferred skills, seniority fit, role type alignment, and a Claude-generated summary line.

## Evidence

- `.memory/alternatives/gap-analyzer.md`
- `.memory/decisions/gap-analyzer-decision.md`
