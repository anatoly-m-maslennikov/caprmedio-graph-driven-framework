---
atom_id: CA-R-1610
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
author: Anatoly Maslennikov
status: Active
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Status
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Projection
  - Subject/CAPRMEDIO/Graph/Rule
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Selection
version: 20
updated_at: 2026-10-27 19:59:59 +0400
relations: {}
tier: 3
type: Rule
---
# Summary

Keep reverse-engineered RMED provisional

## Scope

RMED Claims reconstructed from existing Implementation or its Projections.

## Claim

RMED Claims reconstructed from existing Implementation **or** its Projections **must** remain proposed Draft Claims **until** accepted through the applicable Atom acceptance authority.

- extraction **or** inference alone does **not** establish Active authority.
- the accepted RMED, **not** the legacy Implementation **or** its Projection, governs subsequent refactoring **and** Evaluation of the result.

## Details
