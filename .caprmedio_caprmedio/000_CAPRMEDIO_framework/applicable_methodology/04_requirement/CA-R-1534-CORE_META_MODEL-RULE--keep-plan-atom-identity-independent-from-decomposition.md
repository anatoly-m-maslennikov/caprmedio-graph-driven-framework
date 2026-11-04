---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1534
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1534-CORE_META_MODEL-RULE--keep-plan-atom-identity-independent-from-decomposition.md
  source_atom_id: CA-R-1534
  source_atom_revision: 22
  source_sha256: 385c8ed08aa311e80a724b63e29bc122dec67e61d8949f012cfd3d1ef643f7cc
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Plan Atom Identity Independent from Decomposition

## Claim

### Prose Claim


the identity of a Hub Atom **and** related decomposed Plan Atoms.


adding, removing, reordering, **or** changing a decomposed Plan Atom **must not** establish **or** replace the Hub Atom's identity; **every** related Atom retains its independent Claim **and** lifecycle.
