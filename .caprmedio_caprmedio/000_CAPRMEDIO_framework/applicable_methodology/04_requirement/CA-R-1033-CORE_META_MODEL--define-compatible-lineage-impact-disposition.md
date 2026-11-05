---
atom_id: CA-R-1033
ref_id: CA-R-1033
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 2
status: Active
version: 28
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1033-CORE_META_MODEL-RULE--define-compatible-lineage-impact-disposition.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1033-CORE_META_MODEL--define-compatible-lineage-impact-disposition.md
  source_atom_id: CA-R-1033
  source_atom_revision: 28
  source_sha256: 6722882d1d3ac42b9daf360531e2d7387209d3410d5af5adb86842f28ba9e942
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define compatible Lineage Impact disposition

## Claim

### Prose Claim


`compatible` Lineage Impact dispositions.



When a Lineage Impact analysis addresses an Atom, `compatible` must mean the child remains valid against the parent Revision required by the gate and traversal stops without a child update; a pinned earlier Revision does not establish compatibility where the new Revision is required.

