import uuid
from datetime import datetime

from sqlalchemy import DateTime, Float, ForeignKey, Integer, String, Text, func
from sqlalchemy.dialects.postgresql import ARRAY, JSONB, UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class JobPosting(Base):
    __tablename__ = "job_postings"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    external_id: Mapped[str] = mapped_column(String, unique=True, index=True)
    source: Mapped[str] = mapped_column(String, default="jsearch")

    title: Mapped[str] = mapped_column(String)
    company: Mapped[str] = mapped_column(String)
    location: Mapped[str] = mapped_column(String)
    seniority_level: Mapped[str | None] = mapped_column(String, nullable=True)
    role_type: Mapped[str | None] = mapped_column(String, nullable=True)
    required_skills: Mapped[list] = mapped_column(JSONB, default=list)
    preferred_skills: Mapped[list] = mapped_column(JSONB, default=list)
    tech_stack: Mapped[list] = mapped_column(JSONB, default=list)
    years_experience: Mapped[int | None] = mapped_column(Integer, nullable=True)
    salary_min: Mapped[int | None] = mapped_column(Integer, nullable=True)
    salary_max: Mapped[int | None] = mapped_column(Integer, nullable=True)
    salary_currency: Mapped[str | None] = mapped_column(String, nullable=True)
    remote_type: Mapped[str | None] = mapped_column(String, nullable=True)
    company_stage: Mapped[str | None] = mapped_column(String, nullable=True)

    raw_description: Mapped[str | None] = mapped_column(Text, nullable=True)
    extracted_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    gap_reports: Mapped[list["GapReport"]] = relationship(back_populates="job_posting")


class UserProfile(Base):
    __tablename__ = "user_profiles"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name: Mapped[str] = mapped_column(String)
    skills: Mapped[list] = mapped_column(JSONB, default=list)
    years_experience: Mapped[int | None] = mapped_column(Integer, nullable=True)
    current_level: Mapped[str | None] = mapped_column(String, nullable=True)
    target_roles: Mapped[list] = mapped_column(JSONB, default=list)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    gap_reports: Mapped[list["GapReport"]] = relationship(back_populates="user_profile")


class GapReport(Base):
    __tablename__ = "gap_reports"

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    job_posting_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("job_postings.id"))
    user_profile_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("user_profiles.id"))

    match_score: Mapped[float] = mapped_column(Float)
    missing_required: Mapped[list] = mapped_column(JSONB, default=list)
    missing_preferred: Mapped[list] = mapped_column(JSONB, default=list)
    seniority_fit: Mapped[str] = mapped_column(String)  # "above" | "match" | "below"
    role_type_match: Mapped[bool] = mapped_column(default=False)
    summary: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())

    job_posting: Mapped["JobPosting"] = relationship(back_populates="gap_reports")
    user_profile: Mapped["UserProfile"] = relationship(back_populates="gap_reports")
