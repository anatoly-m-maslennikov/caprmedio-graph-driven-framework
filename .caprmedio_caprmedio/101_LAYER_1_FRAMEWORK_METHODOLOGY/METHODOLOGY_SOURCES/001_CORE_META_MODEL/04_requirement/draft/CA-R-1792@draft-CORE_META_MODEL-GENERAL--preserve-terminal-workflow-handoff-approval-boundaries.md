---
subjects:
  governs: "Step Run/Invocation"
  depends_on:
    ["Step Run", "Workflow Run", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Step", "Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Action/Execution Kind", "Step/Agentic Execution Context", "Artifact/Revision", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/History/Journal"]
version: 2
updated_at: "2026-10-15 18:20:43 +0000"
relations: {"relates_to": ["CA-R-1519", "CA-R-1520", "CA-R-1525", "CA-R-1527"]}
atom_id: "CA-R-1792@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Preserve terminal Workflow handoff approval boundaries

## Scope

a terminal Workflow handoff from an Agentic Step Invocation.

## Claim

a terminal Workflow handoff **must** end the predecessor Run **and** let the executor admit a separate successor under `CA-R-1520-CORE_META_MODEL-GENERAL-REQUIREMENT--return-workflow-handoffs-through-terminal-results`. a session instruction **must not** silently resume an ended Run **or** bypass approval.

## Details
