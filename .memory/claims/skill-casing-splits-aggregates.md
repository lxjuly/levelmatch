---
id: skill-casing-splits-aggregates
type: claim
status: settled
---

# Inconsistent Skill Casing Splits Aggregates

Extraction emits skill values with inconsistent casing and wording (e.g.
"Machine Learning" vs "Machine learning"), so the same underlying skill is
counted as distinct entries. This splits the Insights market aggregates and
weakens gap matching, which compares skill lists.

## Evidence

Observed directly in the Insights view during the dashboard build: across 10
ingested postings, "Machine Learning" and "Machine learning" appeared as two
separate bars.

Discovered during the `implement-dashboard` episode. Grounds the proposed
`normalize-skills` plan item.
