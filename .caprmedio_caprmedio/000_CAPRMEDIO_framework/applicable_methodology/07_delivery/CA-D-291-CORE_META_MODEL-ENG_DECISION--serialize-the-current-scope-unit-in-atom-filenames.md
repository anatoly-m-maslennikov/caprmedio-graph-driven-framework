---
atom_id: CA-D-291
ref_id: CA-D-291
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Scope Unit
tier: 3
status: Active
version: 31
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-291-CORE_META_MODEL-DECISION--serialize-the-current-scope-unit-in-atom-filenames.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-291-CORE_META_MODEL-ENG_DECISION--serialize-the-current-scope-unit-in-atom-filenames.md
  source_atom_id: CA-D-291
  source_atom_revision: 31
  source_sha256: 6c64d825692cbf582a1ed4c6d52e495cbbe98a81b9556e47fc4fa8b259b472c1
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize the Current Scope Unit in Atom Filenames

## Claim

### Prose Claim


Project-owned Atom filenames for Carriers contained **in** Scope Units.


**every** Project-owned Atom filename **must** serialize the Scope Unit that **contains** its authoritative Carrier **`=1`** time **and** **must** omit that segment **if** the Carrier is **in** the Project Scope Unit.
