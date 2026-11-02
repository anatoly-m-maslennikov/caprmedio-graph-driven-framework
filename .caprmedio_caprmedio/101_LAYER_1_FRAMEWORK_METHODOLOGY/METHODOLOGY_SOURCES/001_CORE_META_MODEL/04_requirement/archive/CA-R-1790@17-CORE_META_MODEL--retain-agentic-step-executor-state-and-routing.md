---
subjects:
  governs: Entity/Object/Occurrent/Execution/Step Run
  depends_on:
  - Entity/Object/Occurrent/Execution/Step Run
  - Entity/Object/Occurrent/Execution/Workflow Run
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action.Execution Kind'
  - Entity/Object/Occurrent/Execution/Step Run.Execution Context
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Actor/Operator
  - Entity/Object/Continuant/History/Journal
version: 17
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1790@17
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Retain Agentic Step executor state **and** routing

## Claim scope

execution coordination during dispatch **or** resumption of an Agentic Step, involving the executor together with the participating session **or** separate Agent context.

## Claim

the executor **must** retain execution state **and** select subsequent Steps from the Workflow's declared transitions. the participating session **or** separate Agent context performs the requested Action; it need **not** reconstruct **or** remember what the Workflow will do next.
