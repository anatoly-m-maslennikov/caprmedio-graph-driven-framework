---
atom_id: CA-R-1294
ref_id: CA-R-1294
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Demand).Target Scope Unit'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
tier: 1
status: Active
version: 33
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1294-CORE_META_MODEL-RULE--derive-demand-direction-without-another-relation-kind.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Derive Demand Direction without Another Relation Kind

## Claim

### Prose Claim


Demand Atom directions.


a Demand Atom **must not** introduce a graph Relation Kind for its direction because its Consumer Atom Scope Unit **and** Producer Claim Target Scope Unit references determine that direction.
