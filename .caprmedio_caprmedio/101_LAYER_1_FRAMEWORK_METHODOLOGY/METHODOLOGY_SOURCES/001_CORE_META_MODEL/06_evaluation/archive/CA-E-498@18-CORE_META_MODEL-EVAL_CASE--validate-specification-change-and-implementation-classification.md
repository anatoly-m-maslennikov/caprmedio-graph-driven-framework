---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom/Content Role
  depends_on:
  - Subject/Domain/Node/Continuant/Selection
  - Subject/Domain/Node/Continuant/Atom/Content Role
  - Subject/Domain/Node/Continuant/Atom.Content
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Workflow'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Engineering/Implementation
  - Subject/Engineering/Carrier
version: 18
updated_at: 2026-10-25 00:56:39 +0400
relations:
  evaluation_for:
  - CA-R-1548
  - CA-R-1549
  - CA-R-1550
  - CA-R-1339
  - CA-R-1340
  - CA-R-1343
  - CA-R-1530
  - CA-R-1569
atom_id: CA-E-498@18
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Eval Case
tier: 3
---
# Summary
Validate Specification, Change, and Implementation classification

## Scope
classification of an Atom by its Content Role.

## Claim
the classification Evaluation **must** fail **if** an Atom's Content Role does **not** match its actual contribution under the Specification, Change, **and** Implementation definitions.

- use the evaluated Atom's declared Content Role, complete Main Content, **and** applicable Specification, Change, **and** Implementation definitions as the input evidence.
- compare the declared Content Role with the contribution expressed **in** that Main Content, using the following classification table.
- report unresolved **when** required evidence is unavailable, unresolved, **or** contradictory; **otherwise**, report pass **if** the declared Content Role matches the observed contribution **and** fail **if** it does **not**.
- identify the evaluated Atom **and** report the declared Content Role, relevant content excerpt, applicable definition, **and** comparison result.

| Claim contribution | Expected classification |
|---|---|
| a model definition, required property, **or** permission governing a Concern, Analysis, Task, Action, **or** Workflow | Requirement |
| a convention for authoring **or** constructing that content | Method |
| a falsifiable correctness check | Evaluation |
| a Carrier's fields, format, **or** placement | Delivery |
| a particular unresolved issue, analytical finding, **or** intended Task | the matching Concern, Analysis, **or** Plan role |
| a particular reusable Action behavior, Workflow graph, Step invocation binding, **or** Actor participation/authorization behavior | Operations |
| a current realization of accepted specification | Implementation |

reusing the specified content's role as the specification's role **must** fail this check. a long-lived Concern **or** reusable Workflow **must not** fail merely because its lifetime is long.

## Details
