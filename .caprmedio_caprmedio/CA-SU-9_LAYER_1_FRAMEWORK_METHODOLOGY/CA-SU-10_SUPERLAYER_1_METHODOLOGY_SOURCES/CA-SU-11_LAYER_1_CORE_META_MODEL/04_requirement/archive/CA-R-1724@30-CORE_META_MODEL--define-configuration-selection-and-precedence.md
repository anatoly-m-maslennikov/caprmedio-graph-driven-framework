---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Project.Framework Settings
  - Subject/Graph Node/Domain/Continuant/Selection//Extension Sources
  - Subject/Graph Node/Engineering/Configuration/Tool Selection and Activation Precedence
version: 30
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-1724@30
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Rule
tier: 1
---
# Summary

Define Configuration selection and precedence

## Scope

Framework Instance Settings Artifact selection of available Tools **and** Extensions.

## Claim

the Framework Instance Settings Artifact **may** select, combine, parameterize, activate **in** foreground **or** background, **or** disable available Tools **and** Extensions **and** **must** resolve composition precedence explicitly **without** changing **any** selected capability's governed meaning. installation establishes availability, **not** activation: an installed Extension **may** remain disabled, **and** its retained settings do **not** enable it **unless** the Framework Instance Settings Artifact explicitly does so. the Framework Instance Settings Artifact **must** own the current activation selection **and** selected revision of **every** selected Extension.

## Details
