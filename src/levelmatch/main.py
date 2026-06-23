from fastapi import FastAPI

from levelmatch.api.routes import ingest, jobs

app = FastAPI(title="LevelMatch", version="0.1.0")

app.include_router(ingest.router)
app.include_router(jobs.router)


@app.get("/health")
async def health():
    return {"status": "ok"}
