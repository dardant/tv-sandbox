"""Whitespace and accent normalisation shared by the other modules."""

from __future__ import annotations

import re
import unicodedata

_SPACES = re.compile(r" +")


def collapse_whitespace(text: str) -> str:
    """Runs of spaces collapsed to one, with both ends trimmed."""
    return _SPACES.sub(" ", text).strip(" ")


def fold_accents(text: str) -> str:
    """Accented letters replaced by their ASCII base letter: ``"Café"`` -> ``"Cafe"``."""
    return unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
