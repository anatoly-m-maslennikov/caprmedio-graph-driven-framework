---
artifact_type: requirement
artifact_id: CARMADIO-REQUIREMENT-GOV-142
scope_path: layer:gov
subject_scopes:
  - artifact-catalog
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: replacement_of
    targets:
      - DSET-REQUIREMENT-GOV-078
  - type: child_of
    targets:
      - CARMADIO-REQUIREMENT-META-080
      - CARMADIO-REQUIREMENT-META-090
      - CARMADIO-REQUIREMENT-META-105
---

# Requirement — Register the Development Backlog Projection

GOV registers `development_backlog` as the internal planning Projection Type
with the Delivery Content role.

Each project has at most one active Development Backlog. Its carrier contains
one-line non-authoritative candidates grouped under unscheduled, current target
version, and future target version sections. It may link promoted Atoms but
cannot establish, restate, override, or satisfy their claims.

The Development Backlog is directly maintained under the governed release-
planning procedure. It declares no source frontier because its candidates are
planning inputs rather than a representation compiled from current authority.
Git records every persisted revision.

## Primary claim

`development_backlog` is the single internal Delivery-role planning Projection
Type for mutable future-work allocation.

## Rationale

A dedicated Projection Type preserves a cheap movable planning surface without
turning backlog lines into Atoms or overloading source-derived Catalog, Map, or
Hub Projections.
