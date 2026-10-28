---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Structure
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project.Settings
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Project
  - 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Goal'
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Parent
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Scope Unit.Children
version: 17
updated_at: 2026-10-27 19:59:56 +0400
relations: {}
atom_id: CA-R-1484
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 2
type: Rule
---
# Summary

Establish Scope Units through Project Structure declarations

## Scope

non-Project Scope Unit declarations in their owning Project Structure.

## Claim

**every** non-Project Scope Unit **must** have **`=1`** declaration **in** its owning Project Structure that supplies its unique Name, direct parent, Type, Label, applicable Local Order, navigation number, **and** authority/Implementation Folder bindings. the declaration establishes the unit independently of Goal coverage **and** Carrier materialization; these remain separately evaluated conditions. Project Settings establishes the root identity, **and** Project Structure **must not** redeclare it as a child. Name/Order Atoms **and** concrete binding Atoms **must not** coexist as independent authorities for the same declared values.

## Details
