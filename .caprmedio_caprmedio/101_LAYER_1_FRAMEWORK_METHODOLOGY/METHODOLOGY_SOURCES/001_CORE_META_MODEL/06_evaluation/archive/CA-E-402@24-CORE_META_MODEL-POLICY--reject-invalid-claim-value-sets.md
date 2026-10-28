---
subjects:
  governs: Subject/Graph Node/Domain/Continuant/Atom.Content
  depends_on:
  - Subject/Graph Node/Domain/Continuant/Atom.Content
  - Subject/Graph Node/Domain/Continuant/Term//Property
  - Subject
  - 'Subject/Graph Relation/Type: IS_ALLOWED_VALUE_OF'
version: 24
updated_at: 2026-10-25 17:32:27 +0400
relations:
  evaluation_for:
  - CA-R-1359
  - CA-M-237
atom_id: CA-E-402@24
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
type: Policy
tier: 5
---
# Summary

Reject Invalid Claim Value Sets

## Scope

Claim Value Sets.

## Claim

the Evaluation **must** reject a Claim Value Set **if** it identifies **`!=1`** Property, has **`=0`** values, repeats a value, uses one noncanonical value, has nonfinite **or** ordered semantics, **contains** one value **not** allowed by its Property, permits one value **to** be accepted, replaced, **or** retired independently, **or** parses `:` as Subject Expression syntax.

## Details
