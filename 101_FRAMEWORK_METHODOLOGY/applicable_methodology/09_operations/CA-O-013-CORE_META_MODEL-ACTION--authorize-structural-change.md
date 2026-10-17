---
subjects:
  governs: "Authorize Structural Change"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Project.Structure", "Entity/Continuant/Actor/Type: Operator", "Entity/Continuant/Actor/Type: AI Agent", "Autonomous Confidence Threshold"]
version: 6
updated_at: "2026-10-15 18:52:47 +0000"
relations: {}
atom_id: "CA-O-013"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-013-CORE_META_MODEL-ACTION--authorize-structural-change.md
  source_atom_id: CA-O-013
  source_atom_revision: 6
  source_sha256: e6d96d0de6d85f78da0df5d1a1be4e7475924c439c1ec7c0a3852fe58d41b99a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Authorize structural change

## Operation

Authorize Structural Change **means** the Action that checks a structural change proposal against the Operator's actual authorization **and** the effective Autonomous Confidence Threshold, returning permission for the exact proposed effects **or** a blocked decision with its reason. existing authorization **may** cover those effects; a new approval **must** be requested **if** they exceed it, conflict resolution requires it, **or** uncertainty fails the effective threshold. approval **must** remain bound **to** the proposal **and** selected source state. this Action **must not** infer permission from a folder observation, a generated result, confidence alone, **or** the existence of a Plan.

## Details
