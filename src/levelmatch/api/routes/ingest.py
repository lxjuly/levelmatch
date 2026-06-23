from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from levelmatch.db.session import get_db
from levelmatch.ingestion.pipeline import ingest

router = APIRouter(prefix="/ingest", tags=["ingest"])


class IngestRequest(BaseModel):
    query: str
    num_pages: int = 1


@router.post("")
async def trigger_ingest(body: IngestRequest, db: AsyncSession = Depends(get_db)):
    result = await ingest(body.query, db, num_pages=body.num_pages)
    return result
