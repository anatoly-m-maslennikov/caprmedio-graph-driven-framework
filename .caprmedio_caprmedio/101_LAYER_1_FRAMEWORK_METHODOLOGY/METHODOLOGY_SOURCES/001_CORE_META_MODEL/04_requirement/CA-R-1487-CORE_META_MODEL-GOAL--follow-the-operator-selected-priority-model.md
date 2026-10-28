---
version: 17
updated_at: 2026-10-27 19:59:56 +0400
relations:
  child_of:
  - CA-R-815
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//PROJECT_PRIORITY_MODEL
  depends_on:
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//PROJECT_PRIORITY_MODEL
atom_id: CA-R-1487
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Goal
---
# Summary

Follow the Operator-selected priority model

## Scope

priority-model selection by the CAPRMEDIO Framework Instance for an affected Scope and Project stage.

## Claim

the CAPRMEDIO Framework Instance **must** support the admissible priority model established by the Operator for the affected Scope **and** Project stage. **every** resulting alternative selection **must** satisfy **all** of the following:

- respect applicable authority **and** non-negotiable constraints.
- conform **to** that model, its effective parameters, **and** its active criteria **without** substituting another comparison algorithm.
- remain unresolved **if** the selected model **or** its application does **not** justify a selection.

## Details

the available criteria **and** comparison techniques remain extensible; no fixed criterion set **or** comparison by priority order is mandatory.
