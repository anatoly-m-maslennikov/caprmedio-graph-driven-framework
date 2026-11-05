---
atom_id: CA-R-1542
ref_id: CA-R-1542
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  dependencies:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Status: Backlog'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)/(.Header.Form := Plan)'
tier: 1
status: Active
version: 23
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1542-CORE_META_MODEL-RULE--define-plan-backlog.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Plan Backlog

## Claim

### Prose Claim


Plan Atoms retained for future work outside the current Plan Scope.


the Plan Backlog **means** Plan Atoms retained for future work outside the current Plan Scope, including standalone Plans **and** Plans with decomposition; a Version Label does **not** establish another Status.
