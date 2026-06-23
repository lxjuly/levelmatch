---
id: choose-extraction-schema
type: transition
episode: define-product-scope
operation: create
target_type: decision
target_id: llm-extraction-schema-decision
---

# Choose LLM Extraction Schema

## Rationale

The standard schema (Option B) is the minimum viable set of fields to power both gap analysis and market trend aggregation. Richer qualitative fields add extraction cost without MVP value; a flat skills list is too narrow for seniority-aware gap analysis.

## Before

No extraction schema defined.

## After

Twelve structured fields extracted per job posting via Claude API. Schema covers identity fields, seniority, role type, skills, tech stack, experience, compensation, and work location.

## Evidence

- `.memory/alternatives/llm-extraction-schema.md`
- `.memory/decisions/llm-extraction-schema-decision.md`
