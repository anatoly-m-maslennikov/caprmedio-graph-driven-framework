---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Structural Unit/Scope Unit
version: 21
updated_at: 2026-10-29 07:17:25 +0400
relations:
  child_of:
  - CA-D-361
atom_id: CA-D-374@21
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 6
type: Eng Decision
---
# Summary

Serialize instance Authority Mode selections

## Scope

an explicit Authority Mode selection in the Framework Instance Settings TOML Carrier.

## Claim

an explicit Authority Mode selection **in** the Framework Instance Settings TOML Carrier **must** use `authority_modes.default` for the instance default **or** `authority_modes.project` for the Project override. explicit per-unit overrides **must** use **only** that unit's `authority_mode` **in** authoritative Project Structure; legacy per-unit Settings fields **must not** remain a second selectable source.

## Details
