---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Goal'
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Scope Unit
  - Subject/Graph Node/Domain/Continuant/Project.Structure
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Parent
  - Subject/Graph Node/Domain/Continuant/Scope Unit.Children
version: 33
updated_at: 2026-10-25 17:32:27 +0400
relations:
  child_of:
  - CA-R-925
atom_id: CA-R-926@33
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
