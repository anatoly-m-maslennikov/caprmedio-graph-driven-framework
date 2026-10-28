---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - Subject/CAPRMEDIO/Carrier
version: 5
updated_at: 2026-10-27 19:59:38 +0400
relations:
  evaluation_for:
  - CA-R-1548
  - CA-R-1549
  - CA-R-1550
  - CA-R-1339
  - CA-R-1340
  - CA-R-1530
  - CA-R-1569
atom_id: CA-E-658
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
type: Eval Case
tier: 3
---
# Summary
Validate Atom Content Role classification

## Scope
classification of an Atom by its Content Role.

## Claim
the classification Evaluation **must** fail **if** an Atom's Content Role does **not** match its actual contribution under the Specification **and** Change definitions.

- use the evaluated Atom's declared Content Role, complete Main Content, **and** applicable Specification **and** Change definitions as the input evidence.
- compare the declared Content Role with the contribution expressed **in** that Main Content, using the following classification table.
- report unresolved **when** required evidence is unavailable, unresolved, **or** contradictory; **otherwise**, report pass **if** the declared Content Role matches the observed contribution **and** fail **if** it does **not**.
- identify the evaluated Atom **and** report the declared Content Role, relevant content excerpt, applicable definition, **and** comparison result.

| Claim contribution | Expected classification |
|---|---|
| a model definition, required property, permission, **or** Actor participation/authorization policy governing a Concern, Analysis, Task, Action, **or** Workflow | Requirement |
| a convention for authoring **or** constructing that content | Method |
| a falsifiable correctness check | Evaluation |
| a Carrier's fields, format, **or** placement | Delivery |
| a particular unresolved issue, analytical finding, **or** intended Task | the matching Concern, Analysis, **or** Plan role |
| a particular reusable Action behavior, Workflow graph, **or** Step invocation binding | Operations |


reusing the specified content's role as the specification's role **must** fail this check. a long-lived Concern **or** reusable Workflow **must not** fail merely because its lifetime is long.

## Details
