---
subject_scopes:
  - requirement-topology
tier: core
version: 3
updated_at: 2026-08-17 19:48:08
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-140-apply-dry-across-caprmadio
---
# Govern tier-preserving Requirement relations

Every active Requirement `child_of` edge must preserve applicability tier and the project-declared structural hierarchy:

- the Project Goal is the only Goal and has no parent;
- Project Principles are the only Principles and depend directly on the Project Goal;
- a Core may depend directly on an applicable Project Principle;
- a descendant-scope Core may depend directly on an applicable ancestor-scope Core;
- within one structural scope, a Standard may depend on an applicable Core;
- a descendant-scope Standard may depend directly on an applicable ancestor-scope Standard; and
- no other tier combination, backward structural edge, or cross-branch ancestry edge is permitted.

A direct Project-Principle-to-Core edge records project-wide applicability. Child scopes do not restate inherited ancestry unless the direct dependency is materially necessary to the child claim.

The child stores each direct relation. Transitive ancestry and inverse children are derived, and transitive ancestors must not be duplicated as direct relations. The active `authority_mode` governs topology-completeness obligations; relation legality applies in both modes.
