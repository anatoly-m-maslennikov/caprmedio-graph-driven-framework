---
atom_id: CA-R-1788
ref_id: CA-R-1788
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Updated At
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
relations:
  child_of:
  - CA-R-1416
status: Active
version: 20
updated_at: 2026-11-03 23:25:51 +0400
carrier_destination:
  file:
    name: CA-R-1788-CORE_META_MODEL-RULE--initialize-version-creation-timestamp.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
claim_target_scope_unit: CORE_META_MODEL
current_scope_unit: CORE_META_MODEL
---
## Summary

Initialize Version creation timestamp

## Claim

### Prose Claim

Initialize Updated At to the actual Project-time creation instant when a new Atom Version is created. In-place edits, Status-only changes, archival, and promotion preserve the existing Version's Updated At. An ancestor-only move also preserves a descendant's Updated At. Timestamp encoding follows CA-D-270.
