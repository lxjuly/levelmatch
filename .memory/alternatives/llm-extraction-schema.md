---
id: llm-extraction-schema-alternatives
type: alternative
status: resolved
resolved_by: llm-extraction-schema-decision
---

# LLM Extraction Schema Alternatives

Alternatives considered for what structured fields to extract from raw job postings.

## Option A — Minimal

`title, company, location, seniority_level, required_skills[], salary_range, remote_type`

Too thin for gap analysis. Sufficient to render a listing but not to compute skill gaps or aggregate market trends.

## Option B — Standard — accepted

`title, company, location, seniority_level, role_type, required_skills[], preferred_skills[], tech_stack[], years_experience, salary_range, remote_type, company_stage`

Minimum viable schema for both gap analysis (required_skills + seniority_level + years_experience vs. user background) and market trend views (role_type + tech_stack frequency). Balances extraction cost and analytical value.

## Option C — Rich

All of Option B plus: `responsibilities[], team_signals, culture_signals, interview_hints`

Adds qualitative noise at extraction time without clear MVP value. Deferred.

## Option D — Flat skills only

Extract a normalized list of skills/technologies per posting only. Too narrow — gap analysis needs seniority and role type context, not just skills.

## Option E — Taxonomy-driven

Extract against a fixed controlled vocabulary mapping skills to predefined categories. Produces cleaner aggregations but requires maintaining a taxonomy and breaks on emerging terms. Deferred until signal quality demands it.
