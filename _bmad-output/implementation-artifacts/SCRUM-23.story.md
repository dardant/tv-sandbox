<!-- tandemvelocity:knowledge kind=story work-item=SCRUM-23 project=textkit -->

# SCRUM-23 — Fix title_case() leading punctuation capitalization (SCRUM-23) (as built)

_What this change did, recorded by TandemVelocity before the change was captured as an immutable candidate. This is a record, not a contract: the approved requirements are in the specification it names below._

## Summary

Fixes jira:SCRUM-23: _title_word() in src/textkit/case.py now isolates leading non-alphanumeric punctuation and applies existing acronym/mixed-case logic to the remainder, so '"hello' -> '"Hello' and '(hello)' -> '(Hello)' while preserving NASA/API/iPhone/NASA's behavior. Adds quoted-word and bracketed-word regression tests in tests/test_case.py and a CHANGELOG.md Fixed entry. Verified with pytest -q (90 passed) and pytest -q ci (4 passed) unmodified.

## Implemented against

- specification: `_bmad-output/implementation-artifacts/SCRUM-23.spec.md`
- approved content digest: `8a8076dda6926061e487d3c6436b193a0ced1dc25fd1a39a6f37a232c62b9218`
- plan approval: bc9ae283-c8b8-58c3-acb9-65d08668e9e4

## Changes

- `src/textkit/case.py` (modified) — Isolate leading non-alphanumeric prefix in _title_word() and apply existing single-char/isupper/islower/mixed branches to remainder, then reattach prefix. Fixes quoted/bracketed capitalization while preserving acronyms and mixed-case tails.
- `tests/test_case.py` (modified) — Add the two requested regression tests: quoted leading word and bracketed leading word, which fail before the fix per CONTRIBUTING rule 5.
- `CHANGELOG.md` (modified) — Record fix under Unreleased Fixed per CONTRIBUTING rule 1 to satisfy changelog CI job.

## Plan tasks

Completed:
- reproduce-issue
- add-regression-tests
- fix-title-word
- update-changelog
- verify-suite

## Verification

Commands selected to prove the change:
- `pytest -q`
- `pytest -q ci`

Tests written or changed:
- `tests/test_case.py::test_title_case_capitalizes_quoted_word`
- `tests/test_case.py::test_title_case_capitalizes_bracketed_word`
- `tests/test_case.py::test_title_case_leaves_empty_string_unchanged`
- `tests/test_case.py::test_title_case_leaves_punctuation_only_token_unchanged`
- `tests/test_case.py::test_title_case_capitalizes_quoted_single_letter_word`
- `tests/test_case.py::test_title_case_preserves_quoted_acronym`
- `tests/test_case.py::test_title_case_preserves_mixed_case_after_leading_punctuation`

The authoritative result of running them is not recorded here: it is produced after this document exists, by a deterministic execution against the immutable candidate, and it lives in TandemVelocity as TestEvidence bound to that candidate.

## Provenance

- work item: jira:SCRUM-23
- project: textkit
- source revision: dardant/tv-sandbox@ca088206a7191df6fdadbb5b726b147777059c96 (ref main)
- project context baseline: v7
- context pack: 01a0a1cf-9b60-7068-9fc1-4bf20a3c1788
- approved plan artifact: 01a0a1d0-ce2e-772e-9bb3-a84e251cde41 (content hash 6dbb0428c882)
- produced by: TandemVelocity issue_to_change_request.v3, run 01a0a1cf-97e1-70df-a4d8-ae7e9e1604b9
