"""Canonicalize extracted skill strings so the same skill isn't counted twice.

Grounded in the `skill-casing-splits-aggregates` claim: Claude emits skills with
inconsistent casing ("Machine Learning" vs "Machine learning"), which splits
aggregates and weakens gap matching. We canonicalize to Title Case while keeping
known acronyms uppercase.
"""

# Tokens that should stay uppercase rather than be Title-Cased.
ACRONYMS = {
    "ai", "ml", "llm", "llms", "rag", "sql", "nosql", "aws", "gcp", "gcs",
    "api", "apis", "nlp", "etl", "elt", "ci", "cd", "gpu", "cpu", "mlops",
    "devops", "a2a", "mcp", "sdk", "ui", "ux", "css", "html", "js", "ts",
    "ide", "orm", "saas", "paas", "k8s", "rl", "rlhf", "gpt", "tpu", "hpc",
}


def normalize_skill(raw: str) -> str:
    """Trim, collapse whitespace, Title Case, but uppercase known acronyms."""
    collapsed = " ".join(raw.strip().split())
    if not collapsed:
        return ""
    words = []
    for word in collapsed.split(" "):
        lowered = word.lower()
        if lowered in ACRONYMS:
            words.append(lowered.upper())
        else:
            words.append(word[:1].upper() + word[1:].lower())
    return " ".join(words)


def normalize_skills(items: list[str]) -> list[str]:
    """Normalize a list, dropping blanks and case-insensitive duplicates, order-stable."""
    seen: set[str] = set()
    out: list[str] = []
    for item in items or []:
        normalized = normalize_skill(item)
        key = normalized.lower()
        if key and key not in seen:
            seen.add(key)
            out.append(normalized)
    return out
