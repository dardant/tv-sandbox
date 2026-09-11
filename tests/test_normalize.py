from textkit import collapse_whitespace, fold_accents


def test_collapses_runs_of_spaces():
    assert collapse_whitespace("a   b  c") == "a b c"


def test_trims_both_ends():
    assert collapse_whitespace("  a b  ") == "a b"


def test_folds_accents():
    assert fold_accents("Café crème") == "Cafe creme"
