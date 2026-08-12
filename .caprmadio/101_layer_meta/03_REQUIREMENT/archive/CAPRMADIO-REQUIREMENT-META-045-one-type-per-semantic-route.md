---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-045
scope_path: layer:meta
subject_scope: artifact-model
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-043
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-035
---

# Requirement — Assign exactly one type to every semantic route

Each semantic route formed by one Revision mode, one Content role, and one
Governance locus has exactly one canonical `artifact_type`.

No second artifact type may map to the same route. Finer meanings that share
the route are direct `artifact_subtype` values of its canonical type. A subtype
inherits its parent type's complete route and cannot override any route axis.

The mapping is therefore unique in both directions:

- one registered artifact type maps to exactly one semantic route;
- one semantic route maps to exactly one registered artifact type.

Scope path, provenance, priority, lifecycle, and relations remain separate
metadata and do not create additional semantic routes.

## Rationale

A route must identify one stable governance category rather than merely select
dispatch policy. Direct subtypes preserve useful distinctions without allowing
several top-level names to compete for the same semantic coordinate.
