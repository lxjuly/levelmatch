---
id: resume-parse-via-claude
type: decision
status: accepted
---

# Parse Resumes To A Structured Profile Via Claude

Resolves the fork in [[resume-upload-matching]]: parse an uploaded resume into a
structured UserProfile via Claude (reusing the extraction pattern), rather than
embedding-based similarity matching.

A parsed profile drops straight into the existing gap analyzer with no new matching
machinery — the resume simply becomes a better-sourced UserProfile. Embedding-based
matching remains a future alternative the steward wants to explore (see
build-job-loop's alternatives note).

Text is extracted from PDF (pypdf) or plain text, then Claude Haiku returns the
profile fields; skills are run through the existing normalizer.
