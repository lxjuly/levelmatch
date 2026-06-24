---
id: implement-resume-upload-matching
type: episode
status: completed
---

# Implement Resume Upload And Matching

This Episode records building use case 1 of [[two-sided-matching-loop]]: upload a
resume, parse it into a profile, and get matched.

## Context

The proposed Goal `resume-upload-matching` was committed (accepted → active), its
fork resolved (parse-via-Claude), and built against the existing profile + gap
analyzer.

## Participants

- project steward
- Claude (claude-opus-4-8)

## Inputs

- Goal: resume-upload-matching; Decision: resume-parse-via-claude
- Existing UserProfile model, gap analyzer, and skill normalizer

## Outputs

- `src/levelmatch/resume/parse.py`: PDF/text extraction + Claude profile parsing
- `POST /profiles/from-resume`: upload → parse → create UserProfile
- Profile page: resume upload card that sets the parsed profile active
- Deps added: pypdf, python-multipart
- Verified: a sample resume parsed to a senior profile feeding the gap analyzer
- Settled Claim: resume-parsing-yields-usable-profile

## Transitions

- create-resume-parse-decision
- accept-resume-upload-goal
- settle-resume-parsing-claim
- implement-resume-upload-matching
