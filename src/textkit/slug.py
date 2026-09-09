"""Turn a human title into a URL slug."""

import re
import unicodedata

#: One or more consecutive characters a slug may not contain. Matched as a single run so that re.sub
#: replaces the entire sequence with one hyphen, collapsing repeated separators.
_NOT_ALLOWED = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """A lowercase, hyphen-separated slug of ``text``.

    Accents are folded to their ASCII base letter, so "Cafe\u0301" and "Cafe" produce the same slug.
    """
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return _NOT_ALLOWED.sub("-", folded.lower()).strip("-")
