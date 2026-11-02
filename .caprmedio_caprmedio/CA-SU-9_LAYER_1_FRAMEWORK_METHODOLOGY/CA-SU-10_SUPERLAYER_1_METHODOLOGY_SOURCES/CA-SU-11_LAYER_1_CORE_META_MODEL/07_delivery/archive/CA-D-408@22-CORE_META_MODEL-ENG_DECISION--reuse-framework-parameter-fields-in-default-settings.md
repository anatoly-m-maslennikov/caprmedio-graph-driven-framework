---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Governing Configuration
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Governing Configuration
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
  - Entity/Carrier
version: 22
updated_at: 2026-10-29 07:45:30 +0400
relations:
  child_of:
  - CA-D-407
atom_id: CA-D-408@22
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 4
type: Decision
---
## Summary

Reuse framework parameter fields in Default Settings

## Claim scope

parameter values in the Default Settings TOML Carrier.

## Claim

**every** parameter value **in** the Default Settings TOML Carrier **must** use the same registered section, field path, value type, **and** allowed domain as the corresponding explicit Framework Instance Settings parameter, **without** introducing a separate defaults-field schema.

## Details
