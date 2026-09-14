<!-- tandemvelocity:knowledge kind=story work-item=SCRUM-24 project=textkit -->

# SCRUM-24 — Fix truncate() to treat all whitespace as word boundaries (SCRUM-24) (as built)

_What this change did, recorded by TandemVelocity before the change was captured as an immutable candidate. This is a record, not a contract: the approved requirements are in the specification it names below._

## Summary

Fixes SCRUM-24 in src/textkit/truncate.py by treating any whitespace (space, tab, line break, non-breaking space via str.isspace()) as a word boundary when placing the cut. Adds two regression tests in tests/test_truncate.py for tab and non-breaking space, and records the fix under Unreleased Fixed in CHANGELOG.md. No public API or contract changes.

## Implemented against

_No repository-backed specification was in force for this change; the approved plan is in TandemVelocity._

## Changes

- `src/textkit/truncate.py` (modified) — Treat any whitespace as word boundary per SCRUM-24 expected behavior
- `tests/test_truncate.py` (modified) — Add required regression tests for tab and non-breaking space
- `CHANGELOG.md` (modified) — Record fix under Unreleased Fixed per CONTRIBUTING rule 1

## Verification

Commands selected to prove the change:
- `pytest -q`
- `pytest -q ci`

The authoritative result of running them is not recorded here: it is produced after this document exists, by a deterministic execution against the immutable candidate, and it lives in TandemVelocity as TestEvidence bound to that candidate.

## Provenance

- work item: jira:SCRUM-24
- project: textkit
- source revision: dardant/tv-sandbox@ca088206a7191df6fdadbb5b726b147777059c96 (ref main)
- project context baseline: v7
- context pack: 01a0a1d6-8de5-767e-a351-3eb46196d263
- produced by: TandemVelocity evidence_driven_change_request.v1, run 01a0a1d6-7498-7568-a2b4-0825cc99355f
