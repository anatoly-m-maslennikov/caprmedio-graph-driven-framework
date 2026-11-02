---
subjects:
  governs: "Entity/Occurrent/Execution/Step Run"
  depends_on:
    ["Entity/Occurrent/Execution/Step Run", "Entity/Occurrent/Execution/Workflow Run", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Node/Atom/Content Role: Operations/Type: Action/Execution Kind", "Entity/Occurrent/Execution/Step Run.Execution Context", "Entity/Continuant/Node/Actor/Type: Operator", "Entity/Continuant/Node/History/Journal"]
version: 4
updated_at: "2026-10-18 03:34:00 +0400"
relations: {"relates_to": ["CA-R-1519", "CA-R-1520", "CA-R-1525", "CA-R-1527"]}
atom_id: "CA-R-1793"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
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
