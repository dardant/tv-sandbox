import pytest
from textkit import truncate


def test_returns_text_that_fits_unchanged():
    assert truncate("hello", 10) == "hello"


def test_marks_the_cut_with_an_ellipsis():
    assert truncate("hello world", 8).endswith("...")


def test_rejects_a_width_below_one():
    with pytest.raises(ValueError):
        truncate("hello", 0)


# --- Regression tests for SCRUM-6 ---


def test_result_never_exceeds_width():
    """The returned string, including the ellipsis, must fit within width."""
    result = truncate("Designing resilient systems for real people", 20)
    assert len(result) <= 20


def test_cuts_at_word_boundary():
    """The cut should land at a word boundary, not mid-word."""
    result = truncate("Designing resilient systems for real people", 20)
    # room = 17, text[:17] = "Designing resilien", last space at 9
    # prefix = "Designing", result = "Designing..."
    assert result == "Designing..."


def test_hard_cuts_single_long_word():
    """A single word longer than the available room is hard-cut."""
    result = truncate("abcdefghijklmnop", 8)
    assert result == "abcde..."
    assert len(result) == 8


def test_exact_fit_returned_unchanged():
    """Text whose length equals width is returned unchanged."""
    assert truncate("hello", 5) == "hello"


def test_width_too_small_for_ellipsis():
    """When width < len(ellipsis), return a hard-cut without ellipsis."""
    assert truncate("hello", 2) == "he"
    assert len(truncate("hello", 2)) == 2


def test_width_equals_ellipsis_length():
    """When width == len(ellipsis), return a hard-cut without ellipsis."""
    assert truncate("hello world", 3) == "hel"
    assert len(truncate("hello world", 3)) == 3


def test_reproduces_issue_example():
    """Reproduce the exact example from the bug report."""
    result = truncate("Designing resilient systems for real people", 20)
    assert len(result) <= 20
    # Must not contain a partial word before the ellipsis
    prefix = result.removesuffix("...")
    assert not prefix.endswith(" ")


def test_no_trailing_spaces_before_ellipsis():
    """No trailing spaces should appear between the text and the ellipsis."""
    result = truncate("hello   world foo bar", 12)
    prefix = result.removesuffix("...")
    assert not prefix.endswith(" ")


def test_word_boundary_at_exact_room():
    """When the character right after room is a space, cut cleanly there."""
    # "The quick brown fox", width=12 → room=9, text[:9]="The quick", text[9]=" "
    result = truncate("The quick brown fox", 12)
    assert result == "The quick..."
    assert len(result) == 12


def test_width_of_one():
    """Width of 1 should return a single character."""
    assert truncate("hello", 1) == "h"
    assert len(truncate("hello", 1)) == 1


def test_multiple_spaces_between_words():
    """Multiple spaces between words should still find a word boundary."""
    result = truncate("hello    world", 10)
    assert len(result) <= 10
    assert result.endswith("...")


# --- Additional acceptance-criteria tests (test agent, SCRUM-6) ---


@pytest.mark.parametrize(
    "text, width",
    [
        ("Designing resilient systems for real people", 20),
        ("Designing resilient systems for real people", 40),
        ("Designing resilient systems for real people", 10),
        ("Designing resilient systems for real people", 5),
        ("Designing resilient systems for real people", 3),
        ("Designing resilient systems for real people", 1),
        ("hello world", 8),
        ("hello world", 4),
        ("hello world", 11),
        ("hello world", 12),
        ("abcdefghijklmnop", 8),
        ("abcdefghijklmnop", 4),
        ("abcdefghijklmnop", 1),
        ("The quick brown fox", 12),
        ("The quick brown fox", 19),
        ("The quick brown fox", 7),
        ("a b c d e f", 6),
        ("a b c d e f", 4),
        ("short", 100),
        ("x", 1),
        ("hello   world   foo   bar", 15),
        ("hello   world   foo   bar", 10),
        ("hello   world   foo   bar", 5),
    ],
    ids=lambda v: repr(v),
)
def test_width_invariant_parametrized(text, width):
    """Core invariant: len(result) <= width for all valid inputs."""
    result = truncate(text, width)
    assert len(result) <= width


def test_hello_world_width_8_exact_value():
    """Plan acceptance criterion: truncate('hello world', 8) returns 'hello...'."""
    result = truncate("hello world", 8)
    assert result == "hello..."
    assert len(result) == 8


def test_no_mid_word_cut_like_resil():
    """Bug report: must NOT produce 'Designing resil...' or similar mid-word cut."""
    result = truncate("Designing resilient systems for real people", 20)
    # The prefix before the ellipsis must be a complete word
    prefix = result.removesuffix("...")
    # "resil", "resilie", "resilien" etc. would indicate a mid-word cut
    assert "resil" not in prefix


def test_negative_width_raises():
    """Negative width should raise ValueError just like zero."""
    with pytest.raises(ValueError):
        truncate("hello", -1)
    with pytest.raises(ValueError):
        truncate("hello", -100)


def test_empty_string_returned_unchanged():
    """Empty string always fits any valid width."""
    assert truncate("", 1) == ""
    assert truncate("", 10) == ""


def test_text_one_char_longer_than_width():
    """Text that is exactly one character longer than width must be truncated."""
    # "hello!" is 6 chars, width=5 → room=2, candidate="he", no space → hard cut
    result = truncate("hello!", 5)
    assert len(result) <= 5
    assert result == "he..."


def test_width_just_above_ellipsis_length():
    """Width=4 gives room=1, just enough for one char + ellipsis."""
    result = truncate("hello world", 4)
    assert result == "h..."
    assert len(result) == 4


def test_custom_ellipsis_respects_width():
    """Custom ellipsis marker should also respect the width budget."""
    result = truncate("hello world", 8, ellipsis="…")
    assert len(result) <= 8
    assert result.endswith("…")


def test_contract_compatible_truncation():
    """Verify the exact contract test scenario produces the right result.

    The contract test checks: truncate('The quick brown fox', 12).endswith('...')
    We verify both the endswith and the exact value for full confidence.
    """
    result = truncate("The quick brown fox", 12)
    assert result.endswith("...")
    assert result == "The quick..."
    assert len(result) == 12


def test_ellipsis_marker_is_three_ascii_dots():
    """The ELLIPSIS constant must be three ASCII dots (CMS importer dependency)."""
    from textkit.truncate import ELLIPSIS
    assert ELLIPSIS == "..."
    assert len(ELLIPSIS) == 3


# --- Regression tests for SCRUM-24 ---


def test_tab_is_a_word_boundary():
    """A tab counts as a word boundary, so the cut lands before it."""
    result = truncate("Designing\tresilient systems", 20)
    assert result == "Designing..."
    assert len(result) <= 20


def test_non_breaking_space_is_a_word_boundary():
    """A non-breaking space counts as a word boundary, so the cut lands before it."""
    result = truncate("Designing resilient systems", 20)
    assert result == "Designing..."
    assert len(result) <= 20
