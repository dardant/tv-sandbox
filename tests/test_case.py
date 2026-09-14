from textkit import snake_case, title_case


def test_title_case_capitalizes_each_word():
    assert title_case("hello world") == "Hello World"


def test_title_case_collapses_repeated_spaces():
    assert title_case("hello   world") == "Hello World"


def test_title_case_preserves_acronyms():
    assert title_case("NASA launches new API") == "NASA Launches New API"


def test_title_case_capitalizes_single_letter_word():
    assert title_case("a") == "A"


def test_title_case_preserves_mixed_case_word():
    assert title_case("iPhone") == "iPhone"


def test_title_case_preserves_acronym_with_trailing_punctuation():
    assert title_case("new API, today") == "New API, Today"


def test_title_case_preserves_acronym_with_digits():
    assert title_case("NASA2 launches") == "NASA2 Launches"


def test_title_case_preserves_apostrophe_mixed_case_word():
    assert title_case("NASA's launch") == "NASA's Launch"


def test_title_case_capitalizes_single_letter_words_in_sentence():
    assert title_case("a tale of a whale") == "A Tale Of A Whale"


def test_title_case_collapses_spaces_around_acronyms():
    assert title_case("NASA   launches  new   API") == "NASA Launches New API"


def test_title_case_leaves_already_titlecased_word_unchanged():
    assert title_case("Launches") == "Launches"


def test_title_case_capitalizes_quoted_word():
    assert title_case('"hello world" said the fox') == '"Hello World" Said The Fox'


def test_title_case_capitalizes_bracketed_word():
    assert title_case("(hello) world") == "(Hello) World"


def test_title_case_leaves_empty_string_unchanged():
    assert title_case("") == ""


def test_title_case_leaves_punctuation_only_token_unchanged():
    assert title_case("...") == "..."
    assert title_case('"""') == '"""'


def test_title_case_capitalizes_quoted_single_letter_word():
    assert title_case('"a" test') == '"A" Test'


def test_title_case_preserves_quoted_acronym():
    assert title_case('"NASA launches') == '"NASA Launches'


def test_title_case_preserves_mixed_case_after_leading_punctuation():
    assert title_case('"iPhone" case') == '"iPhone" Case'
    assert title_case("(NASA) launches") == "(NASA) Launches"


def test_snake_case_splits_camel_case():
    assert snake_case("orderTotal") == "order_total"


def test_snake_case_joins_words():
    assert snake_case("Order Total") == "order_total"


def test_snake_case_keeps_digits_attached_to_their_word():
    assert snake_case("version2Update") == "version2_update"
