---
id: frontend-alternatives
type: alternative
status: resolved
resolved_by: frontend-sveltekit
---

# Frontend Framework Alternatives

Alternatives considered for the LevelMatch dashboard frontend. The project
steward dislikes React's complexity (hooks, useEffect, ceremony), prompting a
re-evaluation of the Next.js choice recorded in [[stack-decision]].

## SvelteKit — accepted

Reactivity is built into the language — no hooks or effect-dependency mental
model. Compiles away to small, fast bundles, ideal for a dashboard. First-class
Cloudflare Pages adapter. Still a recognizable modern framework on a portfolio.

## Astro

Ships zero JS by default; opt into interactive islands only where needed. Great
for read-heavy dashboards. Less ideal if the dashboard becomes heavily
interactive.

## Vue (Vite, no Nuxt)

Gentler than React, template-based. Mature ecosystem and charting libraries.
Heavier than SvelteKit for the same result here.

## HTMX + FastAPI templates

Lightest possible — no separate frontend build; FastAPI serves HTML and HTMX
handles interactivity. Keeps everything in Python but weakens the frontend
portfolio signal and makes charts awkward.

## Next.js — superseded for this project

The original [[stack-decision]] choice. Dropped because React's complexity is a
poor fit for the steward's preference and unnecessary for an API-backed
dashboard.
