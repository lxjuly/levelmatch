from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from levelmatch.api.routes import gap, ingest, jobs, profiles
from levelmatch.config import settings

app = FastAPI(title="LevelMatch", version="0.1.0")

# Allowed origins come from the CORS_ORIGINS env var (dev defaults to the Vite
# origin; production adds the Cloudflare Pages origin).
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
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
