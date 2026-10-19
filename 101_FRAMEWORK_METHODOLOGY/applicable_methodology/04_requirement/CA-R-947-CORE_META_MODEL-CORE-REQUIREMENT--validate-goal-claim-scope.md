---
subjects:
  governs: "Entity/Continuant/Node/Atom.Target Scope Unit"
  depends_on:
    ["Entity/Continuant/Node/Atom/Content Role: Requirement/Type: Goal", "Entity/Continuant/Node/Atom.Owning Scope Unit", "Entity/Continuant/Node/Scope Unit", "Entity/Continuant/Node/Project.Structure", "Entity/Continuant/Node/Project"]
version: 24
updated_at: "2026-10-18 03:34:14 +0400"
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
  source_atom_revision: 24
  source_sha256: 6a28980fd28244344b253b32457d63ae46a23ab8a5e089c59310f3af429aec65
  original_relations_sha256: 5c9f7c8eabd47f3a1145066b2d404575be26ad76ec5f6fe4c4c68ec66380a8d6
---
# Summary
Validate Goal Claim Scope

## Scope

Goal Atoms.

## Claim

a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.

## Details
