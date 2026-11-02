---
subjects:
  governs: Entity/Object/Occurrent/Execution/Step Run
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow >{1+} Atom/Content Role: Operations/Type: Step >{0+} Atom/Content Role: Operations/Type: Sub-step'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
  - Entity/Object/Occurrent/Execution/Action Run
  - Entity/Object/Occurrent/Execution/Workflow Run
version: 22
updated_at: 2026-10-29 10:13:49 +0400
relations: {}
atom_id: CA-R-1511@22
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Entity Definition
tier: 1
---
## Summary

Define Step Run

## Claim scope

Actual executions of Steps within Workflow Runs.

## Claim

A Step Run is one actual execution of one Step within one enclosing Workflow Run. Every executed Step, including a containing Step, has its own distinct Step Run.

A leaf Step Run follows its Step's bound call target. An Action call executes through the corresponding Action Run; a Workflow call executes through the corresponding called Workflow Run. A containing Step Run executes its declared Sub-steps and makes no Action or Workflow call of its own; each Sub-step invokes its bound Action.

Separate executions of a Step are distinct Step Runs. Definitions remain reusable and are not copied for each execution. A recorded attempt or failure must not be represented as successful completion.

## Semantics

The enclosing Workflow Run and a Workflow Run called by a leaf Step are different execution roles. Calling a Workflow does not require an artificial wrapper Action or Action Run. The Step Run remains distinct from its definition and from Event Records describing it.
