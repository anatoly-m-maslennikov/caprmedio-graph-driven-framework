---
subject_scopes:
  - artifact-model
tier: core
version: 1
updated_at: 2026-08-17 19:36:01
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  replacement_of:
    - CAPRMADIO-REQUIREMENT-META-089
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
---
# Coordinate artifacts without an 81 type bijection

Every governed artifact occupies exactly one semantic coordinate:

```text
Artifact form x Content role x Governance locus
```

The Cartesian product of three Artifact forms, nine Content roles, and three Governance loci describes 81 possible coordinates. It is a classification space, not a mandate to invent 81 top-level Type names or admit every coordinate.

`scope_path` remains an independent structural ownership coordinate. Direct subtype, carrier format, priority, lifecycle condition, and provenance remain qualifying properties rather than additional primary axes.

GOV registers admitted Types, optional direct subtypes, and their coordinates. The complete registered Type–subtype pair resolves exactly one semantic coordinate; a Type policy may require a direct subtype to complete that resolution. A subtype cannot create a fourth axis or inherit another subtype. Writers and validators fail closed on unknown, disabled, contradictory, or ambiguous registered combinations, but they do not reject an intentionally empty coordinate.
