import textkit
from textkit import kebab_case, snake_case, title_case


def test_title_case_capitalizes_each_word():
    assert title_case("hello world") == "Hello World"


def test_title_case_collapses_repeated_spaces():
    assert title_case("hello   world") == "Hello World"


def test_snake_case_splits_camel_case():
    assert snake_case("orderTotal") == "order_total"


def test_snake_case_joins_words():
    assert snake_case("Order Total") == "order_total"


def test_snake_case_keeps_digits_attached_to_their_word():
    assert snake_case("version2Update") == "version2_update"


def test_kebab_case_splits_camel_case():
    assert kebab_case("orderTotal") == "order-total"


def test_kebab_case_joins_words():
    assert kebab_case("Order Total") == "order-total"


def test_kebab_case_keeps_digits_attached_to_their_word():
    assert kebab_case("version2Update") == "version2-update"


# --- kebab_case and snake_case parity ---

def test_kebab_case_and_snake_case_split_words_identically():
    """kebab_case and snake_case must use the same word splitting; only the separator differs."""
    samples = [
        "orderTotal",
        "Order Total",
        "version2Update",
        "HTMLParser",
        "getHTTPResponse",
        "simple",
        "already_snake",
        "already-kebab",
        "MixedCASE Words",
        "  extra   spaces  ",
    ]
    for text in samples:
        assert kebab_case(text) == snake_case(text).replace("_", "-"), (
            f"Parity broken for {text!r}"
        )


# --- kebab_case edge cases ---

def test_kebab_case_single_word():
    assert kebab_case("hello") == "hello"


def test_kebab_case_single_uppercase_word():
    assert kebab_case("HELLO") == "hello"


def test_kebab_case_empty_string():
    assert kebab_case("") == ""


def test_kebab_case_strips_punctuation():
    """Non-alphanumeric characters are dropped (same as snake_case)."""
    assert kebab_case("hello, world!") == "hello-world"


def test_kebab_case_handles_underscored_input():
    """Input already in snake_case should be converted to kebab-case."""
    assert kebab_case("order_total") == "order-total"


def test_kebab_case_multiple_uppercase_run():
    """Consecutive uppercase letters (acronyms) are treated as one word."""
    assert kebab_case("HTMLParser") == "htmlparser"


# --- public API ---

def test_kebab_case_is_in_all():
    assert "kebab_case" in textkit.__all__


def test_kebab_case_importable_from_textkit():
    assert callable(textkit.kebab_case)
