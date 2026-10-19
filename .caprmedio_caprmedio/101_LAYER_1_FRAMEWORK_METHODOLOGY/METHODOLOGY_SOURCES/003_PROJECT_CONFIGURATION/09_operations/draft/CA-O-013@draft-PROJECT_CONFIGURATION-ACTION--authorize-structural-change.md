---
subjects:
  governs: "Authorize Structural Change"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Project.Structure", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Actor/Type: AI Agent", "Autonomous Confidence Threshold"]
version: 8
updated_at: "2026-10-19 11:48:58 +0000"
relations: {}
atom_id: "CA-O-013@draft"
content_role: "Operations"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Draft"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
---
# Summary

Authorize structural change

## Operation

Authorize Structural Change **means** the Action that checks a structural change proposal against the Operator's actual authorization **and** the effective Autonomous Confidence Threshold, returning permission for the exact proposed effects **or** a blocked decision with its reason. existing authorization **may** cover those effects; a new approval **must** be requested **if** they exceed it, conflict resolution requires it, **or** uncertainty fails the effective threshold. approval **must** remain bound **to** the proposal **and** selected source state. this Action **must not** infer permission from a folder observation, a generated result, confidence alone, **or** the existence of a Plan.

## Details
