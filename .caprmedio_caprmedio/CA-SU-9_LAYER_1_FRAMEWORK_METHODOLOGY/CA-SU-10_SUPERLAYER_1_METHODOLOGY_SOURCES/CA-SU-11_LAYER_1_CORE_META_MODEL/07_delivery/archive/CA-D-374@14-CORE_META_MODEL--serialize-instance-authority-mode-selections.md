---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Framework Settings
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Structure
  - Authority Mode
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Scope Unit
version: 14
updated_at: 2026-10-24 00:38:25 +0400
relations:
  child_of:
  - CA-D-361
atom_id: CA-D-374@14
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Serialize instance Authority Mode selections

## Scope

an explicit Authority Mode selection in the Framework Instance Settings TOML Carrier.

## Claim

an explicit Authority Mode selection **in** the Framework Instance Settings TOML Carrier **must** use `authority_modes.default` for the instance default **or** `authority_modes.project` for the Project override. explicit per-unit overrides **must** use **only** that unit's `authority_mode` **in** authoritative Project Structure; legacy per-unit Settings fields **must not** remain a second selectable source.

## Details
