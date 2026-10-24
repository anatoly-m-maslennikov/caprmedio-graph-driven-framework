---
subjects:
  governs: Subject/Domain/Node/Continuant/Atom.Substance
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Local Scope Unit
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Claim Value Set
  - Subject/Domain/Node/Continuant/Term//Property
  - IS_ALLOWED_VALUE_OF
version: 21
updated_at: 2026-10-24 02:14:24 +0400
relations:
  child_of:
  - CA-R-918
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
