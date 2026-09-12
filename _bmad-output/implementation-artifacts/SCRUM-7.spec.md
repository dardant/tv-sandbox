<!-- tandemvelocity:knowledge kind=spec work-item=SCRUM-7 project=textkit -->

# SCRUM-7 — title_case() lowercases acronyms: 'NASA launches new API' becomes 'Nasa Launches New Api'

_The approved implementation contract for this work item. Produced by TandemVelocity from the plan a person approved, before implementation. Do not edit by hand: an edit here is not an approved change of requirements, and the platform compares this file against the digest the approval bound._

## Problem

Fix jira:SCRUM-7 in dardant/tv-sandbox: title_case() must preserve all-caps acronyms (e.g., NASA, API) and mixed-case words (e.g., iPhone) while still capitalizing ordinary lowercase words and single-letter words.

title_case() currently applies str.capitalize() to every whitespace-separated word, lowercasing acronyms ('NASA launches new API' -> 'Nasa Launches New Api'). Plan preserves existing whitespace-collapse behavior and contract test, adds per-word preservation for len>1 all-caps and mixed-case tokens, adds failing-first regression tests in tests/test_case.py, and records the fix in CHANGELOG.md.

## Acceptance Criteria

- Confirmed current output 'Nasa Launches New Api' for the issue example
- Confirmed contract case 'hello world' -> 'Hello World' baseline
- New tests fail on unfixed code except already-passing cases
- Tests live in tests/test_case.py next to behaviour
- title_case('NASA launches new API') == 'NASA Launches New API'
- title_case('a') == 'A' and single-letter handling verified
- title_case('iPhone') preserves 'iPhone'
- title_case('hello world') == 'Hello World' and collapse-spaces case still pass
- No change to snake_case or other exports
- CHANGELOG.md touched under Unreleased Fixed
- Changelog CI job passes
- pytest -q passes
- pytest -q ci passes without editing ci/test_contract.py
- No public API drift

## Affected Area

Components: textkit

Files the plan expects to touch:
- `CHANGELOG.md`
- `src/textkit/case.py`
- `tests/test_case.py`

## Test Strategy

New regression tests in tests/test_case.py for: 'NASA launches new API' -> 'NASA Launches New API', single-letter 'a' -> 'A', 'iPhone' preserved, plus all-lower and multi-space cases. Must fail before fix and pass after. Run pytest -q for units and pytest -q ci for the 4 consumer contract tests (especially test_title_case_capitalizes_each_word) unmodified. Verify changelog job by confirming CHANGELOG.md is touched.

Authoritative test command: `pytest -q`

## Constraints / Relevant Conventions

Reproduce with the exact issue string, then add failing-first tests in tests/test_case.py. Implement minimal per-word branch in src/textkit/case.py using str.isupper()/islower() with len==1 special-case, preserving split/join whitespace semantics. Do not touch snake_case, __all__, ci/public_api.txt, or ci/test_contract.py. Finish with CHANGELOG.md Fixed entry and local pytest -q plus pytest -q ci verification.

- Base is main at a9082d86713db6d10e41b459bc9b08305f510d02; src/textkit/case.py title_case is `return ' '.join(word.capitalize() for word in text.split())`.
- Existing behavior to preserve: split on whitespace, collapse repeats, join with single space.
- Acronym means word where all cased characters are uppercase and word length >1 (Python str.isupper() semantics), so trailing punctuation/digits do not break detection (e.g., 'API,' stays).
- Single-letter words are always capitalized (e.g., 'a' -> 'A'), even though 'A'.isupper() is true.
- Mixed-case means not all-lower and not all-upper with length >1 (e.g., 'iPhone', 'Launches'); preserved exactly as written.
- No public API change: no new export, no change to ci/public_api.txt; contract tests in ci/ must not be edited.
- CHANGELOG.md Unreleased/ Fixed entry is required for CI changelog job.

## Risks

- Punctuation/digit-attached tokens (e.g., 'API,', "NASA's", 'MP3') may classify unexpectedly under isupper()/islower() semantics. — mitigation: Use isupper() semantics (ignores non-cased chars) and cover punctuated acronyms in tests; keep logic simple and document assumption.
- Downstream code may rely on current lowercasing behavior (e.g., expecting 'Nasa'); preserving acronyms changes output. — mitigation: Contract tests only pin 'hello world' case which is unchanged; change is the requested fix. Flag in changelog and PR description.
- Overlap with SCRUM-12 snake_case acronym handling could tempt a shared helper refactor that widens scope. — mitigation: Keep fix local to title_case; do not refactor snake_case or _CAMEL_SEAM in this change.

## Decisions a person must settle

- Confirm acronym definition: len>1 word where all cased chars are uppercase via str.isupper() (so 'API,' and 'NASA2' count as acronyms) vs strict A-Z-only? Mixed-case (e.g., 'iPhone', "NASA's") always preserved exactly? (recommended: Yes: use isupper() len>1 + preserve mixed-case (recommended)) — not blocking

## Provenance

- work item: jira:SCRUM-7
- project: textkit
- source revision: dardant/tv-sandbox@a9082d86713db6d10e41b459bc9b08305f510d02 (ref main)
- project context baseline: v1
- context pack: 01a09482-1886-75d3-8492-f6e473210ffe
- produced by: TandemVelocity issue_to_change_request.v3, run 01a09482-08fc-7300-8bd1-b9a1fe29b069
