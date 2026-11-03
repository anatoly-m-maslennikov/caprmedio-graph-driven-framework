---
atom_id: CA-R-1875
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: Atom/(.Role := "Analysis & Advisory").Status
  passive:
  - Atom/(.Role := "Analysis & Advisory")
  - Atom/(.Role := "Analysis & Advisory").Form
  - Atom.Status
  - Entity/Object/Continuant/Selection//Extension Sources
  - Scope Unit//PROJECT_CONFIGURATION
version: 22
updated_at: 2026-11-02 19:33:47 +0400
relations: {}
tier: 2
role: Requirement
form: Rule
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1875-CORE_META_MODEL-RULE--register-core-analysis-status-values.md
  source_atom_id: CA-R-1875
  source_atom_revision: 22
  source_sha256: 37e7f6571e2f675fbd099989d4f01aea7c1b59ec290547e30ef68cf2a88daece
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register Core Analysis Status Values

## Claim scope

the default Status value domain of Analysis & Advisory Atoms with Form Analysis Report or Rationale.

## Claim

the Core Analysis & Advisory Status model **must** inherit the allowed values of Atom.Status and add Done. That Role Status model applies to Analysis & Advisory Atoms with Form Analysis Report or Rationale. An admitted Extension or Project Configuration **may** add values under the applicable complete Role and Form path; it **must not** remove inherited values.

## Details

this Status belongs to the Analysis & Advisory Atom itself. It does **not** define a Status transition, carrier placement, setting, or a Workflow, Step, or Action Run outcome, receipt, retry state, result, or completion state. CA-R-1727@30 defines the meanings of Draft and Done for Analysis and the meaning of its archival.

