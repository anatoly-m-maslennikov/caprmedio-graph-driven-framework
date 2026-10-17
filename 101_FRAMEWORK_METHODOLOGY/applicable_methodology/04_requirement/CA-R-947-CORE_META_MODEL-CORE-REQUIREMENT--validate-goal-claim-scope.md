---
subjects:
  governs: "Entity/Continuant/Object/Atom.Target Scope Unit"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Requirement/Type: Goal", "Entity/Continuant/Object/Atom.Owning Scope Unit", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Project.Structure", "Entity/Continuant/Object/Project"]
version: 23
updated_at: "2026-10-16 12:08:57 +0000"
relations:
  child_of:
    - CA-R-925
    - CA-R-926
    - CA-R-927
atom_id: "CA-R-947"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 9
projection:
  source_carrier_path: ../../sources/001_CORE_META_MODEL/04_requirement/CA-R-947-CORE_META_MODEL-CORE-REQUIREMENT--validate-goal-claim-scope.md
  source_atom_id: CA-R-947
  source_atom_revision: 23
  source_sha256: bffe3f3b6c83065529e8d83e7422f9590a559e0cac57ce5831d0153af7e304e2
  original_relations_sha256: 5c9f7c8eabd47f3a1145066b2d404575be26ad76ec5f6fe4c4c68ec66380a8d6
---
# Summary
Validate Goal Claim Scope

## Scope

Goal Atoms.

## Claim

a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.

## Details
