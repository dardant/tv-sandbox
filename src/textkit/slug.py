"""Turn a human title into a URL slug."""

import re
import unicodedata

#: Every character a slug may not contain. Replaced one for one, which is why runs of punctuation currently
#: survive as runs of hyphens.
_NOT_ALLOWED = re.compile(r"[^a-z0-9]")


def slugify(text: str) -> str:
    """A lowercase, hyphen-separated slug of ``text``.

    Accents are folded to their ASCII base letter, so "Cafe\u0301" and "Cafe" produce the same slug.
    """
    folded = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    return _NOT_ALLOWED.sub("-", folded.lower())
