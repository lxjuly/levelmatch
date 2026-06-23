import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from levelmatch.db.models import JobPosting
from levelmatch.db.session import get_db

router = APIRouter(prefix="/jobs", tags=["jobs"])


@router.get("")
async def list_jobs(
    role_type: str | None = Query(None),
    seniority_level: str | None = Query(None),
    remote_type: str | None = Query(None),
    limit: int = Query(20, le=100),
    offset: int = Query(0),
    db: AsyncSession = Depends(get_db),
):
    stmt = select(JobPosting).order_by(JobPosting.created_at.desc()).limit(limit).offset(offset)

    if role_type:
        stmt = stmt.where(JobPosting.role_type.ilike(f"%{role_type}%"))
    if seniority_level:
        stmt = stmt.where(JobPosting.seniority_level == seniority_level)
    if remote_type:
        stmt = stmt.where(JobPosting.remote_type == remote_type)

    result = await db.execute(stmt)
    postings = result.scalars().all()
    return postings


@router.get("/{job_id}")
async def get_job(job_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    posting = await db.get(JobPosting, job_id)
    if not posting:
        raise HTTPException(status_code=404, detail="Job posting not found")
    return posting
