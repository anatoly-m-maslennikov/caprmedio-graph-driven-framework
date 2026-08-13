---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-134
scope_path: layer:meta
subject_scope: artifact-model
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-089
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-080
      - CAPRMADIO-REQUIREMENT-META-131
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-100
      - CAPRMADIO-REQUIREMENT-META-133
---

# Requirement — Coordinate artifacts without an 81-Type bijection

Every governed artifact occupies exactly one semantic coordinate:

```text
Artifact form x Content role x Governance locus
```

The Cartesian product of three Artifact forms, nine Content roles, and three
Governance loci describes 81 possible coordinates. It is a classification
space, not a mandate to invent 81 top-level Type names or admit every
coordinate.

`scope_path` remains an independent structural ownership coordinate. Direct
subtype, carrier format, priority, lifecycle condition, and provenance remain
qualifying properties rather than additional primary axes.

GOV registers admitted Types, subtypes, and coordinates. Writers and validators
fail closed on unknown, disabled, contradictory, or ambiguous registered
combinations, but they do not reject an intentionally empty coordinate.

## Primary claim

Artifact form, Content role, and Governance locus define an 81-coordinate
classification space whose routes are admitted only when semantically needed.

## Rationale

The nine-role model must preserve orthogonal classification without multiplying
types or forcing meaningless artifacts to populate every theoretical cell.
