<!-- tandemvelocity:knowledge kind=spec work-item=SCRUM-11 project=textkit -->

# SCRUM-11 — collapse_whitespace() leaves tabs, newlines and non-breaking spaces in imported titles

_The approved implementation contract for this work item. Produced by TandemVelocity from the plan a person approved, before implementation. Do not edit by hand: an edit here is not an approved change of requirements, and the platform compares this file against the digest the approval bound._

## Problem

Fix jira:SCRUM-11 in dardant/tv-sandbox: collapse_whitespace() must collapse any run of whitespace (spaces, tabs, newlines, U+00A0) to a single space and trim leading/trailing whitespace of any kind, with plain-space behaviour unchanged.

Small bug-fix in src/textkit/normalize.py: change regex from ASCII-space-only ` +` plus `strip(" ")` to Unicode-whitespace `\s+` plus `strip()`, update docstring, add failing-first regression tests in tests/test_normalize.py, and add CHANGELOG.md Fixed entry. No public API or consumer-contract change.

## Acceptance Criteria

- Current output documented showing tabs/newlines/NBSP not collapsed/trimmed
- \s NBSP match behaviour confirmed for fix choice
- collapse_whitespace("Breaking\tnews\n today") == "Breaking news today"
- Any run of spaces/tabs/newlines/U+00A0 collapses to single space
- Leading/trailing whitespace of any kind removed
- Plain-space cases unchanged
- New tests cover tabs, newlines, U+00A0, mixed runs, and trim
- New tests fail before fix and pass after fix
- Existing test_collapses_runs_of_spaces and test_trims_both_ends still pass
- CHANGELOG.md touched under Unreleased Fixed
- Changelog CI check passes
- pytest -q passes
- pytest -q ci passes with 4 contract tests unmodified
- No public API surface change

## Affected Area

Components: textkit

Files the plan expects to touch:
- `CHANGELOG.md`
- `src/textkit/normalize.py`
- `tests/test_normalize.py`

## Test Strategy

TDD per CONTRIBUTING rule 5: add tests to tests/test_normalize.py that fail before the fix and pass after. Cover: tabs, newlines/CRLF, U+00A0 runs, mixed runs, leading/trailing whitespace of all kinds, plain-space regression ("a   b  c" -> "a b c", "  a b  " -> "a b"), and issue example. Local gate: pytest -q must pass. CI gate: pytest -q ci must pass unmodified (4 contract tests: public API, hyphenated slugs, three-dot ellipsis, title_case) plus changelog check.

Authoritative test command: `pytest -q`

## Constraints / Relevant Conventions

Reproduce the bug with the issue example "Breaking\tnews\n today" plus U+00A0 cases. Fix src/textkit/normalize.py: replace _SPACES = re.compile(r" +") with re.compile(r"\s+") and return _SPACES.sub(" ", text).strip() (no args), update docstring from "Runs of spaces" to "Runs of whitespace". Keep stdlib-only, Python 3.10+ and existing `from __future__ import annotations`. Add regression tests, add CHANGELOG Fixed line, then run unit and contract suites to prove no breakage.

- collapse_whitespace lives in src/textkit/normalize.py and is exported via textkit.__all__ with no signature change needed.
- Python re `\s` with str pattern matches spaces, tabs, newlines and U+00A0 on 3.10 and 3.12; to be verified in reproduction task with fallback to explicit `[\s\xa0]+` if needed.
- Plain `str.strip()` without args (all Unicode whitespace) is the desired trim behaviour per issue.
- slugify() is out of scope: it already maps most whitespace to hyphens via [^a-z0-9]+; only collapse_whitespace changes.
- No public API addition/removal and no ci/ contract-test edit is needed.

## Risks

- Python \s might not match U+00A0 on some builds, leaving NBSP uncollapsed. — mitigation: Explicitly assert re \s matches \xa0 in reproduction; fall back to r"[\s\xa0]+" and cover with NBSP tests.
- strip() without args strips more than before (tabs/newlines/NBSP at ends); a caller relying on preserving them would change behaviour. — mitigation: This is the requested behaviour; verify callers (slugify does its own normalization) and contract tests pass.
- Downstream slug oddities may persist if slugify drops NBSP via ascii-ignore instead of hyphenating; fixing only collapse_whitespace may not fully fix imported-title slugs. — mitigation: Keep slugify unchanged per issue scope; note observation in change request and verify slugify("Breaking\tnews\n today") behaviour in verification task.

## Provenance

- work item: jira:SCRUM-11
- project: textkit
- source revision: dardant/tv-sandbox@3aaef52ce8b5c40704c15b5efca4b6e7f8bd786f (ref main)
- project context baseline: v1
- context pack: 01a095c2-d324-74f0-a6a3-f789e51eadc2
- produced by: TandemVelocity issue_to_change_request.v3, run 01a095c2-d0b0-7789-a68a-aa34ff23ae4c
