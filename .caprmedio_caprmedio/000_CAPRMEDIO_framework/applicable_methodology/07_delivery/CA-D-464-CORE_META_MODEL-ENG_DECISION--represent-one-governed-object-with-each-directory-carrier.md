---
atom_id: CA-D-464
ref_id: CA-D-464
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Carrier/Directory
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Artifact
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ Atom
tier: 1
status: Active
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-464-CORE_META_MODEL-DECISION--represent-one-governed-object-with-each-directory-carrier.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-464-CORE_META_MODEL-ENG_DECISION--represent-one-governed-object-with-each-directory-carrier.md
  source_atom_id: CA-D-464
  source_atom_revision: 25
  source_sha256: 22b235aa4eb578b5e5d51d8c01e79744756025e95449502c6433f47a8d694bc2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Represent One Governed Object with Each Directory Carrier

## Claim

### Prose Claim


represented Directory Carriers and their governed object Revisions.


**every** represented Directory Carrier **must** carry **`=1`** governed object Revision: either one Structural Entity Revision **or**, **where** an applicable Delivery rule permits it, one Atom Revision; it **must not** establish a second object merely because it contains subordinate Carriers.
