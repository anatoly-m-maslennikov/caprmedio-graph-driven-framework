---
atom_id: CA-R-1608
ref_id: CA-R-1608@21
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Status'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern)
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
tier: 2
status: Archived
version: 21
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1608@21-CORE_META_MODEL-RULE--register-core-concern-status-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register Core Concern Status Values

## Claim

### Prose Claim


the Core Concern Status model.


the Core Concern Status model **must** inherit the allowed values of Atom.Header.Status and add (Resolved, Canceled).
