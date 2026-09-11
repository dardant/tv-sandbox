from __future__ import annotations

import pytest

from textkit import slugify


# --- existing tests (unchanged) ---


def test_lowercases_and_separates_words():
    assert slugify("Hello World") == "hello-world"


def test_folds_accents_to_ascii():
    assert slugify("Café Menu") == "cafe-menu"


def test_keeps_digits():
    assert slugify("Top 10 Tips") == "top-10-tips"


def test_is_idempotent_on_an_already_clean_slug():
    assert slugify("hello-world") == "hello-world"


# --- max_length: no truncation needed ---


def test_max_length_none_returns_full_slug():
    assert slugify("Hello World") == "hello-world"


def test_max_length_larger_than_slug_returns_full_slug():
    assert slugify("Hello World", max_length=100) == "hello-world"


def test_max_length_equal_to_slug_length_returns_full_slug():
    assert slugify("Hello World", max_length=11) == "hello-world"


# --- max_length: truncation at hyphen boundary ---


def test_max_length_truncates_at_last_hyphen():
    assert slugify("Hello World", max_length=7) == "hello"


def test_max_length_truncates_long_title_at_boundary():
    # "designing-resilient-systems-for-real-people" is 43 chars
    result = slugify("Designing resilient systems for real people", max_length=20)
    assert len(result) <= 20
    assert result == "designing-resilient"


def test_max_length_truncates_at_60_for_cms():
    title = "Designing resilient systems for real people in a complex world of technology"
    result = slugify(title, max_length=60)
    assert len(result) <= 60
    assert not result.endswith("-")


# --- max_length: hard cut when no hyphen available ---


def test_max_length_hard_cuts_single_long_word():
    assert slugify("abcdefghij", max_length=5) == "abcde"


# --- max_length: trailing hyphen stripping ---


def test_max_length_strips_trailing_hyphens():
    # "hello--world" (punctuation run) — cutting at 6 gives "hello-", which should strip to "hello"
    assert slugify("hello  world", max_length=6) == "hello"


def test_max_length_strips_multiple_trailing_hyphens():
    # Input with consecutive spaces produces consecutive hyphens
    result = slugify("a    b", max_length=4)
    assert not result.endswith("-")


# --- max_length: edge cases ---


def test_max_length_one():
    result = slugify("Hello World", max_length=1)
    assert len(result) <= 1


def test_max_length_zero_raises_value_error():
    with pytest.raises(ValueError):
        slugify("Hello World", max_length=0)


def test_max_length_negative_raises_value_error():
    with pytest.raises(ValueError):
        slugify("Hello World", max_length=-5)


# --- additional acceptance-criteria tests ---


class TestMaxLengthKeywordOnly:
    """max_length must be keyword-only; passing it positionally is a TypeError."""

    def test_max_length_cannot_be_passed_positionally(self):
        with pytest.raises(TypeError):
            slugify("Hello World", 7)  # type: ignore[misc]


class TestBackwardCompatibility:
    """When max_length is omitted the output is byte-for-byte identical to the
    original slugify — no existing slugs are broken."""

    def test_long_title_without_max_length_is_not_truncated(self):
        title = "A" + " very" * 30  # produces a slug well over 120 chars
        result = slugify(title)
        # The full slug must be returned; nothing is silently capped.
        assert len(result) > 60

    def test_accented_text_without_max_length_unchanged(self):
        assert slugify("Café Résumé Naïve") == "cafe-resume-naive"

    def test_consecutive_punctuation_preserved_without_max_length(self):
        # Runs of non-allowed chars become runs of hyphens (documented behaviour).
        result = slugify("hello!!!world")
        assert "---" in result  # consecutive hyphens survive


class TestMaxLengthInvariant:
    """The result must never exceed max_length, regardless of input."""

    CASES = [
        ("Hello World", 5),
        ("Hello World", 6),
        ("Hello World", 11),
        ("Hello World", 12),
        ("Designing resilient systems for real people", 1),
        ("Designing resilient systems for real people", 10),
        ("Designing resilient systems for real people", 20),
        ("Designing resilient systems for real people", 43),
        ("Designing resilient systems for real people", 60),
        ("abcdefghijklmnopqrstuvwxyz", 13),
        ("a    b    c", 3),
        ("Héllo Wörld Café", 8),
    ]

    @pytest.mark.parametrize("text,limit", CASES)
    def test_result_never_exceeds_max_length(self, text: str, limit: int):
        result = slugify(text, max_length=limit)
        assert len(result) <= limit

    @pytest.mark.parametrize("text,limit", CASES)
    def test_result_never_ends_with_hyphen(self, text: str, limit: int):
        result = slugify(text, max_length=limit)
        if result:  # empty is acceptable for extreme edge cases
            assert not result.endswith("-")


class TestCMSScenario:
    """Real-world scenario: the CMS rejects slugs > 60 characters."""

    def test_120_char_slug_capped_to_60(self):
        # Build a title whose slug is well over 120 characters.
        title = (
            "Understanding the Fundamental Principles of Distributed "
            "Systems Architecture in Modern Cloud Computing Environments"
        )
        full_slug = slugify(title)
        assert len(full_slug) > 60, "precondition: slug must exceed 60 chars"

        capped = slugify(title, max_length=60)
        assert len(capped) <= 60
        assert not capped.endswith("-")
        # The capped slug must be a prefix of the full slug (at a word boundary).
        assert full_slug.startswith(capped) or full_slug.startswith(capped.rstrip("-"))

    def test_short_title_unaffected_by_60_cap(self):
        result = slugify("Short Title", max_length=60)
        assert result == "short-title"


class TestAccentsWithMaxLength:
    """Accent folding happens before truncation, so max_length counts ASCII chars."""

    def test_accented_title_truncated_correctly(self):
        result = slugify("Café Résumé Naïve Über", max_length=15)
        assert len(result) <= 15
        assert not result.endswith("-")

    def test_accented_title_exact_fit(self):
        # "cafe-resume" is 11 chars
        result = slugify("Café Résumé", max_length=11)
        assert result == "cafe-resume"


class TestMaxLengthCutAtHyphenPosition:
    """When max_length falls exactly on a hyphen, the hyphen should be stripped."""

    def test_cut_exactly_at_hyphen(self):
        # "hello-world" — max_length=6 means truncated="hello-", should become "hello"
        result = slugify("Hello World", max_length=6)
        assert result == "hello"
        assert not result.endswith("-")

    def test_cut_one_past_hyphen(self):
        # "hello-world" — max_length=7 means truncated="hello-w", last hyphen at 5 → "hello"
        result = slugify("Hello World", max_length=7)
        assert result == "hello"


class TestMaxLengthEdgeCases:
    """Additional edge cases for robustness."""

    def test_max_length_one_returns_single_char(self):
        result = slugify("Hello World", max_length=1)
        assert result == "h"

    def test_max_length_equals_first_word_length(self):
        # "hello-world" — first word is 5 chars
        result = slugify("Hello World", max_length=5)
        assert result == "hello"

    def test_digits_in_slug_with_max_length(self):
        result = slugify("Top 10 Tips for 2025", max_length=10)
        assert len(result) <= 10
        assert not result.endswith("-")

    def test_already_clean_slug_with_max_length(self):
        result = slugify("hello-world", max_length=7)
        assert result == "hello"

    def test_value_error_message_includes_value(self):
        with pytest.raises(ValueError, match="0"):
            slugify("Hello", max_length=0)

    def test_value_error_message_includes_negative_value(self):
        with pytest.raises(ValueError, match="-10"):
            slugify("Hello", max_length=-10)
