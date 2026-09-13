<!-- tandemvelocity:knowledge kind=story work-item=SCRUM-19 project=textkit -->

# SCRUM-19 — Fix fold_accents() to strip combining marks on NFD input (SCRUM-19) (as built)

_What this change did, recorded by TandemVelocity before the change was captured as an immutable candidate. This is a record, not a contract: the approved requirements are in the specification it names below._

## Summary

Fixes SCRUM-19 (reported as strip_accents): fold_accents() in src/textkit/normalize.py now explicitly strips combining marks after NFKD decomposition so both NFC and NFD 'café' fold to 'cafe' with no residual marks. Adds NFC/NFD regression test and CHANGELOG Fixed entry. Unit tests (89 passed) and contract tests (4 passed) verified without touching ci/ or public API.

## Implemented against

- specification: `_bmad-output/implementation-artifacts/SCRUM-19.spec.md`
- approved content digest: `7158257c12cf72a76b6ab51322b051f7c0c1b870c6dce887fbb42bf7a28f2ad2`
- plan approval: b3761e46-0108-5d78-bc31-ca2bef2cb6a7

## Changes

- `src/textkit/normalize.py` (modified) — Harden fold_accents: NFKD decompose then drop chars with combining!=0 or category Mn before ascii-ignore, so decomposed input leaves no combining marks while composed behavior is unchanged. Stdlib only, no signature change.
- `tests/test_normalize.py` (modified) — Add failing-first regression test test_folds_accents_for_composed_and_decomposed_input covering NFC and NFD café -> cafe, len 4, per CONTRIBUTING rule 5 and issue request for NFC+NFD coverage.
- `CHANGELOG.md` (modified) — Add Unreleased Fixed entry for fold_accents (reported as strip_accents) stripping combining marks for NFD input, satisfying CONTRIBUTING rule 1 and changelog CI job.

## Plan tasks

Completed:
- repro-naming
- regression-test
- fix-fold-accents
- changelog-entry
- verify-ci

## Verification

Commands selected to prove the change:
- `pytest -q`
- `pytest -q ci`

Tests written or changed:
- `tests/test_normalize.py::test_folds_accents_for_composed_and_decomposed_input — extended to assert no residual combining marks (unicodedata.combining==0 and category != Mn) for both NFC and NFD forms`

The authoritative result of running them is not recorded here: it is produced after this document exists, by a deterministic execution against the immutable candidate, and it lives in TandemVelocity as TestEvidence bound to that candidate.

## Provenance

- work item: jira:SCRUM-19
- project: textkit
- source revision: dardant/tv-sandbox@ca088206a7191df6fdadbb5b726b147777059c96 (ref main)
- project context baseline: v7
- context pack: 01a09af2-aae1-7624-8e12-822c5c774d5d
- approved plan artifact: 01a09af3-4dc8-731f-90b8-0a918b325498 (content hash e2025ef1e351)
- produced by: TandemVelocity issue_to_change_request.v3, run 01a09af2-7e2f-7338-a115-cacacef46cf7
