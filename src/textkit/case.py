"""Change the case of titles and identifiers."""

from __future__ import annotations

import re

_WORD = re.compile(r"[A-Za-z0-9]+")
#: A lowercase letter or digit followed by an uppercase letter: the seam in ``orderTotal``.
_CAMEL_SEAM = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")


def _split_words(text: str) -> list[str]:
    """Split *text* into lowercased word tokens, recognising camelCase seams."""
    spaced = _CAMEL_SEAM.sub(" ", text)
    return [word.lower() for word in _WORD.findall(spaced)]


def title_case(text: str) -> str:
    """Each word capitalized: ``"hello world"`` -> ``"Hello World"``."""
    return " ".join(word.capitalize() for word in text.split())


def snake_case(text: str) -> str:
    """An identifier in snake case: ``"orderTotal"`` and ``"Order Total"`` both become ``"order_total"``."""
    return "_".join(_split_words(text))


def kebab_case(text: str) -> str:
    """An identifier in kebab case: ``"orderTotal"`` and ``"Order Total"`` both become ``"order-total"``."""
    return "-".join(_split_words(text))
