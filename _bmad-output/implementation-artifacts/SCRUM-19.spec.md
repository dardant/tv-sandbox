<!-- tandemvelocity:knowledge kind=spec work-item=SCRUM-19 project=textkit -->

# SCRUM-19 — strip_accents() leaves combining marks on decomposed input

_The approved implementation contract for this work item. Produced by TandemVelocity from the plan a person approved, before implementation. Do not edit by hand: an edit here is not an approved change of requirements, and the platform compares this file against the digest the approval bound._

## Problem

Deliver jira:SCRUM-19 on branch tv/scrum-19/01a09af2: strip_accents/fold_accents returns text with no combining marks for both NFC and NFD input, preserving existing composed-input behaviour, with NFC/NFD regression test and changelog, without breaking consumer contracts.

SCRUM-19 reports textkit.strip_accents() in src/textkit/normalize.py leaves combining marks on NFD input (NFD cafe -> 5 codepoints instead of cafe). The pinned main (ca08820) has no strip_accents symbol; the accent-folding public API is fold_accents() using NFKD+ascii-ignore, plus duplicated logic in slugify(). Plan treats strip_accents as fold_accents naming mismatch, adds a failing-first NFC/NFD regression test, hardens normalize.py to explicitly strip combining marks, records the fix in CHANGELOG.md, and verifies with pytest -q and pytest -q ci without touching ci/ contracts or public API.

## Acceptance Criteria

- Repro script output recorded for NFC vs NFD café
- Confirmed target function is fold_accents absent strip_accents
- Test covers both NFC and NFD input for same word
- Asserts result == 'cafe' and no combining marks remain
- Existing composed-input expectation unchanged
- NFD café returns cafe with 4 codepoints and zero combining marks
- NFC café behaviour unchanged
- No new public name added or renamed
- CHANGELOG.md touched under Unreleased Fixed
- No other changelog sections altered
- pytest -q passes
- pytest -q ci passes with no edits to ci/
- No change to ci/public_api.txt or __all__

## Affected Area

Components: textkit

Files the plan expects to touch:
- `CHANGELOG.md`
- `ci/test_contract.py`
- `src/textkit/__init__.py`
- `src/textkit/normalize.py`
- `tests/test_normalize.py`

## Test Strategy

New test in tests/test_normalize.py: NFC and NFD forms of café both assert == 'cafe', len==4, and all(unicodedata.combining(c)==0). Run pytest -q for units and pytest -q ci for the 4 consumer contracts (hyphenated slugs, three-dot ellipsis, title_case, exact public API). Contracts must pass unmodified; any need to edit ci/ is treated as breaking and stops the change. Existing test_folds_accents guards composed-input regression.

Authoritative test command: `pytest -q`

## Constraints / Relevant Conventions

Resolve naming first (strip_accents vs fold_accents), reproduce NFD residual-mark case, add NFC/NFD regression test next to behaviour in tests/test_normalize.py, then harden fold_accents in src/textkit/normalize.py to NFKD + explicit Mn/combining strip + ascii-ignore with unchanged signature, add CHANGELOG Fixed entry, and verify without touching ci/ or public API. Keep change minimal; do not refactor slugify duplication unless human approves.

- Issue's strip_accents() refers to the existing public fold_accents() in src/textkit/normalize.py; no strip_accents symbol exists on main (verified by search).
- Base for the branch is main ca088206a7191df6fdadbb5b726b147777059c96 with fold_accents as NFKD+ascii-ignore.
- No new public API name is intended; fix is internal behaviour of fold_accents, so ci/public_api.txt and src/textkit/__init__.py stay unchanged.
- Python 3.10+ standard library only and from __future__ import annotations convention apply.
- slugify() in src/textkit/slug.py duplicates folding logic and is out of scope unless human decides otherwise.

## Risks

- Issue names strip_accents() but codebase only exports fold_accents(); fixing the wrong symbol or adding a duplicate API breaks expectations. — mitigation: Treat as naming mismatch, fix fold_accents only, and gate on human decision before adding any alias.
- Current NFKD+ascii-ignore may already strip NFD marks, making the reported bug unreproducible on main and the fix a hardening no-op. — mitigation: Require repro evidence in repro-naming task; explicit Mn filter makes intent robust regardless.
- Adding a new strip_accents export would change textkit.__all__ and require ci/public_api.txt update, tripping the public-API contract. — mitigation: No __all__ or public_api.txt change in plan; any new name needs maintainer approval.
- Missing CHANGELOG.md touch fails the changelog CI job even when pytest passes. — mitigation: Dedicated changelog-entry task under Unreleased Fixed.
- Over-broad combining-mark stripping could alter non-Latin, ligature, or slug behaviour relied on by CMS importer. — mitigation: Limit scope to fold_accents, keep ascii folding semantics, verify slug and contract tests unmodified.

## Decisions a person must settle

- SCRUM-19 says strip_accents() but the repo only has fold_accents(). Should implementation fix fold_accents() (no API change) or add strip_accents as a new public name/alias (requires __all__ + ci/public_api.txt + Added changelog)? (recommended: Fix fold_accents only, no new name)
- Should src/textkit/slug.py be refactored to reuse the fixed fold_accents() instead of its duplicated NFKD+ascii-ignore logic, or left untouched for minimal scope? (recommended: Leave slug.py untouched) — not blocking

## Provenance

- work item: jira:SCRUM-19
- project: textkit
- source revision: dardant/tv-sandbox@ca088206a7191df6fdadbb5b726b147777059c96 (ref main)
- project context baseline: v7
- context pack: 01a09af2-aae1-7624-8e12-822c5c774d5d
- approved plan artifact: 01a09af3-4dc8-731f-90b8-0a918b325498 (content hash e2025ef1e351)
- produced by: TandemVelocity issue_to_change_request.v3, run 01a09af2-7e2f-7338-a115-cacacef46cf7
