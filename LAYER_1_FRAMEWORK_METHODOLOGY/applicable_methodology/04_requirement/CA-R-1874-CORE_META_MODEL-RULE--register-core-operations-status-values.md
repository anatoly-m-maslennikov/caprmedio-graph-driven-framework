---
atom_id: CA-R-1874
ref_id: CA-R-1874
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations).Header.Status'
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations).Header.Form'
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Extension Sources
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
tier: 2
status: Active
version: 19
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1874-CORE_META_MODEL-RULE--register-core-operations-status-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1874-CORE_META_MODEL-RULE--register-core-operations-status-values.md
  source_atom_id: CA-R-1874
  source_atom_revision: 19
  source_sha256: 9a38fe341cc9ad2a9ed417339810982336de1703941708d9428e3cd16e223190
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Core Operations Status Values

## Claim

### Prose Claim


the default Status value domain of Operations Atoms with Type Workflow, Step, or Action.


the Core allowed values of Operations Status **must** be exactly (Draft, Active, Archived); that one Content Role Status model applies to Operations Atoms with Type Workflow, Step, or Action unless an admitted Extension or Project Configuration establishes a more-specific Status domain under that exact Content Role and Type path.

## Details

this Status is the Artifact Revision Property of the Operations Atom itself. it does **not** define a Status transition, carrier placement, setting, or a Workflow, Step, or Action Run outcome, receipt, retry state, result, or completion state.
