---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Plan.Autonomous Confidence Threshold"
  depends_on:
    ["Atom/Content Role: Plan/Type: Plan", "Autonomous Confidence Threshold", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Object/Project.Framework Settings"]
version: 6
updated_at: "2026-10-15 18:44:45 +0000"
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
  source_atom_revision: 6
  source_sha256: 420eade5c66b82deaf3d751291ada6cb72813d27536ca95c67e79a9c78c387c2
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Require an effective confidence threshold for Plan execution

## Scope

autonomous Plan execution decisions.

## Claim

**every** autonomous Plan execution decision **must** resolve **=1** effective Autonomous Confidence Threshold from its applicable explicit **or** inherited source under CA-M-271.

## Details
