---
artifact_type: requirement
artifact_id: DSET-REQUIREMENT-GOV-057
scope_path: layer:gov
subject_scopes:
  - external-boundary
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-102
  - type: relates_to
    targets:
      - CARMADIO-REQUIREMENT-GOV-138
      - CARMADIO-REQUIREMENT-GOV-141
---

# Requirement — Constraints are externally imposed

Use the `constraint` Type only when the limitation originates outside the project's
choice boundary, such as a law, existing DDL, mandated host format, platform
limit, or non-negotiable upstream interface.

Use `requirement` for results the operator or project requires, including
format choices, supported behavior, forbidden project behavior, and quality
targets. A selected implementation approach is a `method` Atom with the
`technical_decision` subtype; an obligation across governed endpoints uses the
relational `contract` Type.

## Primary claim

The Constraint Type is reserved for externally imposed limitations that the project must obey; operator-selected or project-owned required results use the internal Requirement Type.

## Rationale

Separating external limits from required project outcomes makes Requirement and Constraint mutually exclusive and prevents implementation preferences from being mislabeled as unavoidable boundaries.
