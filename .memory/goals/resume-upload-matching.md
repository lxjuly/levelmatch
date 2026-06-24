---
id: resume-upload-matching
type: goal
status: active
---

# Resume Upload And Job Matching

A user uploads a resume and is matched to relevant jobs.

**Status:** Implemented (committed via [[resume-parse-via-claude]]); live on next
deploy. First slice of the loop is built.

**Why:** The resume is the richest single signal of a candidate's level and skills.
Parsing it replaces manual profile entry and feeds the existing gap analyzer with
far better input. First step of [[two-sided-matching-loop]].

**Depends on:** current ingestion + gap analyzer (a parsed resume becomes a
UserProfile).

**Claims to validate (before committing):**
- LLM resume parsing yields a profile good enough to drive matching.
- Users prefer uploading a resume over filling a profile form.

**Main fork:** structured parse → UserProfile via Claude, vs. embedding-based
similarity matching against postings. (Likely parse first; embeddings later.)
