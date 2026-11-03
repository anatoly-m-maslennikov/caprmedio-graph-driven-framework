---
version: 21
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-R-815
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_PRIORITY_MODEL
  passive:
  - CAPRMEDIO_MODEL <+ Entity/Object/Continuant/Actor/Operator
  - CAPRMEDIO_MODEL <+ Project
  - CAPRMEDIO_STRUCTURE <+ Entity/Object/Continuant/Selection//PROJECT_PRIORITY_MODEL
atom_id: CA-R-1487
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Requirement
form: Rule
---
## Summary

Follow the Operator-selected priority model

## Claim scope

priority-model selection by the CAPRMEDIO Framework Instance for an affected Scope and Project stage.

## Claim

the CAPRMEDIO Framework Instance **must** support the admissible priority model established by the Operator for the affected Scope **and** Project stage. **every** resulting alternative selection **must** satisfy **all** of the following:

- respect applicable authority **and** non-negotiable constraints.
- conform **to** that model, its effective parameters, **and** its active criteria **without** substituting another comparison algorithm.
- remain unresolved **if** the selected model **or** its application does **not** justify a selection.

## Details

the available criteria **and** comparison techniques remain extensible; no fixed criterion set **or** comparison by priority order is mandatory.
