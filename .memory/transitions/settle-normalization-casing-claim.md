---
id: settle-normalization-casing-claim
type: transition
episode: implement-skill-normalization
operation: create
target_type: claim
target_id: normalization-loses-product-casing
---

# Settle The Product-Casing Limitation Claim

## Rationale

The normalization fix introduced a smaller, truth-apt inaccuracy worth tracking so
it isn't rediscovered: Title Case degrades camelCase product names.

## Before

The limitation existed but was unrecorded.

## After

Settled claim `normalization-loses-product-casing` records it, grounding a future
canonical-skill-dictionary refinement.

## Evidence

- `.memory/claims/normalization-loses-product-casing.md`
