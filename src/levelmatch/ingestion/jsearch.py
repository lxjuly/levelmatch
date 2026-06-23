from dataclasses import dataclass

import httpx

from levelmatch.config import settings

JSEARCH_SEARCH_URL = "https://api.openwebninja.com/jsearch/search-v2"
JSEARCH_HEADERS = {
    "X-API-Key": settings.jsearch_api_key,
}


@dataclass
class RawJobPosting:
    external_id: str
    title: str
    company: str
    location: str
    description: str
    job_apply_link: str | None = None


async def search_jobs(query: str, page: int = 1, num_pages: int = 1) -> list[RawJobPosting]:
    params = {
        "query": query,
        "page": str(page),
        "num_pages": str(num_pages),
        "country": "us",
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(
            JSEARCH_SEARCH_URL,
            headers=JSEARCH_HEADERS,
            params=params,
            timeout=30.0,
        )
        response.raise_for_status()

    data = response.json()
    postings = []

    for item in data.get("data", {}).get("jobs", []):
        postings.append(
            RawJobPosting(
                external_id=item["job_id"],
                title=item.get("job_title", ""),
                company=item.get("employer_name", ""),
                location=_parse_location(item),
                description=item.get("job_description", ""),
                job_apply_link=item.get("job_apply_link"),
            )
        )

    return postings


def _parse_location(item: dict) -> str:
    city = item.get("job_city", "")
    state = item.get("job_state", "")
    country = item.get("job_country", "")
    parts = [p for p in [city, state, country] if p]
    return ", ".join(parts) if parts else "Unknown"
