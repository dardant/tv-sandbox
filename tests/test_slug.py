from textkit import slugify


def test_lowercases_and_separates_words():
    assert slugify("Hello World") == "hello-world"


def test_folds_accents_to_ascii():
    assert slugify("Caf\u00e9 Menu") == "cafe-menu"


def test_keeps_digits():
    assert slugify("Top 10 Tips") == "top-10-tips"


def test_is_idempotent_on_an_already_clean_slug():
    assert slugify("hello-world") == "hello-world"


def test_collapses_consecutive_separators():
    assert slugify("Hello -- World!") == "hello-world"


def test_strips_leading_and_trailing_hyphens():
    assert slugify("  leading and trailing  ") == "leading-and-trailing"


def test_all_disallowed_returns_empty():
    assert slugify("!!!") == ""


# --- Additional edge-case tests for the separator-collapsing fix ---


def test_empty_string_returns_empty():
    """An empty input must produce an empty slug."""
    assert slugify("") == ""


def test_single_allowed_character():
    """A single allowed character needs no hyphens."""
    assert slugify("a") == "a"


def test_mixed_punctuation_between_words():
    """A run of varied punctuation between words collapses to one hyphen."""
    assert slugify("foo...bar") == "foo-bar"


def test_hyphens_only_returns_empty():
    """A string of only hyphens (disallowed-only) returns empty."""
    assert slugify("---") == ""


def test_single_disallowed_at_boundaries():
    """Leading and trailing single disallowed characters are stripped."""
    assert slugify("!hello!") == "hello"


def test_whitespace_and_punctuation_mix_collapses():
    """Mixed whitespace and punctuation between words collapses to one hyphen."""
    assert slugify("hello   !!!   world") == "hello-world"


def test_accented_with_surrounding_punctuation():
    """Accent folding combined with leading/trailing punctuation stripping."""
    assert slugify("**Café**") == "cafe"


def test_digits_only():
    """A string of only digits is fully allowed and returned as-is."""
    assert slugify("12345") == "12345"


def test_single_space_between_words():
    """A single space still produces exactly one hyphen (regression guard)."""
    assert slugify("one two three") == "one-two-three"


def test_tabs_and_newlines_collapse():
    """Tabs and newlines are disallowed and collapse like other separators."""
    assert slugify("hello\t\tworld\n\n") == "hello-world"


def test_trailing_punctuation_stripped():
    """Trailing punctuation does not leave a trailing hyphen."""
    assert slugify("Hello World!") == "hello-world"


def test_leading_punctuation_stripped():
    """Leading punctuation does not leave a leading hyphen."""
    assert slugify("...Hello") == "hello"
