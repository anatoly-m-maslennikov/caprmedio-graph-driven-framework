---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-134
scope_path: layer:meta
subject_scope: artifact-model
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-089
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-117-admit-only-materially-distinct-framework-constructs
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

GOV registers admitted Types, optional direct subtypes, and their coordinates.
The complete registered Type–subtype pair resolves exactly one semantic
coordinate; a Type policy may require a direct subtype to complete that
resolution. A subtype cannot create a fourth axis or inherit another subtype.
Writers and validators fail closed on unknown, disabled, contradictory, or
ambiguous registered combinations, but they do not reject an intentionally
empty coordinate.

## Primary claim

Artifact form, Content role, and Governance locus define an 81-coordinate
classification space whose routes are admitted only when semantically needed.
