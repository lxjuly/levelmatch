---
id: implement-resume-upload-matching
type: transition
episode: implement-resume-upload-matching
operation: create
target_type: milestone
target_id: resume-upload-matching
---

# Implement Resume Upload And Matching

## Rationale

Delivers the first use case of the two-sided loop: a resume becomes a profile that
feeds the existing gap analyzer.

## Before

Profiles could only be created by filling a form.

## After

A resume (PDF or text) can be uploaded; Claude parses it into a UserProfile, which
is set active and matched on the Jobs view. Backend `POST /profiles/from-resume`,
`resume/parse.py`, and a Profile-page upload card.

## Evidence

- `src/levelmatch/resume/parse.py`
- `src/levelmatch/api/routes/profiles.py`
- `web/src/routes/profile/+page.svelte`, `web/src/lib/api.js`
