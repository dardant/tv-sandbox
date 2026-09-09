from textkit import slugify


def test_lowercases_and_separates_words():
    assert slugify("Hello World") == "hello-world"


def test_folds_accents_to_ascii():
    assert slugify("Caf\u00e9 Menu") == "cafe-menu"


def test_keeps_digits():
    assert slugify("Top 10 Tips") == "top-10-tips"


def test_is_idempotent_on_an_already_clean_slug():
    assert slugify("hello-world") == "hello-world"


def test_collapses_repeated_separators():
    assert slugify("Hello -- World!") == "hello-world"


def test_strips_leading_and_trailing_hyphens():
    assert slugify("  leading and trailing  ") == "leading-and-trailing"


def test_all_disallowed_returns_empty_string():
    assert slugify("!!!") == ""


# --- Additional edge-case tests ---


def test_empty_string_returns_empty():
    """An empty input should produce an empty slug."""
    assert slugify("") == ""


def test_single_allowed_character():
    """A single allowed character should pass through unchanged."""
    assert slugify("a") == "a"


def test_single_disallowed_character():
    """A single disallowed character should produce an empty string (stripped)."""
    assert slugify("!") == ""


def test_mixed_punctuation_and_spaces_collapse():
    """A mix of different disallowed characters in a row should collapse to one hyphen."""
    assert slugify("hello !@# world") == "hello-world"


def test_leading_disallowed_only():
    """Leading disallowed characters should be stripped, not produce a leading hyphen."""
    assert slugify("---hello") == "hello"


def test_trailing_disallowed_only():
    """Trailing disallowed characters should be stripped, not produce a trailing hyphen."""
    assert slugify("hello---") == "hello"


def test_multiple_words_with_varied_separators():
    """Multiple words separated by varied disallowed runs should each get one hyphen."""
    assert slugify("one  two---three!!!four") == "one-two-three-four"


def test_digits_only():
    """A string of only digits should pass through unchanged."""
    assert slugify("12345") == "12345"
