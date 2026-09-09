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
    assert slugify("") == ""


def test_single_allowed_character():
    assert slugify("a") == "a"


def test_single_disallowed_character():
    assert slugify("!") == ""


def test_only_whitespace_returns_empty():
    assert slugify("   ") == ""


def test_mixed_punctuation_and_spaces_collapse():
    """A run of mixed disallowed characters (spaces, punctuation) collapses to one hyphen."""
    assert slugify("hello ! @ # world") == "hello-world"


def test_leading_disallowed_stripped():
    """Disallowed characters at the start do not produce a leading hyphen."""
    assert slugify("---hello") == "hello"


def test_trailing_disallowed_stripped():
    """Disallowed characters at the end do not produce a trailing hyphen."""
    assert slugify("hello---") == "hello"


def test_hyphens_between_words_preserved_as_single():
    """Internal hyphens (which are disallowed) collapse to one and are kept."""
    assert slugify("one---two") == "one-two"


def test_digits_only():
    assert slugify("12345") == "12345"


def test_accented_with_surrounding_punctuation():
    """Accent folding combined with leading/trailing stripping."""
    assert slugify("  Café! ") == "cafe"


def test_multiple_words_with_varied_separators():
    assert slugify("a  b--c!!d") == "a-b-c-d"
