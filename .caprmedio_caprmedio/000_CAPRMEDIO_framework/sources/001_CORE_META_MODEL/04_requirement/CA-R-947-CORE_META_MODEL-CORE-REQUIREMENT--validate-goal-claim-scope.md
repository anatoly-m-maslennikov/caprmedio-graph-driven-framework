---
subjects:
  governs: "Entity/Node/Continuant/Atom.Target Scope Unit"
  depends_on:
    ["Entity/Node/Continuant/Atom/Content Role: Requirement/Type: Goal", "Entity/Node/Continuant/Atom.Owning Scope Unit", "Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Project.Structure", "Entity/Node/Continuant/Project"]
version: 25
updated_at: "2026-10-19 15:54:32 +0400"
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
---
# Summary
Validate Goal Claim Scope

## Scope

Goal Atoms.

## Claim

a Goal Atom **must** identify **`=1`** Claim Target Scope Unit that is a direct child of its Atom Scope Unit according **to** authoritative Project Structure, **or** the Project Scope Unit **if** its Atom Scope **contains** no Scope Unit. a Goal reference assigns a purpose **and** **must not** independently declare **or** change the target's Name, parent, order, **or** Carrier binding.

## Details
