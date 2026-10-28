---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Actor
  - Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Architecture/Component Structure
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Plan/Type: Plan'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/History/Journal.Record
  - Subject/CAPRMEDIO/Carrier
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action/Execution Kind'
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Step'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Operations/Type: Action'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
version: 25
updated_at: 2026-10-27 19:59:55 +0400
relations: {}
atom_id: CA-R-1452
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
