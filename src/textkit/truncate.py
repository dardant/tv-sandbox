"""Shorten text for previews and titles."""

from __future__ import annotations

#: Appended when text is shortened. Downstream consumers rely on three ASCII dots (see ci/test_contract.py).
ELLIPSIS = "..."


def truncate(text: str, width: int, *, ellipsis: str = ELLIPSIS) -> str:
    """``text`` shortened to ``width`` characters, marking the cut with ``ellipsis``.

    Text that already fits is returned unchanged.
    """
    if width < 1:
        raise ValueError("width must be at least 1")
    if len(text) <= width:
        return text
    return text[:width] + ellipsis
