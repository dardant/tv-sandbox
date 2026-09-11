"""Written by scripts/verify_real_cicd.py to prove exact-revision delivery evidence."""

MARKER = "31f0d194"


def slug(value: str) -> str:
    return value.strip().lower()
