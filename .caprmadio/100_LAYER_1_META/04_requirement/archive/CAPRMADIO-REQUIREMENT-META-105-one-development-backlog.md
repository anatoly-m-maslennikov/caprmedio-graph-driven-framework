---
artifact_type: requirement
artifact_id: CAPRMADIO-REQUIREMENT-META-105
scope_path: layer:meta
subject_scope: development-flow
priority: high
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  - type: child_of
    targets:
      - CAPRMADIO-REQUIREMENT-META-053
      - CAPRMADIO-REQUIREMENT-META-080
      - CAPRMADIO-REQUIREMENT-META-086
  - type: relates_to
    targets:
      - CAPRMADIO-REQUIREMENT-META-058
      - CAPRMADIO-REQUIREMENT-META-090
---

# Requirement — Keep one Development Backlog

The project has one Development Backlog with sections for unscheduled work,
the current target version, and any future target versions. Each entry is a
one-line candidate summary that may anticipate Requirement, Method, Assurance,
Delivery, Implementation, or Ops work.

The Development Backlog has the Delivery Content role and planning Projection
form. Its entries are non-authoritative candidates rather than Atoms and may be
added, removed, reordered, rewritten, or moved between version sections without
creating semantic authority.

A target-version heading is a mutable planning allocation, not a frozen
version scope or release claim.

## Primary claim

CAPRMADIO keeps exactly one freely mutable, non-authoritative Development
Backlog that groups one-line work candidates into unscheduled, current-version,
and future-version sections.

## Rationale

One planning surface keeps small future ideas cheap and movable without
creating short-lived Atoms or splitting backlog and roadmap truth across two
documents.
