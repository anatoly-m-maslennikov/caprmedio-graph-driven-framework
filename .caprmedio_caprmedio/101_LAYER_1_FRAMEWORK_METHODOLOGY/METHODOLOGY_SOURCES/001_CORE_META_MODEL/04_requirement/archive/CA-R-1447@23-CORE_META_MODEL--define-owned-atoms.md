---
subjects:
  governs: Entity/Object/Continuant/Selection
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom
  - Entity/Object/Continuant/Structural Unit/Scope Unit
  - Entity/Carrier
version: 23
updated_at: 2026-10-29 10:13:48 +0400
relations: {}
atom_id: CA-R-1447@23
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 2
type: Entity Definition
---
## Summary

Define Owned Atoms

## Claim scope

the ownership of Atoms by Scope Units.

## Claim

Owned Atoms **means** the set of **all** Atoms whose internally carried current Scope Unit **`=`** the selected Scope Unit.

- a grouping Carrier, Plan decomposition, **or** physical placement does **not** replace that ownership value.
- a missing, invalid, **or** ambiguous ownership value leaves membership unresolved; do **not** derive it from the filename **or** containing folders.
- evaluate placement consistency separately **without** changing the selected Atom's declared ownership.
