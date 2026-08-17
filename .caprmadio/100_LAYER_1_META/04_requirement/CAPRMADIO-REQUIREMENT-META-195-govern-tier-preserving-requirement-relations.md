---
subject_scopes:
  - requirement-topology
tier: core
version: 4
updated_at: 2026-08-17 20:02:25
llm_session_ids:
  - codex:019f591f-04f6-70f2-8de7-828b7cccc69d
relations:
  child_of:
    - CAPRMADIO-REQUIREMENT-114-apply-mece-to-canonical-decompositions
    - CAPRMADIO-REQUIREMENT-140-apply-dry-across-caprmadio
---
# Govern tier-preserving Requirement relations

Every active Requirement `child_of` edge must preserve the project-configured applicability-tier order and the project-declared structural hierarchy:

- the external Goal is the singular hierarchy root at derived depth `-1` and has no parent;
- an Atom in the shallowest configured Project tier depends directly on the external Goal;
- within one structural scope, a tier-classified Atom may depend on an applicable Atom in a shallower configured tier;
- a descendant-scope Atom may depend directly on an applicable ancestor-scope Atom in the same configured tier; and
- no non-shallower same-scope edge, backward structural edge, or cross-branch ancestry edge is permitted.

A direct shallower-to-deeper tier edge records applicability. Child scopes do not restate inherited ancestry unless the direct dependency is materially necessary to the child claim.

The child stores each direct relation. Transitive ancestry and inverse children are derived, and transitive ancestors must not be duplicated as direct relations. The active `authority_mode` governs topology-completeness obligations; relation legality applies in both modes.
