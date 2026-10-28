---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings.Authority Modes
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
version: 20
updated_at: 2026-10-27 19:59:24 +0400
relations:
  child_of:
  - CA-D-361
atom_id: CA-D-374
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
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
