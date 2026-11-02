---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Governing Configuration
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Governing Configuration
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Carrier
version: 19
updated_at: 2026-10-27 06:04:45 +0400
relations:
  child_of:
  - CA-D-407
atom_id: CA-D-408@19
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 4
type: Eng Decision
---
# Summary

Reuse framework parameter fields in Default Settings

## Scope

parameter values in the Default Settings TOML Carrier.

## Claim

**every** parameter value **in** the Default Settings TOML Carrier **must** use the same registered section, field path, value type, **and** allowed domain as the corresponding explicit Framework Instance Settings parameter, **without** introducing a separate defaults-field schema.

## Details
