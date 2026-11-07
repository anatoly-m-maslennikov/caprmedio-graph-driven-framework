---
atom_id: CA-R-992
ref_id: CA-R-992
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Work Sequence Number
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Label'
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
  - CAPRMEDIO_MODEL <+ Atom.Local Scope Unit
  - CAPRMEDIO_MODEL <+ Atom.Target Scope Unit
tier: 2
relations:
  child_of:
  - CA-R-2712
status: Active
version: 36
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-992-CORE_META_MODEL-RULE--separate-work-sequence-from-atom-identity.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-992-CORE_META_MODEL-RULE--separate-work-sequence-from-atom-identity.md
  source_atom_id: CA-R-992
  source_atom_revision: 36
  source_sha256: 4723d077e1b6cf8ef4dd15ee9812f4b26c4210414f65f234ecaa9760ab73f4bc
  original_relations_sha256: 607d9f0a817daa4ba6363a6bd1ce73ec81a73a7d73fe8eba341496be82c68353
---
## Summary

Separate Work Sequence from Atom identity

## Claim

### Prose Claim


Work Sequence Numbers **and** Atom identity-related properties.


a Work Sequence Number **must not** establish **or** change Atom identity, Atom Scope, Claim Target Scope Unit, Type, authoring Subtype, decomposition, **or** blocking.
