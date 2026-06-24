---
id: create-resume-parse-decision
type: transition
episode: implement-resume-upload-matching
operation: create
target_type: decision
target_id: resume-parse-via-claude
---

# Create Resume-Parse Decision

## Rationale

The use case's fork (Claude parse vs embeddings) needed resolving before building.

## Before

Goal `resume-upload-matching` carried an unresolved fork.

## After

Decision `resume-parse-via-claude` records parse-to-UserProfile via Claude, reusing
the gap analyzer.

## Evidence

- `.memory/decisions/resume-parse-via-claude.md`
