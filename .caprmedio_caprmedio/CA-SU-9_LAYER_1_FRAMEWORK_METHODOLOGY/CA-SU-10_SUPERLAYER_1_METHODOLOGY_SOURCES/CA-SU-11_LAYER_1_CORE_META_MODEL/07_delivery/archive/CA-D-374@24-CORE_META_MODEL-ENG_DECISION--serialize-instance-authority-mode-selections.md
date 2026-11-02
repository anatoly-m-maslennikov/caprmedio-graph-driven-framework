---
subjects:
  active: Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  passive:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings.Authority Modes
  - Project
  - Scope Unit
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations:
  child_of:
  - CA-D-361
atom_id: CA-D-374@24
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
tier: 6
role: Delivery
form: Decision
---
## Summary

Serialize instance Authority Mode selections

## Claim scope

an explicit Authority Mode selection in the Framework Instance Settings TOML Carrier.

## Claim

an explicit Authority Mode selection **in** the Framework Instance Settings TOML Carrier **must** use `authority_modes.default` for the instance default **or** `authority_modes.project` for the Project override. explicit per-unit overrides **must** use **only** that unit's `authority_mode` **in** authoritative Project Structure; legacy per-unit Settings fields **must not** remain a second selectable source.
