---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  passive:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan).Header.Status: Done'
version: 23
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1592
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1592-CORE_META_MODEL-RULE--keep-plan-completion-prerequisites-acyclic.md
  source_atom_id: CA-R-1592
  source_atom_revision: 23
  source_sha256: a4e8f93ba5f10e6e83c0dbea59155b943a35af967a87ca904d95504f53ab9074
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Keep Plan completion prerequisites acyclic

## Claim

### Prose Claim


Plan execution.


Plan execution **must not** contain a cycle of completion prerequisites, including one formed jointly by `BLOCKS` **and** the requirement **to** complete directly contained Plan work **before** its containing Plan can be Done **or** Canceled.
