---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Actor
  - Subject/Graph Node/Engineering/Action Execution/Tool Call Boundary
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Graph Node/Domain/Continuant/History/Journal.Record
  - Subject/Graph Node/Engineering/Continuant/Carrier
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action/Execution Kind'
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Graph Node/Domain/Continuant/Atom
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Graph Node/Domain/Continuant/Atom.Content
version: 23
updated_at: 2026-10-26 17:20:40 +0400
relations: {}
atom_id: CA-R-1452@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Definition
tier: 1
---
# Summary

Define Action

## Scope

the definition of an Action.

## Claim

an Action **means** an Atom with Content Role Operations **and** Type Action whose Claim specifies one reusable operational building block with an explicit operational contribution **and** a justified boundary at the modeled responsibility **and** granularity **where** further division has no useful independently governed meaning. this atomic boundary is **not** a count of machine instructions **or** Tool calls; an arbitrary large procedure **without** that justified boundary is **not** an Action. the Action is distinct from an Actor, a Tool, a Task, a particular execution, a Journal Record, **and** a Carrier. its execution kind is defined under CA-R-1526; an Agentic Action **may** use Tools **without** making **every** call another Action **or** Step.

## Details

The Action remains a separate reusable definition. multiple Steps, including Steps in different Workflows, **may** reference the same Action **without** copying **or** redefining its behavior.
