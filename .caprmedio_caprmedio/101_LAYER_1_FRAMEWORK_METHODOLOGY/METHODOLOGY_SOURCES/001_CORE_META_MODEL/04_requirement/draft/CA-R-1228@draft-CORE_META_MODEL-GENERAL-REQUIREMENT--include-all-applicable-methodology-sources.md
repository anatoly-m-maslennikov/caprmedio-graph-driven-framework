---
subjects:
  governs: "Applicable Methodology Source Set"
  depends_on:
    ["Methodology Source", "Core Meta-Model", "Project Configuration", "Extension", "Entity/Continuant/Object/Project.Framework Settings"]
version: 18
updated_at: "2026-10-15 18:12:59 +0000"
relations: {}
atom_id: "CA-R-1228@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Include **all** applicable Methodology Sources

## Scope

The Applicable Methodology source set under current Framework Instance Settings.

## Claim

the Applicable Methodology source set **must** include CORE_META_MODEL, PROJECT_CONFIGURATION, **and** **every** installed Extension Source applicable under the current Framework Instance Settings. **when** **none** is applicable, the Extension contribution **is empty** **without** a rule requiring zero installed Extensions **or** a Carrier for an empty INSTALLED_EXTENSIONS collection.

## Details
