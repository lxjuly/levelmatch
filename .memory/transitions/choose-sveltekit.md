---
id: choose-sveltekit
type: transition
episode: plan-dashboard
operation: create
target_type: decision
target_id: frontend-sveltekit
---

# Choose SvelteKit For Frontend

## Rationale

The project steward dislikes React's complexity. SvelteKit offers language-level
reactivity, small compiled bundles suited to a dashboard, and a first-class
Cloudflare Pages adapter — matching both the preference and the hosting decision.

## Before

Frontend was Next.js, bundled inside [[stack-decision]].

## After

A standalone Decision records SvelteKit as the frontend. The formal
supersede relationship to the bundled stack-decision is deferred.

## Evidence

- `.memory/alternatives/frontend.md`
- `.memory/decisions/frontend-sveltekit.md`
