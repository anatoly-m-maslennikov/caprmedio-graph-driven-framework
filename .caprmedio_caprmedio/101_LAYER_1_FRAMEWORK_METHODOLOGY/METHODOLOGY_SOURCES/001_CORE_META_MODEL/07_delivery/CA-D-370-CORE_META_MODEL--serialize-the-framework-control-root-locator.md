---
subjects:
  governs: Subject/Domain/Node/Continuant/Project.Framework Settings.Framework Control-Root Locator
  depends_on:
  - Subject/Domain/Node/Continuant/Project.Framework Settings
  - Subject/Domain/Node/Continuant/Project
  - Subject/Engineering/Carrier/Directory Carrier
version: 18
updated_at: 2026-10-24 02:14:24 +0400
relations:
  child_of:
  - CA-D-361
atom_id: CA-D-370
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 6
type: Eng Decision
---
# Summary

Serialize the framework control-root locator

## Scope

the framework control-root locator for a Project in the Framework Instance Settings TOML Carrier.

## Claim

the Framework Instance Settings TOML Carrier **must** encode the framework control-root locator for its Project, resolving **to** the Directory Carrier prescribed by CA-D-317 **without** selecting a different authority root.

## Details
