---
atom_id: CA-R-1315
ref_id: CA-R-1315
container:
  scope_unit: CA-SU-13
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//Methodology Sources
  dependencies:
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  - CAPRMEDIO_MODEL <+ Atom.Header.State.Status
tier: 2
status: Active
version: 31
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1315-PROJECT_CONFIGURATION-RULE--select-only-current-active-rmedo-atom-revisions.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-13_LAYER_3_PROJECT_CONFIGURATION/04_requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
---
## Summary

Select Only Current Active RMEDO Atom Revisions

## Claim

### Prose Claim


Applicable Methodology membership selections.


the Applicable Methodology membership **must** contain **only** current Atom Revisions whose type-qualified Status **`=`** Active **and** whose Content Role is **in** (Requirement, Method, Evaluation, Delivery, Operations).
