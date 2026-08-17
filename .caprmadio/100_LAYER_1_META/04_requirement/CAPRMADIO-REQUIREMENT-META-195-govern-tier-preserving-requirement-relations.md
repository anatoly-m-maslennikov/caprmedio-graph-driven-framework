---
subject_scopes:
  - requirement-topology
tier: core
version: 5
updated_at: 2026-08-17 22:39:00
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-247-use-one-global-tier-number-for-rmad-authority
---
# Govern tier-preserving Requirement relations

Every active Requirement `child_of` edge must point to an applicable parent whose global tier number is no greater than the child's. Within one structural scope, the parent must have a lower global tier number. An equal-tier edge is permitted only when the parent occupies an ancestor structural scope, so a Layer Core may specialize a Project Standard and a Feature Core may specialize a Layer Standard. Cross-scope parents must belong to the child's ancestor path; backward and cross-branch authority edges are forbidden.

The child stores only materially necessary direct relations. Transitive ancestry and inverse children are derived and must not be duplicated. The active `authority_mode` governs topology-completeness obligations; relation legality applies in every mode.
