---
subjects:
  active: CAPRMEDIO_MODEL <+ Carrier
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - CAPRMEDIO_MODEL <+ Scope Unit
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-434
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-434-CORE_META_MODEL-ENG_DECISION--place-authoritative-operations-atom-carriers.md
  source_atom_id: CA-D-434
  source_atom_revision: 25
  source_sha256: ef7383cbf8eaa21e520dc7601e88737b4e75d3d9377a716e266f59a56c55e780
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Place authoritative Operations Atom Carriers

## Claim

### Prose Claim


the placement of a current authoritative Operations Atom File Carrier.


a current authoritative Operations Atom File Carrier **must** reside **in** the `09_operations/` Content Role Directory directly under its owning Scope Unit. first-artifact directory materialization remains governed by CA-D-296-CORE_META_MODEL--materialize-content-role-directories-on-first-artifact; this placement does **not** replace the separately governed placement of projected copies **or** archived Revisions.
