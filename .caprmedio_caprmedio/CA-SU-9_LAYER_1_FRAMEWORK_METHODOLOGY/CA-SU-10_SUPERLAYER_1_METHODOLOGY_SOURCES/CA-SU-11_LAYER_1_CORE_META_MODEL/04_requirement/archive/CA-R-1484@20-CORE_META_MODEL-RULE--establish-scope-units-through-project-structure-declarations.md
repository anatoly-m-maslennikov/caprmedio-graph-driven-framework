---
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Structure
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project.Settings
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Goal'
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Parent
  - Entity/Object/Continuant/Structural Unit/Scope Unit.Children
version: 20
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1484@20
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Rule
---
## Summary

Establish Scope Units through Project Structure declarations

## Claim scope

non-Project Scope Unit declarations in their owning Project Structure.

## Claim

**every** non-Project Scope Unit **must** have **`=1`** declaration **in** its owning Project Structure that supplies its unique Name, direct parent, Type, Label, applicable Local Order, navigation number, **and** authority/Implementation Folder bindings. the declaration establishes the unit independently of Goal coverage **and** Carrier materialization; these remain separately evaluated conditions. Project Settings establishes the root identity, **and** Project Structure **must not** redeclare it as a child. Name/Order Atoms **and** concrete binding Atoms **must not** coexist as independent authorities for the same declared values.
