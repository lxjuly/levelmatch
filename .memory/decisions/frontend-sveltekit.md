---
id: frontend-sveltekit
type: decision
status: accepted
---

# Frontend — SvelteKit

The LevelMatch dashboard frontend is SvelteKit.

SvelteKit's language-level reactivity avoids React's hooks/effect complexity,
which the project steward finds a poor fit. It compiles to small, fast bundles
well-suited to a data dashboard, and has a first-class Cloudflare Pages adapter
(see [[hosting-decision]]).

This refines the frontend choice originally recorded in [[stack-decision]],
which named Next.js. The relationship between this decision and that bundled
stack decision (whether to formally supersede, and how) is intentionally
deferred.

See [[frontend-alternatives]] for options considered.
