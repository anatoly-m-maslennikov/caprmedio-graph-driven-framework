---
subject_scopes:
  - requirement-topology
tier: core
version: 1
updated_at: 2026-08-20 05:09:11
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMEDIO-REQU-049--use-one-global-tier-number-for-rmed-authority
---
# Govern tier-preserving RMEDO relations

Every active tier-classified RMEDO Atom `child_of` edge must point to an applicable parent whose global tier number is no greater than the child's. Within one structural scope, the parent must have a lower global tier number. An equal-tier edge is permitted only when a child Structural unit's Goal specializes its immediate parent Structural unit's Standard. Cross-scope parents must belong to the child's ancestor path; backward and cross-branch authority edges are forbidden.
