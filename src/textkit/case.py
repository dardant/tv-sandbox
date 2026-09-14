"""Change the case of titles and identifiers."""

from __future__ import annotations

import re

_WORD = re.compile(r"[A-Za-z0-9]+")
#: A lowercase letter or digit followed by an uppercase letter: the seam in ``orderTotal``.
_CAMEL_SEAM = re.compile(r"(?<=[a-z0-9])(?=[A-Z])")


def _title_word(word: str) -> str:
    prefix_end = 0
    while prefix_end < len(word) and not word[prefix_end].isalnum():
        prefix_end += 1
    prefix = word[:prefix_end]
    rest = word[prefix_end:]
    if not rest:
        return word
    if len(rest) == 1:
        return prefix + rest.capitalize()
    if rest.isupper():
        return word
    if rest.islower():
        return prefix + rest.capitalize()
    return word


def title_case(text: str) -> str:
    """Each word capitalized: ``"hello world"`` -> ``"Hello World"``."""
    return " ".join(_title_word(word) for word in text.split())


def snake_case(text: str) -> str:
    """An identifier in snake case: ``"orderTotal"`` and ``"Order Total"`` both become ``"order_total"``."""
    spaced = _CAMEL_SEAM.sub(" ", text)
    return "_".join(word.lower() for word in _WORD.findall(spaced))
