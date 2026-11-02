---
subjects:
  governs: Entity/Object/Continuant/Selection//Methodology Sources
  depends_on:
  - Entity/Object/Continuant/Selection//Methodology Sources
  - Entity/Object/Continuant/Structural Unit/Scope Unit//CORE_META_MODEL
  - Entity/Object/Continuant/Structural Unit/Scope Unit//PROJECT_CONFIGURATION
  - Entity/Object/Continuant/Selection//Extension Sources
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Framework Settings
version: 32
updated_at: 2026-10-29 07:17:26 +0400
relations: {}
atom_id: CA-R-1228@32
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Include **all** applicable Methodology Sources

## Scope

The Applicable Methodology source set under current Framework Instance Settings.

## Claim

the Applicable Methodology source set **must** include CORE_META_MODEL, PROJECT_CONFIGURATION, **and** **every** installed Extension Source applicable under the current Framework Instance Settings. **when** **none** is applicable, the Extension contribution **is empty** **without** a rule requiring zero installed Extensions **or** a Carrier for an empty INSTALLED_EXTENSIONS collection.

## Details
