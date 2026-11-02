---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Tier
  depends_on:
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type: Project Goal'
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  - Entity/Object/Continuant/Governing Objects/Atom.Tier
  - Entity/Object/Continuant/Actor/Operator
version: 10
updated_at: 2026-10-29 07:45:28 +0400
relations: {}
atom_id: CA-R-2132@10
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Archived
author: Anatoly Maslennikov
type: Rule
---
## Summary

Assign Project Goal Tier Minus One

## Claim scope

Project Goal Atoms.

## Claim

Every Requirement Atom of Type Project Goal **must** target the Project, be owned by its Operator Actor instead of a Local Scope Unit, and carry exactly one numeric Tier `-1`. Tier `-1` is explicit, is not omitted, and is outside the ordinary nonnegative Tier range. This Rule does not impose an arbitrary Type-to-Tier restriction beyond verified Project Goal identity and ownership.

## Details

The Project Goal retains its Operator Actor owner. CA-D-637 uses its Target Project only as the derived ordering context; ordinary Goal ownership and Scope ordering are unchanged.
