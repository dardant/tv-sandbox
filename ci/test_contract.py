"""Consumer contract for textkit.

Two downstream services depend on these exact behaviours: the CMS importer (hyphenated slugs, three-dot
ellipsis) and the file-naming service (the published function names). These tests run in CI only
(CONTRIBUTING.md, rule 4). A change that needs one of them edited is a breaking change and needs a decision from
the maintainers, not an edit here.
"""

from pathlib import Path

import textkit
from textkit import slugify, title_case, truncate


def test_public_api_is_exactly_the_published_surface():
    published = Path(__file__).with_name("public_api.txt").read_text(encoding="utf-8").split()
    assert sorted(textkit.__all__) == sorted(published)


def test_slug_words_are_separated_by_hyphens():
    assert slugify("Hello World") == "hello-world"


def test_truncation_is_marked_with_three_ascii_dots():
    assert truncate("The quick brown fox", 12).endswith("...")


def test_title_case_capitalizes_each_word():
    assert title_case("hello world") == "Hello World"
