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

    room = width - len(ellipsis)

    # Width too small to fit any ellipsis — hard-cut without marker.
    if room < 1:
        return text[:width]

    candidate = text[:room]

    # Determine the prefix, preferring a word-boundary cut.
    if room < len(text) and text[room].isspace():
        # The cut lands right before whitespace — we are at a word boundary.
        prefix = candidate.rstrip()
    elif candidate and candidate[-1].isspace():
        # The candidate itself ends with whitespace — clean word boundary.
        prefix = candidate.rstrip()
    else:
        # Try to find the last whitespace so we don't cut mid-word.
        last_ws = -1
        for i, ch in enumerate(candidate):
            if ch.isspace():
                last_ws = i
        if last_ws > 0:
            prefix = candidate[:last_ws].rstrip()
        else:
            # Single word longer than room — hard-cut.
            prefix = candidate

    return prefix + ellipsis
