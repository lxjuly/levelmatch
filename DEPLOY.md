# Deploying LevelMatch

Hosting split (see `.memory/decisions/hosting-decision.md`):

- **Backend (FastAPI + Postgres)** → Railway
- **Frontend (SvelteKit)** → Cloudflare Pages
- **Domain / DNS / SSL** → Cloudflare

## 1. Backend on Railway

Repo config lives in `railway.toml` (start command, migrations, healthcheck).

1. Create a Railway project and add this repo as a service (root = repo root).
2. Add the **PostgreSQL** plugin. Railway injects `DATABASE_URL` automatically;
   `config.py` rewrites it to the asyncpg driver form.
3. Set service variables:
   - `ANTHROPIC_API_KEY`
   - `JSEARCH_API_KEY`
   - `CORS_ORIGINS` = the Cloudflare Pages URL (e.g. `https://levelmatch.pages.dev`),
     comma-separated if more than one
4. Deploy. `preDeployCommand` runs `alembic upgrade head`; the service starts with
   `uvicorn levelmatch.main:app --app-dir src`. Healthcheck is `/health`.
5. Note the public API URL Railway assigns (e.g. `https://levelmatch-api.up.railway.app`).

CLI alternative: `railway up` after `railway login` and `railway link`.

## 2. Frontend on Cloudflare Pages

1. Create a Pages project from this repo.
2. Build settings:
   - **Root directory:** `web`
   - **Build command:** `npm run build`
   - **Build output directory:** `.svelte-kit/cloudflare`
3. Build-time environment variable:
   - `PUBLIC_API_BASE` = the Railway API URL from step 1.5
4. Deploy. Note the Pages URL and set it as `CORS_ORIGINS` on Railway (step 1.3),
   then redeploy the backend.

CLI alternative: `cd web && npm run build && npx wrangler pages deploy .svelte-kit/cloudflare`.

## 3. Domain (optional)

Point a custom domain in Cloudflare: `app.levelmatch.<tld>` → Pages,
`api.levelmatch.<tld>` → Railway. Update `PUBLIC_API_BASE` and `CORS_ORIGINS`
to the custom hostnames and redeploy both.

## Order of operations

Railway first (need its URL for `PUBLIC_API_BASE`) → Pages → set `CORS_ORIGINS`
to the Pages URL on Railway → redeploy backend.
