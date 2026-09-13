<!-- tandemvelocity:knowledge kind=story work-item=SCRUM-20 project=textkit -->

# SCRUM-20 — Fix snake_case() acronym fusion (SCRUM-20) (as built)

_What this change did, recorded by TandemVelocity before the change was captured as an immutable candidate. This is a record, not a contract: the approved requirements are in the specification it names below._

## Summary

Fixes SCRUM-20: snake_case() now splits a run of capitals followed by a capitalised word via a second zero-width split _ACRONYM_SEAM (?<=[A-Z])(?=[A-Z][a-z]) applied with the existing _CAMEL_SEAM, so HTTPServer->http_server and parseHTTPResponse->parse_http_response while orderTotal, Order Total and version2Update are unchanged. Adds leading-acronym and middle-acronym regression tests and records the fix under CHANGELOG Unreleased/Fixed. Verified with pytest -q (90 passed) and pytest -q ci (4 passed).

## Implemented against

- specification: `_bmad-output/implementation-artifacts/SCRUM-20.spec.md`
- approved content digest: `b5c79d94b361ee92e4bdb6ca7a53ccb0f418b20b75ec4b682674cfe097d05ea4`
- plan approval: 49b0e9a6-9cf3-5c0a-b5a3-3701be77aef4

## Changes

- `src/textkit/case.py` (modified) — Add _ACRONYM_SEAM (?<=[A-Z])(?=[A-Z][a-z]) and apply with _CAMEL_SEAM so acronym + capitalised word splits before last capital.
- `tests/test_case.py` (modified) — Add regression tests for acronym at start (HTTPServer->http_server) and in middle (parseHTTPResponse->parse_http_response) per issue notes.
- `CHANGELOG.md` (modified) — Record snake_case acronym fix under Unreleased Fixed to satisfy changelog CI job.

## Plan tasks

Completed:
- reproduce-bug
- add-regression-tests
- fix-snake-case
- update-changelog
- verify-tests

## Verification

Commands selected to prove the change:
- `pytest -q`
- `pytest -q ci`

Tests written or changed:
- `tests/test_case.py::test_snake_case_splits_leading_acronym_with_trailing_word`
- `tests/test_case.py::test_snake_case_splits_second_middle_acronym`
- `tests/test_case.py::test_snake_case_keeps_lone_acronym_intact`
- `tests/test_case.py::test_snake_case_keeps_trailing_acronym_separate`
- `tests/test_case.py::test_snake_case_splits_acronym_between_lowercase_words`

The authoritative result of running them is not recorded here: it is produced after this document exists, by a deterministic execution against the immutable candidate, and it lives in TandemVelocity as TestEvidence bound to that candidate.

## Provenance

- work item: jira:SCRUM-20
- project: textkit
- source revision: dardant/tv-sandbox@ca088206a7191df6fdadbb5b726b147777059c96 (ref main)
- project context baseline: v7
- context pack: 01a09b79-23c6-76b5-8e04-1701444775ce
- approved plan artifact: 01a09b79-b239-77fc-a123-36ec2fe35d73 (content hash 3ed6ace2ae55)
- produced by: TandemVelocity issue_to_change_request.v3, run 01a09b78-fbf3-7784-90cc-1c74d42397ef
