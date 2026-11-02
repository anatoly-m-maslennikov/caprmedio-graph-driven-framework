---
version: 1
updated_at: 2026-10-29 22:26:56 +0400
relations:
  child_of:
  - CA-R-2426
subjects:
  governs: Entity/Object/Continuant/Structural Unit/Scope Unit/Project
  depends_on:
  - Entity/Object/Continuant/Structural Unit/Scope Unit/Project
atom_id: CA-R-2427@1
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Rule
---
## Summary

Give each Project-wide invariant canonical authority

## Claim scope

Project-wide foundational invariants.

## Claim

Every Project-wide foundational invariant must have exactly one active Project-owned Tier `0` Atom as its canonical authority owner. One such Atom may own several related invariants; this does not require one Atom per invariant or one Tier `0` Atom for the Project. Faithful specialization does not create independent duplicate authority.
