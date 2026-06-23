import anthropic

from levelmatch.config import settings
from levelmatch.db.models import GapReport, JobPosting, UserProfile

_client = anthropic.Anthropic(api_key=settings.anthropic_api_key)

SENIORITY_RANK = {
    "junior": 1,
    "entry": 1,
    "mid": 2,
    "intermediate": 2,
    "senior": 3,
    "lead": 4,
    "staff": 4,
    "principal": 5,
    "director": 5,
}


def _normalize(skills: list[str]) -> set[str]:
    return {s.lower().strip() for s in skills}


def _match_skills(user_skills: set[str], posting_skills: list[str]) -> tuple[list[str], float]:
    missing = []
    matched = 0
    for skill in posting_skills:
        skill_lower = skill.lower().strip()
        if any(skill_lower in u or u in skill_lower for u in user_skills):
            matched += 1
        else:
            missing.append(skill)
    total = len(posting_skills)
    score = matched / total if total > 0 else 1.0
    return missing, score


def _seniority_fit(user_level: str | None, posting_level: str | None) -> str:
    if not user_level or not posting_level:
        return "match"
    user_rank = SENIORITY_RANK.get(user_level.lower(), 0)
    posting_rank = SENIORITY_RANK.get(posting_level.lower(), 0)
    if user_rank == 0 or posting_rank == 0:
        return "match"
    if user_rank < posting_rank:
        return "above"
    if user_rank > posting_rank:
        return "below"
    return "match"


def _role_type_match(user_targets: list[str], posting_role: str | None) -> bool:
    if not posting_role or not user_targets:
        return False
    posting_lower = posting_role.lower()
    return any(t.lower() in posting_lower or posting_lower in t.lower() for t in user_targets)


def _generate_summary(
    posting: JobPosting,
    match_score: float,
    missing_required: list[str],
    seniority_fit: str,
) -> str:
    prompt = f"""Job: {posting.title} at {posting.company}
Match score: {match_score:.0%}
Seniority fit: {seniority_fit}
Top missing required skills: {', '.join(missing_required[:3]) if missing_required else 'none'}

Write a single sentence (max 20 words) summarizing how well this role fits the candidate."""

    message = _client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=60,
        messages=[{"role": "user", "content": prompt}],
    )
    return message.content[0].text.strip()


def analyze(profile: UserProfile, posting: JobPosting) -> GapReport:
    user_skills = _normalize(profile.skills or [])

    missing_required, required_score = _match_skills(user_skills, posting.required_skills or [])
    missing_preferred, _ = _match_skills(user_skills, posting.preferred_skills or [])

    seniority = _seniority_fit(profile.current_level, posting.seniority_level)
    role_match = _role_type_match(profile.target_roles or [], posting.role_type)

    summary = _generate_summary(posting, required_score, missing_required, seniority)

    return GapReport(
        job_posting_id=posting.id,
        user_profile_id=profile.id,
        match_score=required_score,
        missing_required=missing_required,
        missing_preferred=missing_preferred,
        seniority_fit=seniority,
        role_type_match=role_match,
        summary=summary,
    )
