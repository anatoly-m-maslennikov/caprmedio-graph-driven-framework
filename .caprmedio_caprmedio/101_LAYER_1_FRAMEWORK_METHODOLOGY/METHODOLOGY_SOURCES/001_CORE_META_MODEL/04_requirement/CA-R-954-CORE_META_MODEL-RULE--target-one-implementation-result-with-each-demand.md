---
subjects:
  governs: 'Subject/CAPRMEDIO/Graph/Node/Project Model/Atom/Content Role: Requirement/Type: Demand'
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Implementation
version: 29
updated_at: 2026-10-27 20:00:12 +0400
relations:
  child_of:
  - CA-R-933
atom_id: CA-R-954
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 6
type: Rule
---
# Summary
Target one Implementation result with each Demand

## Scope

Demand Atoms.

## Claim

**every** Demand Atom **must** constrain **`=1`** Implementation result produced by its Claim Scope.

## Details
