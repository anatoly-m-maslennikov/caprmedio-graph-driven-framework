---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-GOV-057
scope_path: layer:gov
subject_scopes:
  - external-boundary
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-META-102
  relates_to:
    - CAPRMADIO-REQUIREMENT-GOV-138
    - CAPRMADIO-REQUIREMENT-GOV-196
---
# Constraints are externally imposed

Use the `constraint` Type only when the limitation originates outside the project's
choice boundary, such as a law, existing DDL, mandated host format, platform
limit, or non-negotiable upstream interface.

Use `requirement` for results the operator or project requires, including
format choices, supported behavior, forbidden project behavior, and quality
targets. A selected implementation approach is a `method` Atom with the
`implementation_decision` subtype; an obligation across governed endpoints uses the
relational `contract` Type.

## Rationale

Separating external limits from required project outcomes makes Requirement and Constraint mutually exclusive and prevents implementation preferences from being mislabeled as unavoidable boundaries.
