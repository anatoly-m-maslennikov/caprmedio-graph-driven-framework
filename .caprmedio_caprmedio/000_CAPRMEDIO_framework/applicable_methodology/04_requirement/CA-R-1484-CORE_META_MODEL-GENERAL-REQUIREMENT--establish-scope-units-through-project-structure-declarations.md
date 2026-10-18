---
subjects:
  governs: "Entity/Continuant/Node/Scope Unit"
  depends_on:
    ["Entity/Continuant/Node/Project.Structure", "Entity/Continuant/Node/Project.Settings", "Entity/Continuant/Node/Project", "Entity/Continuant/Node/Atom/Content Role: Requirement/Type: Goal", "Entity/Continuant/Node/Scope Unit.Parent", "Entity/Continuant/Node/Scope Unit.Children"]
version: 8
updated_at: "2026-10-18 03:33:34 +0400"
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
  source_atom_revision: 8
  source_sha256: 72bd10a48027c533b7ab9081caa362fbeb501012fa449813d071753a27193a33
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
# Summary

Establish Scope Units through Project Structure declarations

## Scope

non-Project Scope Unit declarations in their owning Project Structure.

## Claim

**every** non-Project Scope Unit **must** have **`=1`** declaration **in** its owning Project Structure that supplies its unique Name, direct parent, Type, Label, applicable Local Order, navigation number, **and** authority/Implementation Folder bindings. the declaration establishes the unit independently of Goal coverage **and** Carrier materialization; these remain separately evaluated conditions. Project Settings establishes the root identity, **and** Project Structure **must not** redeclare it as a child. Name/Order Atoms **and** concrete binding Atoms **must not** coexist as independent authorities for the same declared values.

## Details
