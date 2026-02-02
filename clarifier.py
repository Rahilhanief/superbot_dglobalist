AMBIGUOUS_TERMS = [
    "best",
    "recommend",
    "collaborate",
    "good fit",
    "partner"
]

def needs_clarification(query: str) -> bool:
    query = query.lower()
    return any(term in query for term in AMBIGUOUS_TERMS)
