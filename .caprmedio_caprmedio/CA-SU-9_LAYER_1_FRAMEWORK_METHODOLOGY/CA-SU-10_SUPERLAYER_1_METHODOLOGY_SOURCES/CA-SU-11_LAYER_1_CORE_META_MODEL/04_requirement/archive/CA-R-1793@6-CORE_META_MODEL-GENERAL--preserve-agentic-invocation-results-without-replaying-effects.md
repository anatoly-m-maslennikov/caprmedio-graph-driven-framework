---
subjects:
  governs: Entity/Node/Occurrent/Execution/Step Run
  depends_on:
  - Entity/Node/Occurrent/Execution/Step Run
  - Entity/Node/Occurrent/Execution/Workflow Run
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Step'
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Operations/Type: Action'
  - 'Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action/Execution Kind'
  - Entity/Node/Occurrent/Execution/Step Run.Execution Context
  - 'Entity/Node/Continuant/Actor/Type: Operator'
  - Entity/Node/Continuant/History/Journal
version: 6
updated_at: 2026-10-23 03:06:32 +0400
relations: {"relates_to": ["CA-R-1519", "CA-R-1520", "CA-R-1525", "CA-R-1527"]}
atom_id: CA-R-1793@6
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Preserve Agentic Invocation results **without** replaying effects

## Scope

repeated delivery **or** reconnection for an Agentic Step Invocation.

## Claim

the receiving context **must** report actual results against the identified Invocation. redelivery **or** reconnection **must not** imply permission **to** repeat already performed effects.

## Details
