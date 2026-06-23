---
id: gap-analyzer-alternatives
type: alternative
status: resolved
resolved_by: gap-analyzer-decision
---

# Gap Analyzer Alternatives

Alternatives considered for defining "gap" and the gap analyzer output.

## Option A — Skills diff

Compare user's skills against `required_skills[]` and `preferred_skills[]` across postings. Output: ranked list of missing skills by frequency. Too narrow — ignores seniority and role fit context.

## Option B — Seniority fit

Compare user's years/level against `seniority_level` and `years_experience` per posting. Output: each role flagged as above/at/below the user's level. Useful signal but insufficient on its own.

## Option C — Per-posting fit score

Score each job posting against the user's profile across skills, seniority, and role type. Output: ranked list of postings with a % match score. Actionable for job applications but loses the "what to fix" narrative.

## Option D — Composite gap report — accepted

Combine skills diff + seniority fit + role type alignment into a structured report. Output: match percentage, top missing skills, seniority assessment. Best balance of depth and clarity for MVP.

## Option E — Market aggregate view

Aggregate across all ingested postings to surface what the market is asking for vs. what the user has. Output: "Top missing skills across AI Engineer roles in the last 30 days." Deferred to August dashboard.

## Option F — Learning path

Given the gap, generate prioritized learning recommendations. Compelling but depends on quality gap data — deferred post-MVP.
