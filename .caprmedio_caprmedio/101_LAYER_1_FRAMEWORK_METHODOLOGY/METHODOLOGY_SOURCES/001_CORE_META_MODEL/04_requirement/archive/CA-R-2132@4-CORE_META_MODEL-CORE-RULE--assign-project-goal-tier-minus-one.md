---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Tier
  depends_on:
  - 'Subject/Domain/Node/Continuant/Atom/Content Role: Requirement/Type: Project Goal'
  - Subject/Domain/Node/Continuant/Project
  - Subject/Domain/Node/Continuant/Atom.Tier
  - 'Subject/Domain/Node/Continuant/Actor/Type: Operator'
version: 4
updated_at: 2026-10-24 02:06:49 +0400
relations: {}
atom_id: CA-R-2132@4
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
tier: 1
status: Archived
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
