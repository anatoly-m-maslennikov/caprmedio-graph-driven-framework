---
subjects:
  governs: "Entity/Node/Continuant/Atom.Subjects"
  depends_on:
    ["Subject", "Subject Path", "Subject Target", "Entity/Node/Continuant/Scope Unit", "Entity/Node/Continuant/Atom.Target Scope Unit"]
version: 8
updated_at: "2026-10-21 01:47:52 +0400"
relations:
  relates_to:
    - CA-R-1275
    - CA-R-1201
    - CA-R-1202
    - CA-R-1595
    - CA-M-273
atom_id: "CA-R-1597@8"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Archived"
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Separate Subject Paths from Scope Coordinates

## Scope

an Atom's Subject Paths.

## Claim

an Atom's Subject Paths **must** identify the Subject Targets of its Subject Relations **without** substituting those paths for its owning Scope Unit **or** its Claim Target Scope Unit.

## Details
