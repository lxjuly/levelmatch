---
id: sveltekit-cloudflare-needs-nodejs-compat
type: claim
status: settled
---

# SvelteKit On Cloudflare Pages Needs nodejs_compat

A SvelteKit app deployed to Cloudflare Pages (adapter-cloudflare) runs its SSR as
a Worker, and that Worker imports `node:async_hooks` via `@sveltejs/kit`. Without
the `nodejs_compat` compatibility flag (and a `compatibility_date`), the Worker
throws at runtime.

## Evidence

The first `wrangler pages deploy` warned that `node:async_hooks` was not found and
the Worker "may throw errors at runtime unless you enable the nodejs_compat
compatibility flag." Adding `web/wrangler.toml` with
`compatibility_flags = ["nodejs_compat"]` and a `compatibility_date`, then
redeploying, cleared the warning.

Connects to [[sveltekit-adapter-in-vite-config]]: the SvelteKit-on-Cloudflare path
has several config gotchas that live outside the conventional locations.
