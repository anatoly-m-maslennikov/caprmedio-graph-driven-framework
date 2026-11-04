---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Plan)
version: 32
updated_at: 2026-11-02 19:44:26 +0400
relations:
  child_of:
  - CA-R-1682
  - CA-R-1702
atom_id: CA-R-1691
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1691-CORE_META_MODEL-RULE--requirement-promote-active-backlog-candidates-into-atoms.md
  source_atom_id: CA-R-1691
  source_atom_revision: 32
  source_sha256: 23ef42295ea57072aafd6d061531f03714369a82a27c7e449f6693b655af198d
  original_relations_sha256: be92ea46e7c0624624be489e5359ed84dc27ef5c9d86897e368c45609f9cf496
---
## Summary

Requirement — Promote active backlog candidates into Atoms

## Claim

### Prose Claim


Development Backlog candidates selected into active work.


assigning a Development Backlog candidate **to** a current **or** future version does **not** establish governed truth. the candidate becomes active work **only** **when** the operator selects it **and** CAPRMEDIO creates **`=1`** bounded Task Atom for its action. execution **then** materializes the minimum Requirement, Method, Evaluation, Delivery, **or** future Operations Atoms needed **to** govern that work.

**`=1`** backlog line **may** produce multiple Atoms. multiple closely related backlog lines **may** produce **`=1`** Concern **or** RMED Atom **only** **when** they resolve **to** **`=1`** independently replaceable claim. Analysis & Advisory, Task, Implementation, **and** Operations use their separately governed atomicity models.

the backlog entry **may** link the resulting Atoms for navigation but remains a non-authoritative planning candidate **until** release finalization removes **or** reschedules it.

## Details

a Development Backlog candidate becomes active **only** through a bounded Task Atom; specification **or** other semantic authority arises **only** from the applicable CAPRMEDIO Atoms created **or** revised during execution.
