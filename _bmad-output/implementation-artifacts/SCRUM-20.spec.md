<!-- tandemvelocity:knowledge kind=spec work-item=SCRUM-20 project=textkit -->

# SCRUM-20 — snake_case() runs acronyms into the following word

_The approved implementation contract for this work item. Produced by TandemVelocity from the plan a person approved, before implementation. Do not edit by hand: an edit here is not an approved change of requirements, and the platform compares this file against the digest the approval bound._

## Problem

Fix jira:SCRUM-20 so textkit.snake_case() splits a run of capitals followed by a capitalised word (HTTPServer -> http_server, parseHTTPResponse -> parse_http_response) while preserving existing behaviour (orderTotal, Order Total, version2Update).

Add an acronym-boundary split to src/textkit/case.py alongside the existing camel seam, pin it with start-of-name and middle-of-name regression tests in tests/test_case.py, and record the fix under CHANGELOG Unreleased/Fixed without touching public API or ci contract tests.

## Acceptance Criteria

- Confirmed HTTPServer returns httpserver (expected http_server)
- Confirmed parseHTTPResponse returns parse_httpresponse (expected parse_http_response)
- Documented current outputs of orderTotal, Order Total, version2Update as baseline
- Test for acronym at start exists and fails before fix
- Test for acronym in middle exists and fails before fix
- Tests live in tests/test_case.py next to snake_case behaviour
- snake_case('HTTPServer') == 'http_server'
- snake_case('parseHTTPResponse') == 'parse_http_response'
- snake_case('orderTotal') == 'order_total', snake_case('Order Total') == 'order_total', snake_case('version2Update') == 'version2_update'
- CHANGELOG.md touched under Unreleased Fixed
- No other sections or versions altered
- pytest -q passes
- pytest -q ci passes without editing ci/test_contract.py
- Branch diff touches only src/textkit/case.py, tests/test_case.py, CHANGELOG.md

## Affected Area

Components: textkit

Files the plan expects to touch:
- `CHANGELOG.md`
- `src/textkit/case.py`
- `tests/test_case.py`

## Test Strategy

Local `pytest -q` must pass (all tests in tests/, including 2 new acronym tests that fail before the fix and pass after, plus existing orderTotal/Order Total/version2Update tests). CI-only `pytest -q ci` must pass unmodified (public API, hyphenated slugs, three-dot ellipsis, title_case). Manually verify repro: HTTPServer->http_server, parseHTTPResponse->parse_http_response, and spot-check HTTPServerError->http_server_error, parseJSONResponse->parse_json_response, single acronym HTTP->http, trailing acronym, and digit cases. Confirm CHANGELOG.md diff exists so changelog job passes.

Authoritative test command: `pytest -q`

## Constraints / Relevant Conventions

Reproduce the two reported cases plus the three must-keep cases. Add failing regression tests for acronym-at-start and acronym-in-middle. Fix snake_case() by adding a second zero-width split _ACRONYM_SEAM = re.compile(r'(?<=[A-Z])(?=[A-Z][a-z])') applied after the existing _CAMEL_SEAM (spaced = _ACRONYM_SEAM.sub(' ', _CAMEL_SEAM.sub(' ', text))) then existing _WORD tokenize + lower + join. This splits before the last capital of a run only when followed by lowercase, so HTTPServer->HTTP Server and parseHTTPResponse->parse HTTP Response, while orderTotal, Order Total, version2Update are unchanged. Record under Unreleased Fixed, then verify with pytest -q and pytest -q ci.

- Base is dardant/tv-sandbox@main ca088206a7191df6fdadbb5b726b147777059c96; src/textkit/case.py contains only _CAMEL_SEAM (?<=[a-z0-9])(?=[A-Z]).
- Fix is non-breaking: no change to textkit.__all__, ci/public_api.txt, slugify/truncate/title_case behaviour, or ci/test_contract.py.
- Standard library only, Python 3.10+; src/textkit/case.py keeps `from __future__ import annotations`.
- CHANGELOG.md must be touched on the branch or the `changelog` CI job fails (CONTRIBUTING.md rule 1).
- Related SCRUM-12 (HTTPServerError, parseJSONResponse) describes the same root cause and will be fixed incidentally but remains a separate work item unless triaged as duplicate.

## Risks

- Over-splitting edge cases (e.g., single trailing acronym, all-caps input 'HTTP', digit+acronym like 'version2API', single letters) changes outputs beyond the issue scope. — mitigation: Keep _WORD tokenization unchanged; verify edge cases manually and keep scope to the (?<=[A-Z])(?=[A-Z][a-z]) rule from SCRUM-12/SCRUM-20.
- Branch fails CI changelog job if CHANGELOG.md is missed, as seen in main CI state (changelog: failure). — mitigation: Dedicated update-changelog task; verify diff includes CHANGELOG.md before review.
- Accidental edit to ci/test_contract.py or public API would be treated as breaking per CONTRIBUTING rule 4. — mitigation: Do not touch ci/ or src/textkit/__init__.py; verify with pytest -q ci unmodified.

## Decisions a person must settle

- SCRUM-12 (HTTPServerError -> http_server_error, parseJSONResponse -> parse_json_response) appears to be the same root cause as SCRUM-20. Should this change also close SCRUM-12 as duplicate/fixed, or keep SCRUM-12 open for separate verification? (recommended: Keep SCRUM-12 separate; note in SCRUM-20 change request that it incidentally fixes SCRUM-12 examples.) — not blocking

## Provenance

- work item: jira:SCRUM-20
- project: textkit
- source revision: dardant/tv-sandbox@ca088206a7191df6fdadbb5b726b147777059c96 (ref main)
- project context baseline: v7
- context pack: 01a09b79-23c6-76b5-8e04-1701444775ce
- approved plan artifact: 01a09b79-b239-77fc-a123-36ec2fe35d73 (content hash 3ed6ace2ae55)
- produced by: TandemVelocity issue_to_change_request.v3, run 01a09b78-fbf3-7784-90cc-1c74d42397ef
