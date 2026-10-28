---
subjects:
  governs: Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  depends_on:
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Local Scope Unit
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Atom.Content
  - Subject/CAPRMEDIO/Graph/Node/Project Model/Term//Property
  - 'Subject/CAPRMEDIO/Graph/Relation/Type: IS_ALLOWED_VALUE_OF'
version: 28
updated_at: 2026-10-27 19:59:53 +0400
relations:
  child_of:
  - CA-R-2102
  - CA-R-1596
atom_id: CA-R-1358
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
author: Anatoly Maslennikov
tier: 3
type: Rule
---
# Summary

Consolidate Single-Value Claims as One Value-Set Claim

## Scope

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X.

## Claim

multiple Claims with the same Atom Scope, Claim Target Scope Unit, textual Claim Scope, **and** Property X **must** be consolidated as **`=1`** Claim Value Set **if** they differ **only** by one allowed value of X.

## Details
