---
atom_id: CA-R-2724
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
version: 2
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2724@2-WORKBENCH-RULE--expand-indexed-relation-references-with-complete-cycle-safe-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
updated_at: 2026-11-04 00:38:14 +0400
---
## Summary

Expand indexed Relation references with complete cycle-safe results

## Claim scope

Expansion of an unambiguous seed reference through indexed registered Relation Types.

## Claim

### Prose Claim

Relation expansion **must**:

- accept one unambiguous seed reference and one or more registered Relation Types.
- include the seed and every reachable typed reference exactly once across all selected Relation Types and directions.
- terminate on cycles.
- return references, not fetched Atom or Scope Unit copies.
- use only indexed Relation facts; it **must not** infer links from prose or interpret Formal Claims as graph declarations.
- resolve each declared derived counterpart from its direct source fact without creating a second direct fact or traversing an inverse twice.
- reflect the applicable source and Declaration state after its query Projection is refreshed.
