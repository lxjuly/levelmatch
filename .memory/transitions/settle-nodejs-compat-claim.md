---
id: settle-nodejs-compat-claim
type: transition
episode: deploy-to-production
operation: create
target_type: claim
target_id: sveltekit-cloudflare-needs-nodejs-compat
---

# Settle The nodejs_compat Claim

## Rationale

The Cloudflare deploy surfaced a truth-apt requirement worth recording so it isn't
rediscovered: SvelteKit SSR Workers need the nodejs_compat flag.

## Before

The requirement was an unrecorded deploy-time warning.

## After

Settled claim `sveltekit-cloudflare-needs-nodejs-compat` records it, grounding the
`web/wrangler.toml` config.

## Evidence

- `.memory/claims/sveltekit-cloudflare-needs-nodejs-compat.md`
- `web/wrangler.toml`
