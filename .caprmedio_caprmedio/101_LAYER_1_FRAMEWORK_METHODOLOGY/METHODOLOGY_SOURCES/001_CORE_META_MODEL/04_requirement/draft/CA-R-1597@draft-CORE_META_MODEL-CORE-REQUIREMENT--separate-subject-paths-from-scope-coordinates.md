---
subjects:
  governs: "Entity/Continuant/Object/Atom.Subjects"
  depends_on:
    ["Subject", "Subject Path", "Entity", "Entity/Continuant/Object/Scope Unit", "Entity/Continuant/Object/Atom.Target Scope Unit"]
version: 6
updated_at: "2026-10-15 18:18:02 +0000"
relations:
  relates_to:
    - CA-R-1275
    - CA-R-1201
    - CA-R-1202
    - CA-R-1595
    - CA-M-273
atom_id: "CA-R-1597@draft"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Draft"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Separate Subject Paths from Scope Coordinates

## Scope

an Atom's Subject Paths.

## Claim

an Atom's Subject Paths **must** identify the Entity targets of its Subject Relations **without** substituting those paths for its owning Scope Unit **or** its Claim Target Scope Unit.

## Details
