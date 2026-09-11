"""A very small text toolkit."""

from textkit.case import kebab_case, snake_case, title_case
from textkit.normalize import collapse_whitespace, fold_accents
from textkit.slug import slugify
from textkit.truncate import truncate

__all__ = ["collapse_whitespace", "fold_accents", "kebab_case", "slugify", "snake_case", "title_case", "truncate"]
