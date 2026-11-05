---
atom_id: CA-R-1487
ref_id: CA-R-1487
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_PRIORITY_MODEL
  dependencies:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_PRIORITY_MODEL
tier: 3
relations:
  child_of:
  - CA-R-815
status: Active
version: 21
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-R-1487-CORE_META_MODEL-RULE--follow-the-operator-selected-priority-model.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Follow the Operator-selected priority model

## Claim

### Prose Claim


priority-model selection by the CAPRMEDIO Framework Instance for an affected Scope and Project stage.


the CAPRMEDIO Framework Instance **must** support the admissible priority model established by the Operator for the affected Scope **and** Project stage. **every** resulting alternative selection **must** satisfy **all** of the following:

- respect applicable authority **and** non-negotiable constraints.
- conform **to** that model, its effective parameters, **and** its active criteria **without** substituting another comparison algorithm.
- remain unresolved **if** the selected model **or** its application does **not** justify a selection.

## Details

the available criteria **and** comparison techniques remain extensible; no fixed criterion set **or** comparison by priority order is mandatory.
