import uuid

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession

from levelmatch.db.models import UserProfile
from levelmatch.db.session import get_db

router = APIRouter(prefix="/profiles", tags=["profiles"])


class ProfileCreate(BaseModel):
    name: str
    skills: list[str]
    years_experience: int | None = None
    current_level: str | None = None
    target_roles: list[str] = []


@router.post("", status_code=201)
async def create_profile(body: ProfileCreate, db: AsyncSession = Depends(get_db)):
    profile = UserProfile(**body.model_dump())
    db.add(profile)
    await db.commit()
    await db.refresh(profile)
    return profile


@router.get("/{profile_id}")
async def get_profile(profile_id: uuid.UUID, db: AsyncSession = Depends(get_db)):
    profile = await db.get(UserProfile, profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
