import unicodedata

from textkit import collapse_whitespace, fold_accents


def test_collapses_runs_of_spaces():
    assert collapse_whitespace("a   b  c") == "a b c"


def test_trims_both_ends():
    assert collapse_whitespace("  a b  ") == "a b"


def test_collapses_tabs_and_newlines():
    assert collapse_whitespace("Breaking\tnews\n today") == "Breaking news today"


def test_collapses_crlf_and_mixed_runs():
    assert collapse_whitespace("a\t\n b") == "a b"
    assert collapse_whitespace("a \t\n b") == "a b"
    assert collapse_whitespace("a\r\nb") == "a b"


def test_collapses_non_breaking_spaces():
    assert collapse_whitespace("\xa0a\xa0\xa0b\xa0") == "a b"


def test_trims_all_whitespace_kinds():
    assert collapse_whitespace(" \t\n\xa0a b\xa0\n\t ") == "a b"


def test_whitespace_only_collapses_to_empty():
    assert collapse_whitespace("") == ""
    assert collapse_whitespace("   ") == ""
    assert collapse_whitespace(" \t\n\r\xa0 ") == ""
    assert collapse_whitespace("\xa0") == ""


def test_collapses_other_ascii_whitespace():
    assert collapse_whitespace("a\vb") == "a b"
    assert collapse_whitespace("a\fb") == "a b"
    assert collapse_whitespace("a\rb") == "a b"


def test_folds_accents():
    assert fold_accents("Café crème") == "Cafe creme"


def test_folds_accents_for_composed_and_decomposed_input():
    composed = unicodedata.normalize("NFC", "café")
    decomposed = unicodedata.normalize("NFD", "café")
    assert len(decomposed) == 5
    for form in (composed, decomposed):
        result = fold_accents(form)
        assert result == "cafe"
        assert len(result) == 4
        assert all(unicodedata.combining(c) == 0 for c in result)
        assert all(unicodedata.category(c) != "Mn" for c in result)
