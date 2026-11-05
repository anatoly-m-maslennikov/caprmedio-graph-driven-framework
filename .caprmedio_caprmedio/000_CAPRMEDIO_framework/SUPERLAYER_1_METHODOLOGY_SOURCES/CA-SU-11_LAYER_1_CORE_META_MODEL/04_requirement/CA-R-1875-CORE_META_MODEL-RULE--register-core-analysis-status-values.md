---
atom_id: CA-R-1875
ref_id: CA-R-1875
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory").Header.Status
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory")
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Role := "Analysis & Advisory").Header.Form
  - CAPRMEDIO_MODEL <+ Atom.Header.Status
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Extension Sources
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
tier: 2
status: Active
version: 22
updated_at: 2026-11-02 19:33:47 +0400
carrier_destination:
  file:
    name: CA-R-1875-CORE_META_MODEL-RULE--register-core-analysis-status-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register Core Analysis Status Values

## Claim

### Prose Claim


the default Status value domain of Analysis & Advisory Atoms with Form Analysis Report or Rationale.


the Core Analysis & Advisory Status model **must** inherit the allowed values of Atom.Header.Status and add Done. That Role Status model applies to Analysis & Advisory Atoms with Form Analysis Report or Rationale. An admitted Extension or Project Configuration **may** add values under the applicable complete Role and Form path; it **must not** remove inherited values.

## Details

this Status belongs to the Analysis & Advisory Atom itself. It does **not** define a Status transition, carrier placement, setting, or a Workflow, Step, or Action Run outcome, receipt, retry state, result, or completion state. CA-R-1727@30 defines the meanings of Draft and Done for Analysis and the meaning of its archival.

