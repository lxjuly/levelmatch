import json

import anthropic

from levelmatch.config import settings
from levelmatch.extraction.schema import ExtractedPosting

_client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

_SYSTEM_PROMPT = """You are a structured data extractor for job postings.
Extract the requested fields from the job description provided.
Return only valid JSON matching the schema. Use null for fields you cannot determine."""

_EXTRACTION_SCHEMA = """{
  "title": "string",
  "company": "string",
  "location": "string",
  "seniority_level": "junior | mid | senior | staff | principal | null",
  "role_type": "string | null (e.g. ML Engineer, Data Scientist, AI Engineer)",
  "required_skills": ["string"],
  "preferred_skills": ["string"],
  "tech_stack": ["string"],
  "years_experience": "integer | null",
  "salary_range": {"min": "integer | null", "max": "integer | null", "currency": "string"} | null,
  "remote_type": "remote | hybrid | on-site | null",
  "company_stage": "startup | series-a | series-b | public | unknown | null"
}"""


def extract(title: str, company: str, location: str, description: str) -> ExtractedPosting:
    prompt = f"""Extract structured fields from this job posting.

Title: {title}
Company: {company}
Location: {location}

Description:
{description[:4000]}

Return JSON matching this schema:
{_EXTRACTION_SCHEMA}"""

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
    data.setdefault("title", title)
    data.setdefault("company", company)
    data.setdefault("location", location)

    return ExtractedPosting.model_validate(data)
