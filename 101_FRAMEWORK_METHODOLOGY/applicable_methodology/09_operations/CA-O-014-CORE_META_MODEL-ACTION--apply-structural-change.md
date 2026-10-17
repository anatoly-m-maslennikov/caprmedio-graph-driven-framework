---
subjects:
  governs: "Apply Structural Change"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Operations/Type: Action", "Entity/Continuant/Object/Project.Structure", "Entity/Continuant/Actor/Type: Operator", "Entity/Carrier", "Entity/Continuant/Object/Atom/Content Role: Requirement/Type: Goal", "Entity/Continuant/History/Journal"]
version: 6
updated_at: "2026-10-15 18:52:48 +0000"
relations: {}
atom_id: "CA-O-014"
content_role: "Operations"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/09_operations/CA-O-014-CORE_META_MODEL-ACTION--apply-structural-change.md
  source_atom_id: CA-O-014
  source_atom_revision: 6
  source_sha256: 98d669eec9c538d8a994f9a72c166d3778120d8d96bdee4d12d80eec2ed0a6f3
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Apply structural change

## Operation

Apply Structural Change **means** the Action that rechecks the authorized proposal against the unchanged selected source state **and** applies its accepted declarations, reference repairs, **and** explicitly included Carrier changes through one recoverable cutover. **if** the source state differs, required validation fails, **or** permission no longer covers the effects, it **must** stop **before** mutation. **if** a partial failure occurs, it **must** report the actual effects **and** use **only** the authorized recovery boundary; it **must not** delete unapproved contents, overwrite concurrent edits, reset the retry budget, **or** claim a completed migration. event evidence follows the applicable Journal model, **not** a second structural authority.

## Details
