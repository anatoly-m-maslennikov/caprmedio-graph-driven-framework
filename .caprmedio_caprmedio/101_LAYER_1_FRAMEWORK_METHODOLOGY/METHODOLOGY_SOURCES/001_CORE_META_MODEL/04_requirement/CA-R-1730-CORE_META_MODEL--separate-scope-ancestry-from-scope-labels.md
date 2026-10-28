---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Path
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Parent
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Children
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Label
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Actor/Type: Operator'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
version: 35
updated_at: 2026-10-27 20:00:02 +0400
relations:
  child_of:
  - CA-R-1776
atom_id: CA-R-1730
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
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
