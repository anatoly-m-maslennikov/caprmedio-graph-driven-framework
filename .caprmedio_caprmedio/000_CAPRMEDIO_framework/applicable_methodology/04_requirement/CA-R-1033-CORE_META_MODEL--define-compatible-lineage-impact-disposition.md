---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1033
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1033-CORE_META_MODEL--define-compatible-lineage-impact-disposition.md
  source_atom_id: CA-R-1033
  source_atom_revision: 28
  source_sha256: 5dc14361dd91eddf9302d729acafb2a9983b8a248b275cd2a93bde14b0b05e77
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define compatible Lineage Impact disposition

## Claim

### Prose Claim


`compatible` Lineage Impact dispositions.



When a Lineage Impact analysis addresses an Atom, `compatible` must mean the child remains valid against the parent Revision required by the gate and traversal stops without a child update; a pinned earlier Revision does not establish compatibility where the new Revision is required.

