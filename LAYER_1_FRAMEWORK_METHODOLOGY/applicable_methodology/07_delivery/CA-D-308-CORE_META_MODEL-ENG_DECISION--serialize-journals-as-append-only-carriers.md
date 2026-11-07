---
atom_id: CA-D-308
ref_id: CA-D-308
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Journal
  dependencies:
  - CAPRMEDIO_MODEL <+ Event Record
tier: 1
status: Active
version: 26
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-308-CORE_META_MODEL-DECISION--serialize-journals-as-append-only-carriers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-308-CORE_META_MODEL-ENG_DECISION--serialize-journals-as-append-only-carriers.md
  source_atom_id: CA-D-308
  source_atom_revision: 26
  source_sha256: c60a8df0cef0176b1dc2970048ad9fa7cc679c8e3c1158405158c32d6140087c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Journals as Append-Only Carriers

## Claim

### Prose Claim


Journal Carriers.


**every** Journal Carrier **must** serialize its ordered Records append-only **in** its registered format **and** **must not** rewrite an admitted Record.
