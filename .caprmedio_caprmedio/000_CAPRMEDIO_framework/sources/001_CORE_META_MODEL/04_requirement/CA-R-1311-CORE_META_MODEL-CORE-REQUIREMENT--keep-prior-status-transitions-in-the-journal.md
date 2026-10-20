---
subjects:
  governs: "Artifact.Status"
  depends_on:
    ["Entity/Node/Continuant/History/Journal"]
version: 16
updated_at: "2026-10-19 15:52:47 +0400"
relations: {}
atom_id: "CA-R-1311"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Keep Prior Status Transitions in the Journal

## Scope

Artifact Revision Status Properties and their prior transitions.

## Claim

an Artifact Revision **must** expose **only** its current Status as a current Property **and** **must** preserve prior Status transitions through Journal events.

## Details
