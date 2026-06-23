---
id: gap-analyzer-decision
type: decision
status: accepted
---

# Gap Analyzer — Composite Gap Report (Option D)

The gap analyzer produces a composite gap report per job posting, combining:

- **Match score** — % of required skills the user covers
- **Missing skills** — required and preferred skills the user lacks, ranked by frequency across postings
- **Seniority assessment** — whether the role is above / at / below the user's level
- **Role type alignment** — whether the posting's role_type matches the user's target roles

Output shape per posting:

```
{
  match_score: float,          # 0.0–1.0
  missing_required: list[str],
  missing_preferred: list[str],
  seniority_fit: "above" | "match" | "below",
  role_type_match: bool,
  summary: str                 # Claude-generated one-liner
}
```

The market aggregate view (Option E) is deferred to the August dashboard. Learning path generation (Option F) is deferred post-MVP.

See [[gap-analyzer-alternatives]] for options considered.
