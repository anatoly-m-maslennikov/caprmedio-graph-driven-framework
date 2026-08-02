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

# Problem — Atomic carriers are not role-local

Active META and GOV atomic carriers still use legacy family directories:

- `decision/`;
- `problem/`;
- `question/`; and
- `qa/`.

The `decision/` directory mixes Requirement, Method, Delivery, and other
Content roles, while `problem/`, `question/`, `qa/`, and `evidence/` encode
historical families rather than the canonical CARMADIO role order. This does
not implement the accepted recursive role-local active-root, `drafts/`, and
`archive/` layout.

The current Type surface and role-local target layout are registered, but the
carriers have not yet undergone the governed identity-and-path migration tracked
by the active identity Problem.

## Primary claim

Current META and GOV atoms remain grouped by legacy families rather than by
their canonical Content roles, so the accepted recursive role-local lifecycle
layout is not yet implemented.

## Rationale

The gap must remain explicit until identity and role-local placement are
migrated as one lossless graph operation; moving paths alone would separate
carriers from their registered identities and provenance.
