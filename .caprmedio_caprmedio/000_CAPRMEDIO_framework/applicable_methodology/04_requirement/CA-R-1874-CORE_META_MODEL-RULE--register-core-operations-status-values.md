---
atom_id: CA-R-1874
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations.Status'
  passive:
  - Atom/(.Role := Operations)
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type'
  - Atom.Status
  - Entity/Object/Continuant/Selection//Extension Sources
  - Scope Unit//PROJECT_CONFIGURATION
version: 19
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1874-CORE_META_MODEL-RULE--register-core-operations-status-values.md
  source_atom_id: CA-R-1874
  source_atom_revision: 19
  source_sha256: 43f4195af243ae4e88194df69670c1099b1f5bd9bd26de3502886b98096a2c66
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Core Operations Status Values

## Claim scope

the default Status value domain of Operations Atoms with Type Workflow, Step, or Action.

## Claim

the Core allowed values of Operations Status **must** be exactly (Draft, Active, Archived); that one Content Role Status model applies to Operations Atoms with Type Workflow, Step, or Action unless an admitted Extension or Project Configuration establishes a more-specific Status domain under that exact Content Role and Type path.

## Details

this Status is the Artifact Revision Property of the Operations Atom itself. it does **not** define a Status transition, carrier placement, setting, or a Workflow, Step, or Action Run outcome, receipt, retry state, result, or completion state.
