---
atom_id: CA-D-304
ref_id: CA-D-304
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.ID
  - CAPRMEDIO_MODEL <+ Atom.Content
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: Active
version: 30
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-304-CORE_META_MODEL-DECISION--preserve-authority-through-carrier-only-recoding.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-304-CORE_META_MODEL-ENG_DECISION--preserve-authority-through-carrier-only-recoding.md
  source_atom_id: CA-D-304
  source_atom_revision: 30
  source_sha256: 5740063e9c6f5d68a142e6a515f99a735956158a10174da49c6a0753b71e2a90
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Preserve Authority through Carrier-Only Recoding

## Claim

### Prose Claim


Carrier-only recoding.


**every** Carrier-only recoding **must** preserve Atom identity, Claim, its textual Claim Scope, Claim Target Scope Unit, Atom Scope, **and** authored direct semantic relations **without** semantic change.
