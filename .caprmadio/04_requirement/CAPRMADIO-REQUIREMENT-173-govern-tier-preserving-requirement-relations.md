---
subject_scopes:
  - requirement-topology
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-140-apply-dry-across-caprmadio
---

# Govern tier-preserving Requirement relations

Every active Requirement `child_of` edge preserves applicability tier and the
ordered Layer topology:

- every Layer may consume applicable authority from PROJECT and any earlier
  Layer in the cumulative topology defined by CAPRMADIO-REQUIREMENT-065;
- project Principles are the only Principles and have no parents;
- a project or Layer Core may depend directly on an applicable project
  Principle;
- a Layer Core may depend on an applicable project Core;
- within one project, Layer, or Feature scope, a Standard may depend on a Core;
- between Layers, a Core may depend on a Core and a Standard may depend on a
  Standard from any earlier Layer when that dependency is direct; and
- no other tier combination or backward Layer edge is permitted.

A direct project-Principle-to-Core edge records project-wide applicability; it
does not require every intermediate Layer to restate that applicability.

The child stores the direct relation. Transitive ancestry and inverse children
are derived. Every active Principle and Core has at least one active child
through a permitted edge. Transitive ancestry must not be duplicated as a
direct relation.
