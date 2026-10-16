---
subjects:
  governs: "Entity/Continuant/Object/Atom.Target Scope Unit"
  depends_on:
    ["Entity/Continuant/Object/Atom/Content Role: Requirement/Type: Goal", "Entity/Continuant/Object/Atom.Owning Scope Unit", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Project.Structure", "Entity/Continuant/Object/Project"]
version: 23
updated_at: "2026-10-16 12:00:15 +0000"
relations:
  child_of:
    - CA-R-925
    - CA-R-926
    - CA-R-927
atom_id: "CA-R-947@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary
Validate Goal Claim Scope

## Scope

Goal Atoms.

## Claim

a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.

## Details
