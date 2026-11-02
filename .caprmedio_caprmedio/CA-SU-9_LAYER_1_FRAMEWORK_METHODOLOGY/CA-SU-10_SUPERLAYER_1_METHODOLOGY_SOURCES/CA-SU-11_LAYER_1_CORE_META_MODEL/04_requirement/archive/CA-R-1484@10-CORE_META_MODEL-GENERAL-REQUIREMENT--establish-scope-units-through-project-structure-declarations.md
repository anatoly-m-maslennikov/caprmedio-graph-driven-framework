---
subjects:
  governs: Entity/Node/Continuant/Scope Unit
  depends_on:
  - Entity/Node/Continuant/Project.Structure
  - Entity/Node/Continuant/Project.Settings
  - Entity/Node/Continuant/Project
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Goal'
  - Entity/Node/Continuant/Scope Unit.Parent
  - Entity/Node/Continuant/Scope Unit.Children
version: 10
updated_at: 2026-10-23 03:06:32 +0400
relations: {}
atom_id: CA-R-1484@10
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Establish Scope Units through Project Structure declarations

## Scope

non-Project Scope Unit declarations in their owning Project Structure.

## Claim

**every** non-Project Scope Unit **must** have **`=1`** declaration **in** its owning Project Structure that supplies its unique Name, direct parent, Type, Label, applicable Local Order, navigation number, **and** authority/Implementation Folder bindings. the declaration establishes the unit independently of Goal coverage **and** Carrier materialization; these remain separately evaluated conditions. Project Settings establishes the root identity, **and** Project Structure **must not** redeclare it as a child. Name/Order Atoms **and** concrete binding Atoms **must not** coexist as independent authorities for the same declared values.

## Details
