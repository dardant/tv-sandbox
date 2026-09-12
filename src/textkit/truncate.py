"""Shorten text for previews and titles."""

from __future__ import annotations

#: Appended when text is shortened. Downstream consumers rely on three ASCII dots (see ci/test_contract.py).
ELLIPSIS = "..."


def truncate(text: str, width: int, *, ellipsis: str = ELLIPSIS) -> str:
    """``text`` shortened to ``width`` characters, marking the cut with ``ellipsis``.

    Text that already fits is returned unchanged.  The cut is placed at the
    last word boundary that keeps the result (including the ellipsis) within
    ``width``.  A single word longer than the available room is hard-cut.
    When ``width`` is too small to leave room for the ellipsis, the text is
    hard-cut to ``width`` without an ellipsis.
    """
    if width < 1:
        raise ValueError("width must be at least 1")
    if len(text) <= width:
        return text

    # Width too small to fit the ellipsis — hard-cut without marker.
    if width <= len(ellipsis):
        return text[:width]

    room = width - len(ellipsis)

    candidate = text[:room]

    # Determine the prefix, preferring a word-boundary cut.
    if room < len(text) and text[room] == " ":
        # The cut lands right before a space — we are at a word boundary.
        prefix = candidate.rstrip()
    elif candidate.endswith(" "):
        # The candidate itself ends with space(s) — clean word boundary.
        prefix = candidate.rstrip()
    else:
        # Try to find the last space so we don't cut mid-word.
        last_space = candidate.rfind(" ")
        if last_space > 0:
            prefix = candidate[:last_space].rstrip()
        else:
            # Single word longer than room — hard-cut.
            prefix = candidate

    return prefix + ellipsis
