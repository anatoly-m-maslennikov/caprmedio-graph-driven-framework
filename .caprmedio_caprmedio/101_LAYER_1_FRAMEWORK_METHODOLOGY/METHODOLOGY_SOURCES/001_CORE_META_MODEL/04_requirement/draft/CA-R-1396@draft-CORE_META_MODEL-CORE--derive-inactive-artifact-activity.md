---
subjects:
  governs: "Artifact.Activity: Inactive"
  depends_on:
    ["Artifact.Activity", "Artifact.Status"]
version: 11
updated_at: "2026-10-15 12:11:47 +0000"
relations: {}
atom_id: "CA-R-1396@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Derive Inactive Artifact Activity

## Scope

Artifacts for which Activity applies.

## Claim

an Artifact's Activity **must** be Inactive **if** Activity applies under CA-R-1307, its current Revision has **`=1`** valid Status from the applicable explicitly defined Status model, **and** that Status **`!=`** Active.

## Details
