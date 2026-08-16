---
subject_scopes:
  - requirement-topology
tier: core
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-116-preserve-strict-semantic-distinctions
    - CAPRMADIO-REQUIREMENT-120-preserve-bounded-meaning-across-structural-scales
    - CAPRMADIO-REQUIREMENT-140-apply-dry-across-caprmadio
---

# Govern tier-preserving Requirement relations

Every active Requirement `child_of` edge preserves applicability tier and the
ordered Layer topology:

- project Principles are the only Principles and have no parents;
- a Core may depend directly on an applicable project Principle;
- a Layer 1 Core may depend on a project Core;
- within one project, Layer, or Feature scope, a Standard may depend on a Core;
- between adjacent Layers, a Core may depend on a Core and a Standard may
  depend on a Standard; and
- no other tier combination or backward Layer edge is permitted.

The child stores the direct relation. Transitive ancestry and inverse children
are derived. Every active Principle and Core has at least one active child
through a permitted edge; farther-Layer ancestry must not be duplicated as a
direct relation.
