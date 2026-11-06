---
atom_id: CA-D-393
ref_id: CA-D-393
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Form
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Role
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
relations:
  child_of:
  - CA-R-1690
status: Active
version: 23
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-393-CORE_META_MODEL-DECISION--derive-default-external-type-names.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-393-CORE_META_MODEL-ENG_DECISION--derive-default-external-type-names.md
  source_atom_id: CA-D-393
  source_atom_revision: 23
  source_sha256: 5cfc7b3d787cfe22a813b1b2096016c0d1444353926376f5f4cf3f4ee407b8ec
  original_relations_sha256: b4bfcaf0f728812dfb598f500841b6f79cbc5173222acf7ef2ca5e3d51354bd1
---
## Summary

Derive default external Type names

## Claim

### Prose Claim


external Type names derived from internal Types.


**when** an external Type name is derived from an internal Type, the derivation uses `external_<internal_type_name>`. **when** the internal Type is the Content Role's default, the derived name uses that registered default Type. a separately registered explicit external Type name is non-default **and** does **not** modify this derivation rule.
