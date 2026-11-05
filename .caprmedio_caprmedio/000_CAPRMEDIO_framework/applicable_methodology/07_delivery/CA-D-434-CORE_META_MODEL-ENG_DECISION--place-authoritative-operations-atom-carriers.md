---
atom_id: CA-D-434
ref_id: CA-D-434
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: Active
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-434-CORE_META_MODEL-DECISION--place-authoritative-operations-atom-carriers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-434-CORE_META_MODEL-ENG_DECISION--place-authoritative-operations-atom-carriers.md
  source_atom_id: CA-D-434
  source_atom_revision: 25
  source_sha256: f54e12032ff67f5ce5d6bd5e1fc18ec83f1976f145b745b0add71009b7b4d4b3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Place authoritative Operations Atom Carriers

## Claim

### Prose Claim


the placement of a current authoritative Operations Atom File Carrier.


a current authoritative Operations Atom File Carrier **must** reside **in** the `09_operations/` Content Role Directory directly under its owning Scope Unit. first-artifact directory materialization remains governed by CA-D-296-CORE_META_MODEL--materialize-content-role-directories-on-first-artifact; this placement does **not** replace the separately governed placement of projected copies **or** archived Revisions.
