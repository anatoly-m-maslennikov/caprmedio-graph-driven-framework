---
subjects:
  governs: Default Settings
  depends_on:
  - Default Settings
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Engineering/Carrier
version: 12
updated_at: 2026-10-24 00:38:25 +0400
relations:
  child_of:
  - CA-D-407
  relates_to:
  - CA-D-361
  - CA-D-368
  - CA-D-369
  - CA-D-374
  - CA-D-383
  - CA-D-387
atom_id: CA-D-408@12
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
---
# Summary

Reuse framework parameter fields in Default Settings

## Scope

parameter values in the Default Settings TOML Carrier.

## Claim

**every** parameter value **in** the Default Settings TOML Carrier **must** use the same registered section, field path, value type, **and** allowed domain as the corresponding explicit Framework Instance Settings parameter, **without** introducing a separate defaults-field schema.

## Details
