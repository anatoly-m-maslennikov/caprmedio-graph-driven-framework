---
subjects:
  governs: Owned Atoms
  depends_on:
  - Subject/Domain/Node/Continuant/Atom
  - Subject/Domain/Node/Continuant/Scope Unit
  - Subject/Engineering/Carrier
version: 13
updated_at: 2026-10-23 03:14:50 +0400
relations: {}
atom_id: CA-R-1447@13
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: General
status: Archived
author: Anatoly Maslennikov
global_tier: 10
---
# Summary

Define Owned Atoms

## Scope

the ownership of Atoms by Scope Units.

## Claim

Owned Atoms **means** the set of **all** Atoms whose internally carried current Scope Unit **`=`** the selected Scope Unit.

- a grouping Carrier, Plan decomposition, **or** physical placement does **not** replace that ownership value.
- a missing, invalid, **or** ambiguous ownership value leaves membership unresolved; do **not** derive it from the filename **or** containing folders.
- evaluate placement consistency separately **without** changing the selected Atom's declared ownership.

## Details
