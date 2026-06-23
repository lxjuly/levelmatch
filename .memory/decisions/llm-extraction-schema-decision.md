---
id: llm-extraction-schema-decision
type: decision
status: accepted
---

# LLM Extraction Schema — Standard (Option B)

LevelMatch extracts the following fields from each raw job posting via Claude API:

```
title           str
company         str
location        str
seniority_level str        # e.g. "junior", "mid", "senior", "staff", "principal"
role_type       str        # e.g. "ML Engineer", "Data Scientist", "AI Engineer"
required_skills list[str]
preferred_skills list[str]
tech_stack      list[str]
years_experience int | null
salary_range    {min: int, max: int, currency: str} | null
remote_type     str        # "remote", "hybrid", "on-site"
company_stage   str | null # e.g. "startup", "series-a", "public"
```

This schema is the minimum needed to power gap analysis (required_skills + seniority_level + years_experience vs. user background) and market trend aggregation (role_type + tech_stack frequency).

Qualitative fields (responsibilities, culture signals) and taxonomy mapping are deferred.

See [[llm-extraction-schema-alternatives]] for options considered.
