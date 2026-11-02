---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - Subject/Domain/Node/Continuant/Actor
  - Subject/Engineering/Action Execution/Tool Call Boundary
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Plan/Type: Plan'
  - Subject/Domain/Node/Continuant/History/Journal.Record
  - Subject/Engineering/Carrier
  - 'Atom/Content Role: Operations/Type: Action/Execution Kind'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - Subject/Domain/Node/Continuant/Atom
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - Subject/Domain/Node/Continuant/Atom.Substance
version: 17
updated_at: 2026-10-23 03:20:06 +0400
relations: {}
atom_id: CA-R-1452@17
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Core
status: Archived
author: Anatoly Maslennikov
global_tier: 9
type: Definition
---
# Summary

Define Action

## Scope

the definition of an Action.

## Claim

an Action **means** an Atom with Content Role Operations **and** Type Action whose Claim specifies one reusable operational building block with an explicit operational contribution **and** a justified boundary at the modeled responsibility **and** granularity **where** further division has no useful independently governed meaning. this atomic boundary is **not** a count of machine instructions **or** Tool calls; an arbitrary large procedure **without** that justified boundary is **not** an Action. the Action is distinct from an Actor, a Tool, a Task, a particular execution, a Journal Record, **and** a Carrier. its execution kind is defined under CA-R-1526; an Agentic Action **may** use Tools **without** making **every** call another Action **or** Step.

## Details
