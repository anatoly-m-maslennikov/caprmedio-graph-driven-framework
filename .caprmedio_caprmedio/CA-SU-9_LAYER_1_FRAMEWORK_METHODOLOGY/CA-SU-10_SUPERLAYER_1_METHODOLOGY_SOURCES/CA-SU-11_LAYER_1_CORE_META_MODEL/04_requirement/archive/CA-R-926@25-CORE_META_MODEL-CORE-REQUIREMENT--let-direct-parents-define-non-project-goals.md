---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Goal'
  depends_on:
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Domain/Node/Continuant/Project.Structure
  - Entity/Node/Continuant/Atom.Substance
  - Subject/Domain/Node/Continuant/Scope Unit.Parent
  - Subject/Domain/Node/Continuant/Scope Unit.Children
version: 25
updated_at: 2026-10-23 03:14:50 +0400
relations:
  child_of:
    - CA-R-925
atom_id: CA-R-926@25
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary
Let Direct Parents Define Non-Project Goals

## Scope

Non-Project Scope Units.

## Claim

**every** non-Project Scope Unit **must** have **`>=1`** accepted Goal Atom owned by its declared direct parent Scope Unit. this is a Goal-coverage obligation, **not** the source of the child's structural identity; a missing accepted Goal is a reported gap **and** **must not** remove **or** conceal the declared Scope Unit.

## Details
