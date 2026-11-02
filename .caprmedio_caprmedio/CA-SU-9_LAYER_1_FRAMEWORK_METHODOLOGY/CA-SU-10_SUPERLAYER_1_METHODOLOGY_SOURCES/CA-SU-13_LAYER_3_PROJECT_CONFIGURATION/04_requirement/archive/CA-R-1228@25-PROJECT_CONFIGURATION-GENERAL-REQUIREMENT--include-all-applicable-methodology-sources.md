---
subjects:
  governs: Applicable Methodology Source Set
  depends_on:
  - Methodology Source
  - Core Meta-Model
  - Subject/Domain/Node/Continuant/Scope Unit//PROJECT_CONFIGURATION
  - Subject/Domain/Node/Continuant/Selection//Extension Sources
  - Subject/Domain/Node/Continuant/Project.Framework Settings
version: 25
updated_at: 2026-10-24 05:54:58 +0400
relations: {}
atom_id: CA-R-1228@25
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
