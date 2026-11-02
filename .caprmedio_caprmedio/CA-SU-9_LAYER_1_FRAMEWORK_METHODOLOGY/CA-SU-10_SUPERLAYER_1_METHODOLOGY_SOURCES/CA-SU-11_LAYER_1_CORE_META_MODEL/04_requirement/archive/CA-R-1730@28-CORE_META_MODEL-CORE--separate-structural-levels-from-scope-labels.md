---
subjects:
  governs: Subject/Domain/Node/Continuant/Scope Unit
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit.Path
  - Subject/Domain/Node/Continuant/Scope Unit.Parent
  - Subject/Domain/Node/Continuant/Scope Unit.Children
  - Subject/Domain/Node/Continuant/Scope Unit.Label
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
  - Subject/Domain/Node/Continuant/Project.Structure
version: 28
updated_at: 2026-10-24 01:37:42 +0400
relations:
  child_of:
  - CAPRMEDIO-REQU-031-CORE-REQUIREMENT--model-project-structure-as-numbered-levels
  - CA-R-1776
atom_id: CA-R-1730@28
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 1
type: Rule
---
# Summary

Separate scope ancestry from scope labels

## Scope

Scope Unit ancestry **and** Scope Unit Labels.

## Claim

Scope Unit ancestry **must** follow declared Scope Unit parentage. CAPRMEDIO **must not** author or persist a Structural Level property; an optional derived depth or path rendering **must not** independently override that parentage under CA-R-1485.

the Operator **may** choose **any** suitable Scope Unit Label, including `Layer`, `Feature`, `group`, `supergroup`, **or** `sub-feature`, **without** changing the unit's ancestry, authority, precedence, **or** Relation semantics. Labels **and** readability fields do **not** replace the active authority for those distinctions.

## Details
