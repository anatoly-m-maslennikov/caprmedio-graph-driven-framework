---
subjects:
  governs: "Apply Structural Change"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Project.Structure", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Carrier", "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Goal", "Entity/Node/Continuant/History/Journal"]
version: 8
updated_at: "2026-10-19 15:56:36 +0400"
relations: {}
atom_id: "CA-O-014"
content_role: "Operations"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Action"
global_tier: 11
projection:
  source_carrier_path: ../../sources/003_PROJECT_CONFIGURATION/09_operations/CA-O-014-PROJECT_CONFIGURATION-ACTION--apply-structural-change.md
  source_atom_id: CA-O-014
  source_atom_revision: 8
  source_sha256: e07f5d7928a5dbf62c77f0115c890bdfefa4e2dbe0aa661da033cab6aeeae367
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Apply structural change

## Operation

Apply Structural Change **means** the Action that rechecks the authorized proposal against the unchanged selected source state **and** applies its accepted declarations, reference repairs, **and** explicitly included Carrier changes through one recoverable cutover. **if** the source state differs, required validation fails, **or** permission no longer covers the effects, it **must** stop **before** mutation. **if** a partial failure occurs, it **must** report the actual effects **and** use **only** the authorized recovery boundary; it **must not** delete unapproved contents, overwrite concurrent edits, reset the retry budget, **or** claim a completed migration. event evidence follows the applicable Journal model, **not** a second structural authority.

## Details
