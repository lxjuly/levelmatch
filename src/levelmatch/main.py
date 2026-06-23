from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from levelmatch.api.routes import gap, ingest, jobs, profiles

app = FastAPI(title="LevelMatch", version="0.1.0")

# Dev: SvelteKit runs on a separate origin (Vite on :5173). Production origins
# (Cloudflare Pages) are added via the LEVELMATCH_CORS_ORIGINS env var later.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest.router)
app.include_router(jobs.router)
app.include_router(profiles.router)
app.include_router(gap.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
