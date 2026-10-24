---
subjects:
  governs: "Entity/Node/Continuant/Atom.Subjects"
  depends_on:
    - "Entity"
    - "Method"
atom_id: "CA-R-2006@1"
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

Define Subject Target Roots

## Scope

the first named component of a canonical Subject Target path.

## Claim

a canonical Subject Target path **must** begin with exactly one registered root:
`Entity` for what a Claim governs or `Method` for how a Method Claim guides work.

## Details

the roots are namespaces, not a hierarchy between Entity and Method. a Scope
Unit path, carrier path, owner path, or implementation-language folder does not
qualify a Subject Target unless it is explicitly part of the canonical target.
