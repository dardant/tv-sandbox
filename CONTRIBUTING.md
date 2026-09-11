# Contributing to textkit

textkit is small, but two services consume it, so a few rules keep it safe to change. CI enforces rules 1, 2 and 4;
a branch that breaks one of them fails the `ci` workflow even when `pytest -q` passes locally.

1. **Record every change in `CHANGELOG.md`.** Add a line under `## Unreleased` in the matching subsection
   (`Added`, `Changed`, `Fixed`). The `changelog` CI job fails a branch that does not touch `CHANGELOG.md`.
2. **The public API is `textkit.__all__`.** To add a function, export it from `src/textkit/__init__.py`, add its
   name to `ci/public_api.txt`, and list it under `Added`. Removing or renaming a published name is a breaking
   change (rule 4).
3. **Python 3.10+ and the standard library only.** CI runs the unit tests on 3.10 and 3.12. Every module starts
   with `from __future__ import annotations`.
4. **`ci/` holds consumer contract tests.** They run in CI only. The CMS importer depends on hyphenated slugs and
   the three-dot ellipsis; the file-naming service depends on the published names. Do not edit a contract test to
   make a change pass: a change that needs one edited is breaking and needs a maintainers' decision first.
5. **Tests live next to the behaviour they pin**: one `tests/test_<module>.py` per module. A bug fix adds a test
   that fails before the fix.

Local check before pushing: `pytest -q`. CI additionally runs `pytest -q ci` and the changelog check.
