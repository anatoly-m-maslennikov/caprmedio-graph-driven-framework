---
subjects:
  governs: "Entity/Continuant/Object/Scope Unit"
  depends_on:
    ["Entity/Continuant/Object/Project.Structure", "Entity/Continuant/Object/Project.Settings", "Entity/Continuant/Object/Project", "Entity/Continuant/Object/Atom/Content Role: Requirement/Type: Goal", "Entity/Continuant/Object/Scope Unit.Parent", "Entity/Continuant/Object/Scope Unit.Children"]
version: 7
updated_at: "2026-10-16 12:08:26 +0000"
relations: {}
atom_id: "CA-R-1484"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-1484-CORE_META_MODEL-GENERAL-REQUIREMENT--establish-scope-units-through-project-structure-declarations.md
  source_atom_id: CA-R-1484
  source_atom_revision: 7
  source_sha256: 80c80cf224a82ae977a2f57aac951cdae297532d4d5c66080d47c02ce792143c
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Establish Scope Units through Project Structure declarations

## Scope

non-Project Scope Unit declarations in their owning Project Structure.

## Claim

**every** non-Project Scope Unit **must** have **`=1`** declaration **in** its owning Project Structure that supplies its unique Name, direct parent, Type, Label, applicable Local Order, navigation number, **and** authority/Implementation Folder bindings. the declaration establishes the unit independently of Goal coverage **and** Carrier materialization; these remain separately evaluated conditions. Project Settings establishes the root identity, **and** Project Structure **must not** redeclare it as a child. Name/Order Atoms **and** concrete binding Atoms **must not** coexist as independent authorities for the same declared values.

## Details
