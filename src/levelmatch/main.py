from fastapi import FastAPI

from levelmatch.api.routes import gap, ingest, jobs, profiles

app = FastAPI(title="LevelMatch", version="0.1.0")

app.include_router(ingest.router)
app.include_router(jobs.router)
app.include_router(profiles.router)
app.include_router(gap.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
