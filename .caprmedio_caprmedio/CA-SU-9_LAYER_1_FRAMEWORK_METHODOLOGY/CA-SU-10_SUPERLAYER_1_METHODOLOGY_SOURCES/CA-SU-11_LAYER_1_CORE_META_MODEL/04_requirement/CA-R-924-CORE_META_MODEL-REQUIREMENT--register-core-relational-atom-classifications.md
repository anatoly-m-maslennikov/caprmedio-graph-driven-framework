---
atom_id: CA-R-924
ref_id: CA-R-924
container:
  scope_unit: CA-SU-11
role: Requirement
form: Requirement
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context.Form
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Goal)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Requirement)/(.Header.Context.Form := Demand)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan)/(.Header.Context.Form := Plan)
tier: 4
relations:
  child_of:
  - CA-R-923
status: Active
version: 39
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-R-924-CORE_META_MODEL-REQUIREMENT--register-core-relational-atom-classifications.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Register Core Relational Atom Classifications

## Claim

### Prose Claim

The allowed qualified Relational Atom types in the Core Model include Requirement/Goal, Requirement/Demand, Plan/Plan, and Requirement/Scope Delegation, Method/Scope Delegation, Evaluation/Scope Delegation, Delivery/Scope Delegation and Operations/Scope Delegation.

A Scope Delegation is relational because its receiving Scope Unit differs from its direct containing Scope Unit. A Plan is relational only when its actual Claim target differs under the Relational Atom definition, not because it has decomposition, blocking or a particular Label.
