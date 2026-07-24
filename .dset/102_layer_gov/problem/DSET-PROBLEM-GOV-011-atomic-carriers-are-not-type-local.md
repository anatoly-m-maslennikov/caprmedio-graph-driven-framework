---
artifact_type: problem
artifact_id: DSET-PROBLEM-GOV-011
scope_path: ["layer:gov"]
priority: high
llm_session_ids:
  - "codex:019f591f-04f6-70f2-8de7-828b7cccc69d"
relations:
  - type: relates_to
    targets:
      - "DSET-REQUIREMENT-GOV-108"
      - "DSET-REQUIREMENT-GOV-120"
      - "DSET-REQUIREMENT-GOV-121"
      - "DSET-PROBLEM-GOV-009"
---

# Problem — Atomic carriers are not Type-local

Active META and GOV atomic carriers still use four legacy family directories:

- `decision/`;
- `problem/`;
- `question/`; and
- `qa/`.

The `decision/` directory contains several distinct Types, while `qa/`
distinguishes subtypes without a canonical QA Case Type directory. This does
not implement the accepted Type-local active-root, `drafts/`, and `archive/`
layout.

Until the canonical route catalog is complete and carriers are migrated
losslessly, directory placement cannot derive an unambiguous Type-local
carrier kind for every atom.

## Primary claim

Current META and GOV atoms remain grouped by legacy families rather than by
their canonical artifact Types, so the accepted Type-local lifecycle layout is
not yet implemented.

## Rationale

The gap must remain explicit while the route catalog is incomplete. Moving
carriers prematurely would either invent Type ownership or require another
whole-graph migration immediately afterward.
