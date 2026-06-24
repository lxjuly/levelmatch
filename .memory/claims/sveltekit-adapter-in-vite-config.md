---
id: sveltekit-adapter-in-vite-config
type: claim
status: settled
---

# The SvelteKit Adapter Lives In vite.config.js

In the scaffolded SvelteKit version (Svelte 5 / SvelteKit 2 via `sv create`), the
deployment adapter is configured inside `vite.config.js` (within the `sveltekit`
plugin), not in a separate `svelte.config.js`. Runes mode is forced by default.

## Evidence

Observed when swapping `adapter-auto` for `adapter-cloudflare`: there was no
`svelte.config.js` in the generated project — the adapter import and call live in
`vite.config.js`.

Relevant to the `deploy-stack` plan item: Cloudflare Pages adapter config is
edited there, not in the conventional `svelte.config.js`.
