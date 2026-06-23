from pydantic import BaseModel, Field


class SalaryRange(BaseModel):
    min: int | None = None
    max: int | None = None
    currency: str = "USD"


class ExtractedPosting(BaseModel):
    title: str
    company: str
    location: str
    seniority_level: str | None = Field(None, description="junior | mid | senior | staff | principal")
    role_type: str | None = Field(None, description="e.g. ML Engineer, Data Scientist, AI Engineer")
    required_skills: list[str] = Field(default_factory=list)
    preferred_skills: list[str] = Field(default_factory=list)
    tech_stack: list[str] = Field(default_factory=list)
    years_experience: int | None = None
    salary_range: SalaryRange | None = None
    remote_type: str | None = Field(None, description="remote | hybrid | on-site")
    company_stage: str | None = Field(None, description="startup | series-a | series-b | public | unknown")
