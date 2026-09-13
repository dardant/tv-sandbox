"""Whitespace and accent normalisation shared by the other modules."""

from __future__ import annotations

import re
import unicodedata

_SPACES = re.compile(r"\s+")


def collapse_whitespace(text: str) -> str:
    """Runs of whitespace collapsed to one, with both ends trimmed."""
    return _SPACES.sub(" ", text).strip()


def fold_accents(text: str) -> str:
    """Accented letters replaced by their ASCII base letter: ``"Café"`` -> ``"Cafe"``."""
    decomposed = unicodedata.normalize("NFKD", text)
    stripped = "".join(c for c in decomposed if unicodedata.combining(c) == 0 and unicodedata.category(c) != "Mn")
    return stripped.encode("ascii", "ignore").decode("ascii")
