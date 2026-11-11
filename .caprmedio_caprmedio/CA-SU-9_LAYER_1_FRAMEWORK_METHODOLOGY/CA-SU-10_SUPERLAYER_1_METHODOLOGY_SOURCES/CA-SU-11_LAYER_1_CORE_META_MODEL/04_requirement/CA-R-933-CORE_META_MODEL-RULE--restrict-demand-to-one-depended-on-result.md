---
atom_id: CA-R-933
ref_id: CA-R-933
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Demand)'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom
tier: 5
relations:
  child_of:
  - CA-R-932@37
status: Active
version: 33
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-933-CORE_META_MODEL-RULE--restrict-demand-to-one-depended-on-result.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary
Restrict Demand to one depended-on result

## Claim

### Prose Claim


Demand Atoms.


**every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Goal depends.
