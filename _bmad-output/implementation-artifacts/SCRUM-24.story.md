<!-- tandemvelocity:knowledge kind=story work-item=SCRUM-24 project=textkit -->

# SCRUM-24 — Fix truncate() to treat all whitespace as word boundaries (SCRUM-24) (as built)

_What this change did, recorded by TandemVelocity before the change was captured as an immutable candidate. This is a record, not a contract: the approved requirements are in the specification it names below._

## Summary

truncate() only recognized ASCII space when placing word-boundary cuts, so tab/NBSP titles were hard-cut mid-word. Boundary checks in src/textkit/truncate.py now use str.isspace() and scan for the last whitespace character; rstrip() already trims all whitespace. Added tab and NBSP regression tests in tests/test_truncate.py and a CHANGELOG Fixed entry. Existing width/ellipsis, hard-cut, fits-unchanged, and tiny-width behavior unchanged.

## Implemented against

_No repository-backed specification was in force for this change; the approved plan is in TandemVelocity._

## Changes

- `src/textkit/truncate.py` (modified) — Treat any whitespace (space, tab, line break, NBSP) as a word boundary via str.isspace() instead of ASCII-space-only checks
- `tests/test_truncate.py` (modified) — Add required regression tests: tab and non-breaking space are word boundaries, both yielding Designing... at width 20
- `CHANGELOG.md` (modified) — Record fix under Unreleased/Fixed per CONTRIBUTING rule 1 so the changelog CI job passes

## Verification

Commands selected to prove the change:
- `pytest -q tests/test_truncate.py`

The authoritative result of running them is not recorded here: it is produced after this document exists, by a deterministic execution against the immutable candidate, and it lives in TandemVelocity as TestEvidence bound to that candidate.

## Provenance

- work item: jira:SCRUM-24
- project: textkit
- source revision: dardant/tv-sandbox@ca088206a7191df6fdadbb5b726b147777059c96 (ref main)
- project context baseline: v7
- context pack: 01a0a9d7-9631-76d8-a50f-f546a29e5a26
- produced by: TandemVelocity evidence_driven_change_request.v1, run 01a0a9d7-8ed9-7390-8704-b5b39ce62625
