---
subjects:
  governs: "Step Run/Invocation"
  depends_on:
    ["Step Run", "Workflow Run", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Action/Execution Kind", "Step/Agentic Execution Context", "Artifact/Revision", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/History/Journal"]
version: 2
updated_at: "2026-10-15 18:46:07 +0000"
relations: {"relates_to": ["CA-R-1519", "CA-R-1520", "CA-R-1525", "CA-R-1527"]}
atom_id: "CA-R-1791"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Keep Invocation delivery distinct from Step completion

## Scope

requests for participation **or** prompt delivery for an Agentic Step Invocation.

## Claim

requesting participation **or** returning a prompt **must not** itself complete a Step Run.

## Details
