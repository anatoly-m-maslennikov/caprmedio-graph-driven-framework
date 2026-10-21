---
subjects:
  governs: "Entity/Node/Continuant/Atom/Content Role: Plan.Autonomous Confidence Threshold"
  depends_on:
    ["Atom/Content Role: Plan/Type: Plan", "Autonomous Confidence Threshold", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Node/Continuant/Project.Framework Settings"]
version: 7
updated_at: "2026-10-19 15:53:37 +0400"
relations: {"relates_to": ["CA-M-271", "CA-R-1044"]}
atom_id: "CA-R-1587"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1587-CORE_META_MODEL-CORE--require-an-effective-confidence-threshold-for-plan-execution.md
  source_atom_id: CA-R-1587
  source_atom_revision: 7
  source_sha256: 4f70ceca29e8a1bd384b6a6310076fd6931203695556c1804b31bb912ad207c2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Require an effective confidence threshold for Plan execution

## Scope

autonomous Plan execution decisions.

## Claim

**every** autonomous Plan execution decision **must** resolve **=1** effective Autonomous Confidence Threshold from its applicable explicit **or** inherited source under CA-M-271.

## Details
