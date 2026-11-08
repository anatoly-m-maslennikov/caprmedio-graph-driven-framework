---
atom_id: CA-R-1599
ref_id: CA-R-1599
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Content.Definition of Done
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
tier: 2
status: Active
version: 24
updated_at: 2026-11-08 19:06:46 +0400
carrier_destination:
  file:
    name: CA-R-1599-CORE_META_MODEL-RULE--require-a-definition-of-done-for-every-plan.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1599-CORE_META_MODEL-RULE--require-a-definition-of-done-for-every-plan.md
  source_atom_id: CA-R-1599
  source_atom_revision: 24
  source_sha256: 844a584e8c7629f7d818a00e5c5212d2511e1325799541e0c0059c5f52bb40fb
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Require a Definition of Done for every Plan

## Claim

### Prose Claim


Plan Atoms other than Work Reports, including Hubs with no own work.


Every Plan Atom other than a Work Report **must** have **`=1`** Definition of Done, including a Hub with no own work.
