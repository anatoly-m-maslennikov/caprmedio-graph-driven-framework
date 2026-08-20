---
artifact_subtype: problem
subject_scopes:
  - carrier-format
priority: high
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: relates_to
    targets:
      - CAPRMEDIO-GOV-REQU-300--semantic-immutability-and-lossless-recoding
      - CAPRMEDIO-GOV-REQU-462--type-local-draft-active-and-archive-placement
      - CAPRMEDIO-GOV-REQU-470--register-current-atom-type-surface
      - CAPRMEDIO-GOV-REQU-317--register-evaluation-atom-subtypes
      - CAPRMEDIO-GOV-CONC-015--atomic-identities-use-retired-grammar
---

# Problem — Atomic carriers are not role-local

Active META and GOV atomic carriers still use legacy family directories:

- `decision/`;
- `problem/`;
- `question/`; and
- `qa/`.

The `decision/` directory mixes Requirement, Method, Delivery, and other
Content roles, while `problem/`, `question/`, `qa/`, and `evidence/` encode
historical families rather than the canonical CAPRMEDIO role order. This does
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
