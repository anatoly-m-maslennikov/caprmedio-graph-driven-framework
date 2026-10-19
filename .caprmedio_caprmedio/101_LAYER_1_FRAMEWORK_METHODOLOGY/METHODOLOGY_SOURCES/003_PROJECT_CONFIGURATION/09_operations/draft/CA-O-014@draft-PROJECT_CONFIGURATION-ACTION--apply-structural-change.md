---
subjects:
  governs: "Apply Structural Change"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Operations/Type: Action", "Entity/Node/Continuant/Project.Structure", "Entity/Node/Continuant/Actor/Type: Operator", "Entity/Carrier", "Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Goal", "Entity/Node/Continuant/History/Journal"]
version: 8
updated_at: "2026-10-19 11:48:58 +0000"
relations: {}
atom_id: "CA-O-014@draft"
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

Apply structural change

## Operation

Apply Structural Change **means** the Action that rechecks the authorized proposal against the unchanged selected source state **and** applies its accepted declarations, reference repairs, **and** explicitly included Carrier changes through one recoverable cutover. **if** the source state differs, required validation fails, **or** permission no longer covers the effects, it **must** stop **before** mutation. **if** a partial failure occurs, it **must** report the actual effects **and** use **only** the authorized recovery boundary; it **must not** delete unapproved contents, overwrite concurrent edits, reset the retry budget, **or** claim a completed migration. event evidence follows the applicable Journal model, **not** a second structural authority.

## Details
