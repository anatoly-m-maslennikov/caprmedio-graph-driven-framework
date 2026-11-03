---
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Plan.Status'
  passive:
  - Atom/(.Role := Plan)
  - Atom.Status
version: 22
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1539
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1539-CORE_META_MODEL-RULE--register-core-plan-status-values.md
  source_atom_id: CA-R-1539
  source_atom_revision: 22
  source_sha256: e89153213dd3cc02d14782a20230dc6cbca32fa451853ad77b4ab96abff271ed
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Core Plan Status Values

## Claim scope

Core Plan Status values.

## Claim

the Core Plan Status model **must** inherit the allowed values of Atom.Status and add (Backlog, Done, Canceled). Planned **must not** be a distinct Plan Status.
