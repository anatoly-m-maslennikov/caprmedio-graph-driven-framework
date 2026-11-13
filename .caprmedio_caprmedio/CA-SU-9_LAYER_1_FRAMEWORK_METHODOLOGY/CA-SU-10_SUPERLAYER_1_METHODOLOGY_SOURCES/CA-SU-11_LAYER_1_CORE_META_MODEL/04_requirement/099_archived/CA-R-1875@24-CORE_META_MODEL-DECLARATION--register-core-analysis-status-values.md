---
atom_id: CA-R-1875
ref_id: CA-R-1875@24
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := "Analysis and Advisory").Header.State.Status
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := "Analysis and Advisory")
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := "Analysis and Advisory").Header.Context.Form
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Extension Sources
  - CAPRMEDIO_STRUCTURE <+ Scope Unit//PROJECT_CONFIGURATION
tier: 2
status: archived
version: 24
updated_at: 2026-11-11 15:25:07 +0400
carrier_destination:
  file:
    name: CA-R-1875@24-CORE_META_MODEL-DECLARATION--register-core-analysis-status-values.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register Core Analysis Status Values

## Claim

### Prose Claim


the default Status value domain of Analysis and Advisory Atoms with Form Analysis Report or Rationale.


the Core Analysis and Advisory Status model **must** inherit the allowed values of Atom.Header.Status and add Done. That Role Status model applies to Analysis and Advisory Atoms with Form Analysis Report or Rationale. An admitted Extension or Project Configuration **may** add values under the applicable complete Role and Form path; it **must not** remove inherited values.

### Formal Claim

```CFEL
# model
Atom/(.Header.Context.Role in ("Analysis and Advisory"))/(.Header.Context.Form in (Analysis Report)).Header.State.Status :: Done;

Atom/(.Header.Context.Role in ("Analysis and Advisory"))/(.Header.Context.Form in (Rationale)).Header.State.Status :: Done
```

## Details

this Status belongs to the Analysis and Advisory Atom itself. It does **not** define a Status transition, carrier placement, setting, or a Workflow, Step, or Action Run outcome, receipt, retry state, result, or completion state. CA-R-1727@30 defines the meanings of Draft and Done for Analysis and the meaning of its archival.

