---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Header.Status
  passive:
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Action)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow)'
  - 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/(.Header.Form := Workflow) >{1+} Atom/(.Header.Role := Operations)/(.Header.Form := Step)'
version: 28
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-R-1312
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1312-CORE_META_MODEL--separate-governed-transitions-from-status-values.md
  source_atom_id: CA-R-1312
  source_atom_revision: 28
  source_sha256: 3123f1baa6d1ed712357f00a2e8a4da521c29ffa78c5cefa02334513d3657a90
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary
Separate Governed Transitions from Status Values

## Claim

### Prose Claim

Artifact Revision Status values associated with admission, acceptance, commitment, activation, completion, **or** archival.

an Artifact Revision Status value **must** remain distinct from the Action **or** Workflow whose execution **may** establish that value.

## Details
the same distinction applies **when** a Workflow uses several Steps **to** establish the Status value.
