---
id: stack-decision
type: decision
status: accepted
---

# LevelMatch Stack

- **Backend:** Python + FastAPI
- **Database:** PostgreSQL
- **Frontend:** Next.js — deferred to August
- **LLM:** Claude API (Haiku for extraction, Sonnet for complex reasoning)

Python + FastAPI is the natural fit for LLM/AI pipeline work. PostgreSQL handles structured job posting records and scales past MVP. The frontend is out of July MVP scope — pipeline and LLM extraction ship first, dashboard follows in August. Claude API is chosen for structured extraction given cost efficiency and ecosystem alignment.

See [[stack-alternatives]] for the full set of options considered.
