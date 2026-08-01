---
artifact_type: concern
artifact_subtype: problem
artifact_id: CARMADIO-PROBLEM-GOV-011
scope_path: layer:gov
subject_scopes:
  - carrier-format
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-GOV-108
      - CARMADIO-REQUIREMENT-GOV-120
      - CARMADIO-REQUIREMENT-GOV-138
      - CARMADIO-REQUIREMENT-GOV-139
      - CARMADIO-PROBLEM-GOV-012
---

# Problem — Atomic carriers are not Type-local

Active META and GOV atomic carriers still use four legacy family directories:

- `decision/`;
- `problem/`;
- `question/`; and
- `qa/`.

The `decision/` directory contains several distinct Types, while `qa/`
contains Assurance Atoms outside an `assurance/` Type directory. This does not
implement the accepted Type-local active-root, `drafts/`, and `archive/` layout.

The current Type surface is registered, but the carriers have not yet undergone
the governed identity-and-path migration tracked by the active identity
Problem.

## Primary claim

Current META and GOV atoms remain grouped by legacy families rather than by
their canonical artifact Types, so the accepted Type-local lifecycle layout is
not yet implemented.

## Rationale

The gap must remain explicit until Type identity and placement are migrated as
one lossless graph operation; moving paths alone would separate carriers from
their registered identities and provenance.
