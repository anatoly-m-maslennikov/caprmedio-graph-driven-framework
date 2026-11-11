---
atom_id: CA-R-1947
ref_id: CA-R-1947
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.State.Status
tier: 2
relations:
  child_of:
  - CA-R-1174
status: Active
version: 13
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1947-CORE_META_MODEL-RULE--define-atom-status-allowed-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Atom.Status allowed values

## Claim

### Prose Claim


The base allowed values inherited by narrower Atom kinds.


Atom.Header.Status **must** admit (Draft, Active, Archived). Narrower Atom kinds inherit these values and **may** add allowed values under their applicable Content Role or Type. An inherited value does **not** require a separate declaration for every narrower kind.

## Details

CA-R-1412 requires exactly one Status but does not declare the base allowed values. CA-R-1309 declares Draft, Active and Archived only for Requirements; it must not be retargeted to all Atoms as a Subjects-only change.
