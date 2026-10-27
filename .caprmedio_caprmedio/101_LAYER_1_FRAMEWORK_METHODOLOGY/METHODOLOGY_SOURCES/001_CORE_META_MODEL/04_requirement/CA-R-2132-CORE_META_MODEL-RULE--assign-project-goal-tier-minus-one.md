---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Tier
  depends_on:
  - 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Requirement/Type: Project Goal'
  - Subject/Graph Node/Domain/Continuant/Project
  - Subject/Graph Node/Domain/Continuant/Atom.Tier
  - 'Subject/Graph Node/Domain/Continuant/Actor/Type: Operator'
version: 7
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-R-2132
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Active
author: Anatoly Maslennikov
type: Rule
---
# Summary

Assign Project Goal Tier Minus One

## Scope

Project Goal Atoms.

## Claim

Every Requirement Atom of Type Project Goal **must** target the Project, be owned by its Operator Actor instead of a Local Scope Unit, and carry exactly one numeric Tier `-1`. Tier `-1` is explicit, is not omitted, and is outside the ordinary nonnegative Tier range. This Rule does not impose an arbitrary Type-to-Tier restriction beyond verified Project Goal identity and ownership.

## Details

The Project Goal retains its Operator Actor owner. CA-D-637 uses its Target Project only as the derived ordering context; ordinary Goal ownership and Scope ordering are unchanged.
