---
subjects:
  governs: "relation-model"
  depends_on:
    - "atom-boundary"
version: 17
updated_at: "2026-10-20 00:11:13 +0400"
relations: {}
atom_id: CA-R-1040@17
content_role: "Requirement"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Core"
status: Archived
author: "Anatoly Maslennikov"
global_tier: 9
---
# Summary

Reject authored inverse relations

## Scope

authored inverse typed relations.

## Claim

validators **must** reject **every** inverse typed relation authored **in** an Atom Carrier.

## Details

Inverse means the derived direction declared by the governing Relation Kind definition, not a direction guessed from its name. In the containment pair, IS_CONTAINED_BY is direct from child to parent and is the only permitted authoritative direction when Atom containment is authored; CONTAINS is the inverse and must not be separately authored. This clarification does not admit a new runtime relation key or waive endpoint Graph Rules.
