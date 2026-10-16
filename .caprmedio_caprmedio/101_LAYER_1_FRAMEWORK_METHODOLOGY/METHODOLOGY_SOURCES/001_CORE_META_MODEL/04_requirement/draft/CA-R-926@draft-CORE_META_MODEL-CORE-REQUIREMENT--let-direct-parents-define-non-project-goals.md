---
subjects:
  governs: "Entity/Continuant/Object/Atom/Content Role: Requirement/Type: Goal"
  depends_on:
    ["Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Project.Structure", "Entity/Continuant/Object/Atom.Substance", "Entity/Continuant/Object/Scope Unit.Parent", "Entity/Continuant/Object/Scope Unit.Children"]
version: 21
updated_at: "2026-10-16 12:00:15 +0000"
relations:
  child_of:
    - CA-R-925
atom_id: "CA-R-926@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary
Let Direct Parents Define Non-Project Goals

## Scope

Non-Project Scope Units.

## Claim

**every** non-Project Scope Unit **must** have **`>=1`** accepted Goal Atom owned by its declared direct parent Scope Unit. this is a Goal-coverage obligation, **not** the source of the child's structural identity; a missing accepted Goal is a reported gap **and** **must not** remove **or** conceal the declared Scope Unit.

## Details
