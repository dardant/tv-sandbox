# Changelog

Every change adds a line under **Unreleased** (CONTRIBUTING.md, rule 1). CI refuses a branch that does not.

## Unreleased

### Fixed
- `slugify` now collapses consecutive disallowed characters into a single hyphen and strips leading/trailing hyphens.
- `truncate` now respects the `width` budget (result including ellipsis is never longer than `width`) and cuts at word boundaries instead of mid-word.
- `title_case` now preserves all-caps acronyms and mixed-case words instead of lowercasing them.
- `collapse_whitespace` now collapses all whitespace (tabs, newlines, U+00A0) to a single space and trims ends.

## 0.3.0 - 2026-09-11

### Added
- `truncate`, `title_case`, `snake_case`, `collapse_whitespace` and `fold_accents`.
- Consumer contract tests in `ci/`, run by CI only.

## 0.2.0

### Added
- `slugify` folds accents to their ASCII base letter.
