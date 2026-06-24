# LevelMatch Memory

LevelMatch project memory using the Chronelle ontology.

## Structure

```
.memory/
  alternatives/    — options considered for a decision
  assumptions/     — beliefs the project relies on
  checkpoints/     — mutable working state, one per active session
  claims/          — truth-apt propositions (unsettled/settled/refuted)
  constraints/     — boundaries on what the project can do
  decisions/       — chosen directions and their rationale
  episodes/        — bounded activities worth preserving
  goals/           — intended outcomes
  plans/           — task-planning projection (current.md)
  transitions/     — state changes to durable primitives
```

Ontology reference: [Chronelle](../chronelle) (co-located workspace project).
