import re

def sanitize_query(text: str) -> str:
    text = text.strip()
    text = re.sub(r"[<>]", "", text)

    if len(text) > 500:
        raise ValueError("Query too long")

    return text
