import pytest
from textkit import truncate


def test_returns_text_that_fits_unchanged():
    assert truncate("hello", 10) == "hello"


def test_marks_the_cut_with_an_ellipsis():
    assert truncate("hello world", 8).endswith("...")


def test_rejects_a_width_below_one():
    with pytest.raises(ValueError):
        truncate("hello", 0)
