from textkit import snake_case, title_case


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
