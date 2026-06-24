from datetime import datetime, timezone

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from levelmatch.db.models import JobPosting
from levelmatch.extraction import claude
from levelmatch.extraction.normalize import normalize_skills
from levelmatch.ingestion.jsearch import RawJobPosting, search_jobs


async def ingest(query: str, db: AsyncSession, num_pages: int = 1) -> dict:
    raw_postings = await search_jobs(query, num_pages=num_pages)

    created = 0
    skipped = 0

    for raw in raw_postings:
        existing = await db.scalar(
            select(JobPosting).where(JobPosting.external_id == raw.external_id)
        )
        if existing:
            skipped += 1
            continue

        extracted = claude.extract(
            title=raw.title,
            company=raw.company,
            location=raw.location,
            description=raw.description,
        )

        salary = extracted.salary_range
        posting = JobPosting(
            external_id=raw.external_id,
            title=extracted.title,
            company=extracted.company,
            location=extracted.location,
            seniority_level=extracted.seniority_level,
            role_type=extracted.role_type,
            required_skills=normalize_skills(extracted.required_skills),
            preferred_skills=normalize_skills(extracted.preferred_skills),
            tech_stack=normalize_skills(extracted.tech_stack),
            years_experience=extracted.years_experience,
            salary_min=salary.min if salary else None,
            salary_max=salary.max if salary else None,
            salary_currency=salary.currency if salary else None,
            remote_type=extracted.remote_type,
            company_stage=extracted.company_stage,
            raw_description=raw.description,
            extracted_at=datetime.now(timezone.utc),
        )
        db.add(posting)
        created += 1

    await db.commit()
    return {"created": created, "skipped": skipped, "total_fetched": len(raw_postings)}
