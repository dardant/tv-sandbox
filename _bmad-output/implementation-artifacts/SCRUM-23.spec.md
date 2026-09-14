<!-- tandemvelocity:knowledge kind=spec work-item=SCRUM-23 project=textkit -->

# SCRUM-23 — title_case() does not capitalise a word that starts with a quote or a bracket

_The approved implementation contract for this work item. Produced by TandemVelocity from the plan a person approved, before implementation. Do not edit by hand: an edit here is not an approved change of requirements, and the platform compares this file against the digest the approval bound._

## Problem

Fix jira:SCRUM-23 in dardant/tv-sandbox: title_case() must capitalise a word at its first letter even when leading quote/bracket punctuation is present, while preserving all existing title_case() behaviour.

title_case() in src/textkit/case.py delegates whitespace-split tokens to _title_word(), which calls str.islower()/capitalize() on the whole token. With leading punctuation (e.g. '"hello', '(hello)') capitalize() uppercases the punctuation character (no-op) and leaves the first letter lower, causing the reported bug. Plan: reproduce, add the two requested regression tests in tests/test_case.py, fix _title_word() to isolate leading non-alphanumeric punctuation and apply existing acronym/mixed-case logic to the remainder, record under CHANGELOG.md Unreleased/Fixed, and verify with pytest -q plus pytest -q ci without touching ci/ contracts or public API.

## Acceptance Criteria

- Both bug examples confirmed failing on unmodified code
- Must-keep examples documented as baseline
- One test covers quoted leading word
- One test covers bracketed leading word
- Both tests fail before fix and pass after fix
- title_case('"hello world" said the fox') == '"Hello World" Said The Fox'
- title_case('(hello) world') == '(Hello) World'
- title_case('NASA launches new API') == 'NASA Launches New API'
- title_case('iPhone') == 'iPhone' and title_case('a') == 'A'
- title_case("NASA's launch") == "NASA's Launch"
- Pure-punctuation and empty tokens do not crash
- CHANGELOG.md touched under Unreleased Fixed
- No other changelog sections altered
- pytest -q passes including the two new tests
- pytest -q ci passes unmodified
- No contract test edited and no public API surface changed

## Affected Area

Components: textkit

Files the plan expects to touch:
- `CHANGELOG.md`
- `src/textkit/case.py`
- `tests/test_case.py`

## Test Strategy

Test-first bugfix per CONTRIBUTING.md rule 5: the two new tests in tests/test_case.py must fail before and pass after. Local gate is pytest -q covering all existing test_case cases plus the must-keep examples from the issue. CI gate additionally runs pytest -q ci to confirm hyphenated-slug, three-dot-ellipsis, exact public API, and basic title_case contracts are unmodified, plus the changelog presence check (CHANGELOG.md must be touched). Manually probe edge cases: empty string, punctuation-only token, single-letter quoted word, quoted acronym (e.g. '"NASA launches') stays upper.

Authoritative test command: `pytest -q`

## Constraints / Relevant Conventions

Keep title_case() splitting on whitespace and joining with single spaces. Fix only _title_word(): match leading non-alphanumeric prefix (e.g. quotes, brackets) via regex or manual scan, delegate the remainder to the existing logic (len==1 capitalize, isupper preserve, islower capitalize, else preserve), then reattach prefix; return token unchanged if remainder is empty. This preserves acronym handling (NASA, API, NASA2, NASA's), mixed-case preservation (iPhone, Launches), and trailing-punctuation behaviour (API,, world") while making '"hello' -> '"Hello' and '(hello)' -> '(Hello)'. No changes to snake_case, __all__, ci/public_api.txt, or ci/test_contract.py.

- Base is main at ca088206a7191df6fdadbb5b726b147777059c96; src/textkit/case.py, tests/test_case.py, CHANGELOG.md and ci/test_contract.py are as read.
- No public API change is needed: title_case signature and textkit.__all__ stay unchanged.
- Fix is non-breaking: existing contract test title_case('hello world')=='Hello World' and all tests/test_case.py cases must keep passing.
- Leading punctuation means leading non-alphanumeric characters (quotes, brackets, etc.); digits are treated as part of the word, not punctuation.
- Trailing punctuation already works and must not change behaviour.
- Python 3.10+ and standard library only; every edited module keeps 'from __future__ import annotations'.

## Risks

- str.capitalize() lowercases the rest of the string; naive upper-first-letter fix could lowercase acronyms or mixed-case tails (e.g. '"NASA' -> '"Nasa'). — mitigation: Reuse existing isupper/islower/mixed branches on the remainder instead of blind capitalize; regression tests cover NASA, API, iPhone, NASA's.
- Ambiguity for digit-leading tokens (e.g. '2nd') and unicode quotes: treating digits as prefix would newly capitalise after digits. — mitigation: Define prefix as non-alphanumeric only so digits stay in the word; limit scope to ASCII punctuation in issue examples and leave unicode behaviour unchanged unless tests demand it.
- Branch fails CI changelog job if CHANGELOG.md is missed (main already shows changelog failures). — mitigation: Dedicated update-changelog task and verify-suite dependency on it.
- Temptation to edit ci/test_contract.py to make change pass would violate rule 4 and mask a breaking change. — mitigation: Explicitly forbid ci/ edits; verify-suite requires pytest -q ci to pass unmodified.

## Provenance

- work item: jira:SCRUM-23
- project: textkit
- source revision: dardant/tv-sandbox@ca088206a7191df6fdadbb5b726b147777059c96 (ref main)
- project context baseline: v7
- context pack: 01a0a1cf-9b60-7068-9fc1-4bf20a3c1788
- approved plan artifact: 01a0a1d0-ce2e-772e-9bb3-a84e251cde41 (content hash 6dbb0428c882)
- produced by: TandemVelocity issue_to_change_request.v3, run 01a0a1cf-97e1-70df-a4d8-ae7e9e1604b9
