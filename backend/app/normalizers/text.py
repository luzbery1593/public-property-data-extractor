import re


def normalize_whitespace(value: str | None) -> str | None:
    if value is None:
        return None

    normalized = re.sub(r"\s+", " ", value).strip()
    return normalized or None


def normalize_optional_text(value: str | None) -> str | None:
    return normalize_whitespace(value)


def normalize_required_text(value: str) -> str:
    normalized = normalize_whitespace(value)
    if normalized is None:
        raise ValueError("value must not be empty")

    return normalized
