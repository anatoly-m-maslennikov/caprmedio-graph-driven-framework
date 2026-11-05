---
atom_id: CA-D-327
ref_id: CA-D-327
container:
  scope_unit: CA-SU-13
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Directory
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Delivery)
tier: 3
status: Active
version: 23
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-327-PROJECT_CONFIGURATION-DECISION--use-the-project-root-only-for-delivery-carriers.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/07_delivery/CA-D-327-PROJECT_CONFIGURATION-ENG_DECISION--use-the-project-root-only-for-delivery-carriers.md
  source_atom_id: CA-D-327
  source_atom_revision: 23
  source_sha256: 01e004ff12aba3dc23133c9a85baa5184a6b287b18020c7e1ca4f24e1b3afd44
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Use the Project Root Only for Delivery Carriers

## Claim

### Prose Claim


Delivery Directory Carriers at the CAPRMEDIO Project root.


the CAPRMEDIO Project root **must** carry **only** Delivery Directory Carriers produced for Project Scope Units whose authority Carriers live under `.caprmedio_caprmedio/` **or** another registered Project-owned Carrier root.
