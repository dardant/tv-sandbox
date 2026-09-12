<!-- tandemvelocity:knowledge kind=story work-item=SCRUM-11 project=textkit -->

# SCRUM-11 — Fix collapse_whitespace() to collapse all whitespace (SCRUM-11) (as built)

_What this change did, recorded by TandemVelocity before the change was captured as an immutable candidate. This is a record, not a contract: the approved requirements are in the specification it names below._

## Summary

Fixed collapse_whitespace() in src/textkit/normalize.py to collapse any run of whitespace (spaces, tabs, newlines, U+00A0) to a single space and trim leading/trailing whitespace of any kind. Changed regex from ASCII-only ` +` plus `strip(" ")` to `\s+` plus `strip()`, updated docstring, added failing-first regression tests, and recorded the fix in CHANGELOG.md. Verified `pytest -q` (86 passed) and `pytest -q ci` (4 passed) with no contract or public API changes.

## Implemented against

- specification: `_bmad-output/implementation-artifacts/SCRUM-11.spec.md`
- approved content digest: `f252c337577c1330bceb41ea3f5e21129abfe17139d8a2dd2577a0ba5aad8fbc`
- plan approval: 215058e4-c777-5f27-b344-a63d9e574bd0

## Changes

- `src/textkit/normalize.py` (modified) — Core fix: _SPACES from ` +` to `\s+` and `strip(" ")` to `strip()` so tabs, newlines, CRLF and U+00A0 collapse to one space and trim; docstring updated from spaces to whitespace.
- `tests/test_normalize.py` (modified) — Added 4 failing-first regression tests covering issue example, tabs/newlines/CRLF/mixed runs, NBSP runs, and trim of all whitespace kinds; existing plain-space tests unchanged.
- `CHANGELOG.md` (modified) — Added Fixed entry under Unreleased for collapse_whitespace per CONTRIBUTING rule 1 and changelog CI check.

## Plan tasks

Completed:
- reproduce-issue
- fix-collapse
- add-regression-tests
- update-changelog
- verify-no-regressions

## Verification

Commands selected to prove the change:
- `pytest -q`
- `pytest -q ci`

Tests written or changed:
- `tests/test_normalize.py::test_collapses_tabs_and_newlines`
- `tests/test_normalize.py::test_collapses_crlf_and_mixed_runs`
- `tests/test_normalize.py::test_collapses_non_breaking_spaces`
- `tests/test_normalize.py::test_trims_all_whitespace_kinds`
- `tests/test_normalize.py::test_whitespace_only_collapses_to_empty`
- `tests/test_normalize.py::test_collapses_other_ascii_whitespace`

The authoritative result of running them is not recorded here: it is produced after this document exists, by a deterministic execution against the immutable candidate, and it lives in TandemVelocity as TestEvidence bound to that candidate.

## Provenance

- work item: jira:SCRUM-11
- project: textkit
- source revision: dardant/tv-sandbox@3aaef52ce8b5c40704c15b5efca4b6e7f8bd786f (ref main)
- project context baseline: v1
- context pack: 01a095c2-d324-74f0-a6a3-f789e51eadc2
- approved plan artifact: 01a095c4-003f-72cf-8cf1-032918244c53 (content hash 127527116959)
- produced by: TandemVelocity issue_to_change_request.v3, run 01a095c2-d0b0-7789-a68a-aa34ff23ae4c
