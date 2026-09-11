"""Turn a human title into a URL slug."""

import re
import unicodedata

#: One or more characters a slug may not contain, collapsed into a single hyphen.
_NOT_ALLOWED = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    """A lowercase, hyphen-separated slug of ``text``.

    Accents are folded to their ASCII base letter, so "Cafe\u0301" and "Cafe" produce the same slug.
    """
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return _NOT_ALLOWED.sub("-", folded.lower()).strip("-")
