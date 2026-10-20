---
subjects:
  governs: "Applicable Methodology Source Set"
  depends_on:
    ["Methodology Source", "Core Meta-Model", "Project Configuration", "Extension", "Entity/Node/Continuant/Project.Framework Settings"]
version: 20
updated_at: "2026-10-19 15:56:04 +0400"
relations: {}
atom_id: "CA-R-1228"
content_role: "Requirement"
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
local_tier: "General"
status: "Active"
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
