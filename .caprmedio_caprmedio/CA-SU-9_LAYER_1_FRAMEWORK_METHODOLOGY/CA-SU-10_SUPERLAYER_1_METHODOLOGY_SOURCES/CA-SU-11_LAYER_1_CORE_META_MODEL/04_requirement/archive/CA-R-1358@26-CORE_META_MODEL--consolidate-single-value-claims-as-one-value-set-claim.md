---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Content
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Local Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Content
  - Subject/Domain/Node/Continuant/Term//Property
  - 'Subject/Graph/Relation/Type: IS_ALLOWED_VALUE_OF'
version: 26
updated_at: 2026-10-25 03:48:37 +0400
relations:
  child_of:
  - CA-R-2102
  - CA-R-1596
atom_id: CA-R-1358@26
content_role: Requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
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
