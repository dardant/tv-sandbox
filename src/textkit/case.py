"""Change the case of titles and identifiers."""

from __future__ import annotations

import re

_WORD = re.compile(r"[A-Za-z0-9]+")
#: A lowercase letter or digit followed by an uppercase letter: the seam in ``orderTotal``.
_CAMEL_SEAM = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")


def _title_word(word: str) -> str:
    if len(word) == 1:
        return word.capitalize()
    if word.isupper():
        return word
    if word.islower():
        return word.capitalize()
    return word


def title_case(text: str) -> str:
    """Each word capitalized: ``"hello world"`` -> ``"Hello World"``."""
    return " ".join(_title_word(word) for word in text.split())


def snake_case(text: str) -> str:
    """An identifier in snake case: ``"orderTotal"`` and ``"Order Total"`` both become ``"order_total"``."""
    spaced = _CAMEL_SEAM.sub(" ", text)
    return "_".join(word.lower() for word in _WORD.findall(spaced))
