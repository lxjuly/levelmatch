---
id: dev-origin-needs-cors
type: claim
status: settled
---

# The Dashboard Dev Origin Requires CORS

The SvelteKit dev server origin (`localhost:5173`) cannot call the FastAPI backend
(`localhost:8000`) without CORS enabled on the backend, because the dashboard and
API are served from different origins.

## Evidence

The dashboard's `fetch` calls failed cross-origin until `CORSMiddleware` was added
to the API allowing the `:5173` origin.

This generalizes to deploy: the production Cloudflare Pages origin must be added
to the API's allowed origins (tracked in the `deploy-stack` plan item).
