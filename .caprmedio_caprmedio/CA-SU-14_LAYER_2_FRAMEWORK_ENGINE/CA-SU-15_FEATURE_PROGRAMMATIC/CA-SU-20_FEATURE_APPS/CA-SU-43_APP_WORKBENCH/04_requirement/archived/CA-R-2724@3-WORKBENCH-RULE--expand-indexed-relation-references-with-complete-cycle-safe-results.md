---
atom_id: CA-R-2724
ref_id: CA-R-2724@3
container:
  scope_unit: CA-SU-43
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 3
status: Archived
version: 3
updated_at: 2026-11-05 18:48:47 +0400
carrier_destination:
  file:
    name: CA-R-2724@3-WORKBENCH-RULE--expand-indexed-relation-references-with-complete-cycle-safe-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archived
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Expand indexed Relation references with complete cycle-safe results

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
- use only `atoms` and `scope_units` as Relation-expansion source tables. The separate technical `change_log` table records watcher observations and is not a graph vertex, edge, Atom or Scope Unit source.

