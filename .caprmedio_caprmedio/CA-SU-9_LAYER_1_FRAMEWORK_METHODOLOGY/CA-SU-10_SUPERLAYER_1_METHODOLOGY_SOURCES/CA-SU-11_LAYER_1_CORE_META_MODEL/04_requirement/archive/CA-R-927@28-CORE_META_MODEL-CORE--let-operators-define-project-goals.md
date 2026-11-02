---
subjects:
  governs: Entity/Node/Continuant/Scope Unit
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Target Scope Unit
  - Entity/Node/Continuant/Atom.Author
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Goal'
  - Entity/Node/Continuant/Atom.Owning Scope Unit
  - 'Entity/Node/Continuant/Actor/Type: Operator'
  - Entity/Node/Continuant/Project
version: 28
updated_at: 2026-10-23 03:06:32 +0400
relations:
  child_of:
    - CA-R-925
atom_id: CA-R-927@28
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Let Operators Define Project Goals

## Scope

Project Scope Units.

## Claim

**every** Project Scope Unit **must** be the Claim Target Scope Unit of **`>=1`** accepted Goal Atom whose Atom Scope **contains** no Scope Unit **and** whose Author is an Operator.

## Details
