---
subjects:
  governs: "Entity/Node/Continuant/Atom.Subjects"
  depends_on:
    - "Entity"
    - "Method"
atom_id: "CA-R-2004@1"
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: "Archived"
version: 1
updated_at: "2026-10-21 01:47:52 +0400"
author: "Anatoly Maslennikov"
global_tier: 9
relations: {}
---
# Summary

Define Subject Target

## Scope

a direct Subject Relation target.

## Claim

a Subject Target **means** exactly one canonical target addressed by a Subject
Expression. a Subject Target **must** be either an Entity or a Method Topic.

## Details

a Subject Target is the endpoint of GOVERNS or DEPENDS_ON. the reference does
not assign the target as the referencing Atom's owning Scope Unit or Carrier.
resolving a Subject Target does not create an Entity, Method Topic, or relation fact.
