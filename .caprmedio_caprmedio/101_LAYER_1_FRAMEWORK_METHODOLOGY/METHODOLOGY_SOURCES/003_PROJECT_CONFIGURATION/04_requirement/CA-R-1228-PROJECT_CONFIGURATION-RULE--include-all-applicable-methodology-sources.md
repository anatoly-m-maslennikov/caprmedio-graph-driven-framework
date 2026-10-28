---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Methodology Sources
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Methodology Sources
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//CORE_META_MODEL
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit//PROJECT_CONFIGURATION
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection//Extension Sources
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Framework Settings
version: 31
updated_at: 2026-10-27 19:59:52 +0400
relations: {}
atom_id: CA-R-1228
content_role: Requirement
current_scope_unit: PROJECT_CONFIGURATION
claim_target_scope_unit: PROJECT_CONFIGURATION
status: Active
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
