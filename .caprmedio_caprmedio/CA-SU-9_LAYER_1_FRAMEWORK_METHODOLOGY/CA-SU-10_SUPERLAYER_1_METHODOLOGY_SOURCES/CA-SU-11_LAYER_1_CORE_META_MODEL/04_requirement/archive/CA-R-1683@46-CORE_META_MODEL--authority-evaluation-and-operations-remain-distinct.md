---
atom_id: CA-R-1683
ref_id: CA-R-1683@46
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ Entity
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Selection
  - CAPRMEDIO_MODEL <+ Atom.Header.Context.Role
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/History
  - CAPRMEDIO_MODEL <+ Package/Project Package
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Action)
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Workflow)
  - CAPRMEDIO_MODEL <+ Actor
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Evaluation)
tier: 1
relations:
  child_of:
  - CA-M-447
status: archived
version: 46
updated_at: 2026-11-10 14:38:45 +0400
carrier_destination:
  file:
    name: CA-R-1683@46-CORE_META_MODEL--authority-evaluation-and-operations-remain-distinct.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/archive
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Authority, Evaluation, and Operations remain distinct

## Claim

### Prose Claim


RMED Spec authority, CAPO Change content, concrete Implementation, actual executions, Verification judgments.


CAPRMEDIO **must** distinguish RMED Spec authority for governed Entities; CAPO Change content under CA-R-1549@21, including specific reusable Operations definitions under CA-R-2463; concrete Implementation; actual executions **and** their Journal Records carrying facts, state changes, **and** Claim-bound evidence; **and** Verification judgments about sufficiency **and** currentness. Evaluation results, evidence, dashboards, **and** Verification judgments **may** support, challenge, **or** invalidate reliance on a Claim, but **must not** themselves establish, edit, replace, **or** override semantic authority.
