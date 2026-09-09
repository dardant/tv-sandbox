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


# ── Additional edge-case tests for SCRUM-5 acceptance criteria ──


def test_empty_string_returns_empty():
    """An empty input must produce an empty slug, not a hyphen."""
    assert slugify("") == ""


def test_single_allowed_character():
    """A single allowed character should pass through unchanged."""
    assert slugify("a") == "a"


def test_single_disallowed_character():
    """A single disallowed character should produce an empty string (stripped)."""
    assert slugify("!") == ""


def test_mixed_punctuation_run_collapses():
    """A run of different disallowed characters collapses to one hyphen."""
    assert slugify("a!@#$%b") == "a-b"


def test_spaces_and_punctuation_mixed():
    """Spaces interleaved with punctuation still collapse to one hyphen."""
    assert slugify("foo  --  bar") == "foo-bar"


def test_leading_disallowed_only():
    """Leading disallowed characters are stripped, not left as a hyphen."""
    assert slugify("---hello") == "hello"


def test_trailing_disallowed_only():
    """Trailing disallowed characters are stripped."""
    assert slugify("hello---") == "hello"


def test_all_spaces_returns_empty():
    """A string of only spaces should produce an empty string."""
    assert slugify("     ") == ""


def test_digits_only():
    """A string of only digits should pass through unchanged."""
    assert slugify("12345") == "12345"


def test_accent_with_surrounding_punctuation():
    """Accented characters with surrounding punctuation collapse correctly."""
    assert slugify("**Caf\u00e9**") == "cafe"


def test_signature_unchanged():
    """slugify() still accepts a single str argument and returns str."""
    result = slugify("test")
    assert isinstance(result, str)
