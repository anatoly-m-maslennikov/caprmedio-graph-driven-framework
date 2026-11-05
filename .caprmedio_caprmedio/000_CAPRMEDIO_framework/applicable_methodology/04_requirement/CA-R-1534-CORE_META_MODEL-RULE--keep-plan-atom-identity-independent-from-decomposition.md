---
atom_id: CA-R-1534
ref_id: CA-R-1534
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
tier: 1
status: Active
version: 22
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1534-CORE_META_MODEL-RULE--keep-plan-atom-identity-independent-from-decomposition.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1534-CORE_META_MODEL-RULE--keep-plan-atom-identity-independent-from-decomposition.md
  source_atom_id: CA-R-1534
  source_atom_revision: 22
  source_sha256: 4757f675779a7560d0a947e1ed123d2be4de6fe408a629b80bcd95a38cd6ecb4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Plan Atom Identity Independent from Decomposition

## Claim

### Prose Claim


the identity of a Hub Atom **and** related decomposed Plan Atoms.


adding, removing, reordering, **or** changing a decomposed Plan Atom **must not** establish **or** replace the Hub Atom's identity; **every** related Atom retains its independent Claim **and** lifecycle.
