<!-- tandemvelocity:knowledge kind=story work-item=SCRUM-7 project=textkit -->

# SCRUM-7 — Fix title_case() lowercasing acronyms (SCRUM-7) (as built)

_What this change did, recorded by TandemVelocity before the change was captured as an immutable candidate. This is a record, not a contract: the approved requirements are in the specification it names below._

## Summary

title_case() applied str.capitalize() to every word, turning 'NASA launches new API' into 'Nasa Launches New Api'. Added per-word preservation: len>1 all-caps words stay as-is, all-lower words are capitalized, single-letter words are capitalized, and mixed-case words are preserved exactly. Added failing-first regression tests and a CHANGELOG Fixed entry. pytest -q: 76 passed; pytest -q ci: 4 passed unmodified.

## Implemented against

- specification: `_bmad-output/implementation-artifacts/SCRUM-7.spec.md`
- approved content digest: `b3debb2a17cac10701286ffa369f1eb8bc07fc6aff976d6abfa95ba8b2d108ce`
- plan approval: 58f770f3-5e1b-5d5f-9c56-7d95a4180cff

## Changes

- `src/textkit/case.py` (modified) — Add _title_word helper with len==1 capitalize, isupper preserve, islower capitalize, else preserve; use it in title_case to keep acronyms and mixed-case words.
- `tests/test_case.py` (modified) — Add regression tests for acronym preservation, single-letter capitalization, and mixed-case preservation next to existing title_case behaviour.
- `CHANGELOG.md` (modified) — Add Unreleased Fixed entry for title_case acronym/mixed-case preservation to satisfy changelog CI job.

## Plan tasks

Completed:
- reproduce-issue
- add-regression-tests
- fix-title-case
- update-changelog
- verify-tests

## Verification

Commands selected to prove the change:
- `pytest -q`
- `pytest -q ci`

Tests written or changed:
- `tests/test_case.py: test_title_case_preserves_acronyms`
- `tests/test_case.py: test_title_case_capitalizes_single_letter_word`
- `tests/test_case.py: test_title_case_preserves_mixed_case_word`
- `tests/test_case.py: test_title_case_preserves_acronym_with_trailing_punctuation`
- `tests/test_case.py: test_title_case_preserves_acronym_with_digits`
- `tests/test_case.py: test_title_case_preserves_apostrophe_mixed_case_word`
- `tests/test_case.py: test_title_case_capitalizes_single_letter_words_in_sentence`
- `tests/test_case.py: test_title_case_collapses_spaces_around_acronyms`
- `tests/test_case.py: test_title_case_leaves_already_titlecased_word_unchanged`

The authoritative result of running them is not recorded here: it is produced after this document exists, by a deterministic execution against the immutable candidate, and it lives in TandemVelocity as TestEvidence bound to that candidate.

## Provenance

- work item: jira:SCRUM-7
- project: textkit
- source revision: dardant/tv-sandbox@a9082d86713db6d10e41b459bc9b08305f510d02 (ref main)
- project context baseline: v1
- context pack: 01a09482-1886-75d3-8492-f6e473210ffe
- approved plan artifact: 01a09483-0719-75e6-8c47-b96986ad7f47 (content hash a0a8d0a3430e)
- produced by: TandemVelocity issue_to_change_request.v3, run 01a09482-08fc-7300-8bd1-b9a1fe29b069
