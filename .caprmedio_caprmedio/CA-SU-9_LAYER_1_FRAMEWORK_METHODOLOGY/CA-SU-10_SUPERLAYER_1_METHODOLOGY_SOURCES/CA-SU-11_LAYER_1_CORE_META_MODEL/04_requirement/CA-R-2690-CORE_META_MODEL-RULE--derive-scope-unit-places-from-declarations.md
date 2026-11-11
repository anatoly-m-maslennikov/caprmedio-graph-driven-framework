---
atom_id: CA-R-2690
ref_id: CA-R-2690
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier/Directory
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery)
tier: 3
status: Active
version: 3
updated_at: "2026-11-07 15:28:42 +0400"
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-R-2690-CORE_META_MODEL-RULE--derive-scope-unit-places-from-declarations.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Derive Scope Unit places from Declarations

## Claim

Each non-Project Scope Unit within the Project has Authority and Delivery folders derived from its governing Scope Delegation. Delivery Atoms govern representation, placement, and general Carrier conventions without repeating a unit's selected paths.
