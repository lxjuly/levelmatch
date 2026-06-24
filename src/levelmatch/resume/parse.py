"""Resume ingestion: extract text from an upload, then parse it into a profile.

Fork resolved in `resume-parse-via-claude`: parse to a structured UserProfile via
Claude (reusing the extraction pattern), rather than embedding-based matching.
"""

import io
import json

import anthropic
from pydantic import BaseModel, Field
from pypdf import PdfReader

from levelmatch.config import settings
from levelmatch.extraction.normalize import normalize_skills

_client = anthropic.Anthropic(api_key=settings.anthropic_api_key)


class ParsedProfile(BaseModel):
    name: str = "Candidate"
    skills: list[str] = Field(default_factory=list)
    years_experience: int | None = None
    current_level: str | None = Field(None, description="junior | mid | senior | staff | principal")
    target_roles: list[str] = Field(default_factory=list)


def extract_text(filename: str, content: bytes) -> str:
    """Pull plain text from a .pdf or text upload."""
    name = (filename or "").lower()
    if name.endswith(".pdf"):
        reader = PdfReader(io.BytesIO(content))
        return "\n".join(page.extract_text() or "" for page in reader.pages)
    # .txt / .md / plain
    return content.decode("utf-8", errors="ignore")


_SYSTEM_PROMPT = """You parse resumes into a structured candidate profile.
Return only valid JSON matching the schema. Infer level and target roles from the
overall resume. Use null where you cannot determine a value."""

_SCHEMA = """{
  "name": "string",
  "skills": ["string"],
  "years_experience": "integer | null",
  "current_level": "junior | mid | senior | staff | principal | null",
  "target_roles": ["string (roles this candidate is a fit for / targeting)"]
}"""


def parse_profile(text: str) -> ParsedProfile:
    prompt = f"""Parse this resume into the profile schema.

Resume:
{text[:8000]}

Return JSON matching:
{_SCHEMA}"""

    message = _client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=_SYSTEM_PROMPT,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = message.content[0].text.strip()
    if raw.startswith("```"):
        raw = raw.split("```")[1]
        if raw.startswith("json"):
            raw = raw[4:]

    data = json.loads(raw)
    profile = ParsedProfile.model_validate(data)
    profile.skills = normalize_skills(profile.skills)
    return profile
