---
id: normalization-loses-product-casing
type: claim
status: settled
---

# Title-Case Normalization Degrades Product-Name Casing

The skill normalization canonicalizes casing by Title-Casing words and uppercasing
a known acronym set. This fixes the case-split problem, but it lowercases the
interior of camelCase product names: "LangChain" → "Langchain", "CrewAI" →
"Crewai", "PyTorch" → "Pytorch", "TensorFlow" → "Tensorflow".

So the fix trades one inaccuracy (split aggregates) for a smaller one (degraded
product-name fidelity). Dedup is correct; display casing for named products is not.

## Evidence

After the normalization backfill, the Insights tech-stack panel showed
"Langchain", "Crewai", "Autogen", "Pytorch", "Tensorflow".

Grounds a future refinement: a canonical skill dictionary / alias map that maps
variants to a curated display label, rather than algorithmic Title Case.
