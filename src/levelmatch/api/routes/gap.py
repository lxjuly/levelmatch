import uuid

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from levelmatch.db.models import GapReport, JobPosting, UserProfile
from levelmatch.db.session import get_db
from levelmatch.gap.analyzer import analyze

router = APIRouter(prefix="/gap", tags=["gap"])


class BatchGapRequest(BaseModel):
    profile_id: uuid.UUID
    job_ids: list[uuid.UUID] | None = None
    role_type: str | None = None
    limit: int = 10


@router.post("/batch")
async def gap_batch(body: BatchGapRequest, db: AsyncSession = Depends(get_db)):
    profile = await db.get(UserProfile, body.profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    if body.job_ids:
        result = await db.execute(
            select(JobPosting).where(JobPosting.id.in_(body.job_ids))
        )
    else:
        stmt = select(JobPosting).order_by(JobPosting.created_at.desc()).limit(body.limit)
        if body.role_type:
            stmt = stmt.where(JobPosting.role_type.ilike(f"%{body.role_type}%"))
        result = await db.execute(stmt)

    postings = result.scalars().all()
    reports = []
    for posting in postings:
        report = analyze(profile, posting)
        db.add(report)
        reports.append(report)

    await db.commit()
    for r in reports:
        await db.refresh(r)

    return sorted(reports, key=lambda r: r.match_score, reverse=True)


@router.post("/{job_id}")
async def gap_for_job(
    job_id: uuid.UUID,
    profile_id: uuid.UUID = Query(...),
    db: AsyncSession = Depends(get_db),
):
    profile = await db.get(UserProfile, profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    posting = await db.get(JobPosting, job_id)
    if not posting:
        raise HTTPException(status_code=404, detail="Job posting not found")

    report = analyze(profile, posting)
    db.add(report)
    await db.commit()
    await db.refresh(report)
    return report
