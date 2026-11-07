---
atom_id: CA-D-670
ref_id: CA-D-670
role: Delivery
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit
  dependencies:
  - Entity/Object/Continuant/History
  - CAPRMEDIO_MODEL <+ Journal
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 3
updated_at: "2026-11-07 15:28:42 +0400"
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-D-670-CORE_META_MODEL-ENG_DECISION--bind-scope-unit-declarations-to-source-evidence.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
---

## Summary

Bind Scope Unit Declarations to source evidence

## Claim

A Scope Unit structural source binding identifies the exact current Project Scope Unit Declaration or non-Project Scope Delegation bytes by SHA-256 digest. Readers determine current structure from those bytes. Journal events record history and do not determine whether the current structural Atom is readable.
