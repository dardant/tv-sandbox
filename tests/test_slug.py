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


# --- Additional edge-case tests for the collapsing / stripping fix ---


def test_empty_string_returns_empty():
    """An empty input should produce an empty slug."""
    assert slugify("") == ""


def test_single_allowed_character():
    """A single alphanumeric character should pass through unchanged."""
    assert slugify("a") == "a"
    assert slugify("5") == "5"


def test_single_disallowed_character():
    """A single disallowed character should produce an empty string (stripped)."""
    assert slugify("!") == ""
    assert slugify(" ") == ""


def test_mixed_punctuation_and_spaces_collapse():
    """Various disallowed characters between words collapse to one hyphen."""
    assert slugify("foo  ...  bar") == "foo-bar"
    assert slugify("a!@#$%^&*b") == "a-b"


def test_leading_disallowed_with_collapse():
    """Leading disallowed characters are collapsed and then stripped."""
    assert slugify("!!!hello") == "hello"
    assert slugify("   hello") == "hello"


def test_trailing_disallowed_with_collapse():
    """Trailing disallowed characters are collapsed and then stripped."""
    assert slugify("hello!!!") == "hello"
    assert slugify("hello   ") == "hello"


def test_only_whitespace_returns_empty():
    """A string of only whitespace should produce an empty slug."""
    assert slugify("     ") == ""
