<!-- tandemvelocity:knowledge kind=spec work-item=SCRUM-24 project=textkit -->
# Work contract jira:SCRUM-24

_truncate() cuts in the middle of a word when the title contains a tab or a line break_

## Objective

Deliver work item jira:SCRUM-24 of project textkit as a reviewed change request on dardant/tv-sandbox.

## Acceptance criteria

Titles imported from the partner feed contain tabs and line breaks, and the article cards show cuts like "Designing\tresilie...". The same title with ordinary spaces is cut cleanly at a word boundary.
Steps to reproduce
- truncate("Designing\tresilient systems", 20) returns 'Designing\tresilie...'; expected 'Designing...'
- truncate("Designing\u00a0resilient systems", 20) with a non-breaking space returns 'Designing\xa0resilie...'; expected 'Designing...'

Expected
Any whitespace - space, tab, line break, non-breaking space - is a word boundary, so the cut lands at the last one that fits. Everything truncate() already does must keep working: the result including the ellipsis is never longer than `width`; a single word longer than the room left is still hard-cut; text that fits is returned unchanged; a `width` too small for the ellipsis still returns a hard cut with no marker.
Notes
- the function is in src/textkit/truncate.py
- please add a test for a tab and one for a non-breaking space

## Out of scope

- anything the acceptance criteria above do not ask for
- weakening, deleting or skipping existing tests
- changes outside the repository and paths this project governs

## Verification TandemVelocity will perform

- the workspace is frozen into an immutable candidate change before anything authoritative is measured
- the authoritative command `pytest -q` is run by the platform against that candidate, and every command it runs must pass
- the deterministic test evidence is bound to the exact candidate digest
- an independent reviewer judges that candidate against this contract
- a person decides the change gate, and delivery pushes exactly the approved bytes

## Provenance

- work item: jira:SCRUM-24 (content hash 56ab2a970d79)
- classification: defect
- repository: dardant/tv-sandbox
- produced by: TandemVelocity evidence_driven_change_request.v1, run 01a0a9d7-8ed9-7390-8704-b5b39ce62625
