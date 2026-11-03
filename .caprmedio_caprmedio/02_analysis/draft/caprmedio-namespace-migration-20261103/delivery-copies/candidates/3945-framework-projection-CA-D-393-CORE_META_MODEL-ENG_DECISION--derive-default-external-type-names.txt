---
subjects:
  active: CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom.Type
  passive:
  - CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-1690
atom_id: CA-D-393
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-393-CORE_META_MODEL-ENG_DECISION--derive-default-external-type-names.md
  source_atom_id: CA-D-393
  source_atom_revision: 23
  source_sha256: a41256b49739dd0d1ebbdbd2fa2dba17ed1c8cfe0ca4be26a6f3f5a8aa2e10b4
  original_relations_sha256: b4bfcaf0f728812dfb598f500841b6f79cbc5173222acf7ef2ca5e3d51354bd1
---
## Summary

Derive default external Type names

## Claim scope

external Type names derived from internal Types.

## Claim

**when** an external Type name is derived from an internal Type, the derivation uses `external_<internal_type_name>`. **when** the internal Type is the Content Role's default, the derived name uses that registered default Type. a separately registered explicit external Type name is non-default **and** does **not** modify this derivation rule.
