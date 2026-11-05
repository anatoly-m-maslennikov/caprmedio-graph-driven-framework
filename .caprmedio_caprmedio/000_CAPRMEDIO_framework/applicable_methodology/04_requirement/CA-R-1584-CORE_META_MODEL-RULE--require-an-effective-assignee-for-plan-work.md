---
atom_id: CA-R-1584
ref_id: CA-R-1584
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Assignee'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Actor
tier: 1
status: Active
version: 23
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1584-CORE_META_MODEL-RULE--require-an-effective-assignee-for-plan-work.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1584-CORE_META_MODEL-RULE--require-an-effective-assignee-for-plan-work.md
  source_atom_id: CA-R-1584
  source_atom_revision: 23
  source_sha256: 67b525cdaa4d0d144eada3f7d40c67f5a1bc6b8f1843faae67ddf59ff18ce259
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Require an effective Assignee for Plan work

## Claim

### Prose Claim


Plan Atoms with their own work content, excluding pure Hubs **without** their own work.


**every** Plan Atom with its own work content **must** have **`=1`** effective Assignee; a pure Hub **without** its own work does **not** require an additional Assignee merely because it organizes other Plans.
