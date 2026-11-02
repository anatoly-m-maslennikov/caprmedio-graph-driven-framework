---
subjects:
  governs: Entity/Object/Continuant/Governing Objects/Atom.Content
  depends_on:
  - Entity/Object/Continuant/Governing Objects/Atom.Local Scope Unit
  - Entity/Object/Continuant/Governing Objects/Atom.Content
  - Entity/Object/Continuant/Term//Property
  - Entity/Graph Syntax > Relation//IS_ALLOWED_VALUE_OF
version: 29
updated_at: 2026-10-29 07:17:16 +0400
relations:
  child_of:
  - CA-R-2102
  - CA-R-1596
atom_id: CA-R-1358@29
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
