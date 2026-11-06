---
atom_id: CA-R-1460
ref_id: CA-R-1460
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
  - CAPRMEDIO_MODEL <+ Projection.Form
  - CAPRMEDIO_MODEL <+ Atom.Content
tier: 1
status: Active
version: 22
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1460-CORE_META_MODEL-RULE--separate-projection-derivation-from-carrier-materialization.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1460-CORE_META_MODEL--separate-projection-derivation-from-carrier-materialization.md
  source_atom_id: CA-R-1460
  source_atom_revision: 22
  source_sha256: 4c5a23a3812122caec15c8bcf4465c38abe44efb53be666297e426b113e2c34c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Separate Projection derivation from Carrier materialization

## Claim

### Prose Claim


the derivation of a Projection and its Carrier materialization.


the governing derivation logic of a Projection **must** remain distinct from its Carrier materialization strategy. whether **and** how its result is represented **or** persisted **in** Carriers does **not**, by itself, define the transformation **or** content-preservation behavior of that derivation, its semantic Type, **or** its refresh behavior; those remain determined by their applicable governing Claims. describing a derivation as direct **or** content-preserving does **not** select a persistence strategy.
