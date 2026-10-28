---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Goal'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Parent
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Children
version: 34
updated_at: 2026-10-27 20:00:12 +0400
relations:
  child_of:
  - CA-R-925
atom_id: CA-R-926
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 5
type: Rule
---
# Summary
Let Direct Parents Define Non-Project Goals

## Scope

Non-Project Scope Units.

## Claim

**every** non-Project Scope Unit **must** have **`>=1`** accepted Goal Atom owned by its declared direct parent Scope Unit. this is a Goal-coverage obligation, **not** the source of the child's structural identity; a missing accepted Goal is a reported gap **and** **must not** remove **or** conceal the declared Scope Unit.

## Details
