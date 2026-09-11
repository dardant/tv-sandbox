"""Turn a human title into a URL slug."""

from __future__ import annotations

import re
import unicodedata

#: Every character a slug may not contain. Replaced one for one, which is why runs of punctuation currently
#: survive as runs of hyphens.
_NOT_ALLOWED = re.compile(r"[^a-z0-9]")


def slugify(text: str, *, max_length: int | None = None) -> str:
    """A lowercase, hyphen-separated slug of ``text``.

    Accents are folded to their ASCII base letter, so "Café" and "Cafe" produce the same slug.

    When *max_length* is given the slug is truncated to at most that many
    characters.  The cut is made at the last hyphen boundary so that words
    are not split, unless the first segment is already longer than
    *max_length*, in which case a hard cut is applied.  Trailing hyphens
    are stripped after truncation.

    Raises ``ValueError`` if *max_length* is less than 1.
    """
    if max_length is not None and max_length < 1:
        raise ValueError(f"max_length must be at least 1, got {max_length}")

    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    slug = _NOT_ALLOWED.sub("-", folded.lower())

    if max_length is not None and len(slug) > max_length:
        truncated = slug[:max_length]
        # Try to cut at the last hyphen to preserve word boundaries.
        last_hyphen = truncated.rfind("-")
        if last_hyphen > 0:
            truncated = truncated[:last_hyphen]
        # Strip any trailing hyphens left over from the cut.
        slug = truncated.rstrip("-")

    return slug
