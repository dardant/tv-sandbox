"""Written by scripts/verify_real_cicd.py to prove exact-revision delivery evidence."""

MARKER = "582f3be4"


def slug(value: str) -> str:
    return value.strip().lower()
