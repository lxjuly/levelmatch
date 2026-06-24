---
id: resume-parsing-yields-usable-profile
type: claim
status: settled
---

# Claude Resume Parsing Yields A Usable Profile

LLM parsing of a resume produces a UserProfile good enough to drive matching — name,
skills, years of experience, seniority level, and target roles.

This settles the first claim-to-validate listed in [[resume-upload-matching]].

## Evidence

A sample senior ML resume parsed via Claude Haiku returned: name "Jane Doe",
years_experience 7, current_level "senior", target_roles ["Senior AI Engineer",
"ML Engineer", "Staff ML Engineer"], and a normalized skills list. The output fed
the gap analyzer unchanged.

Caveat: skills inherit the known [[normalization-loses-product-casing]] limitation
(Pytorch, Langchain, MLOPS).
