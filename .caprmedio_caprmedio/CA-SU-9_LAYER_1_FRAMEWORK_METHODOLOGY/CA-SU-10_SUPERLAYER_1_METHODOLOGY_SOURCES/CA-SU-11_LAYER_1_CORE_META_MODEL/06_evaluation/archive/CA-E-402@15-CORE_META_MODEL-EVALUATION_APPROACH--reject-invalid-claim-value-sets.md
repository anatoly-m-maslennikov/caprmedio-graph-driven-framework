---
subjects:
  governs: Claim Value Set Validation
  depends_on:
  - Subject/Domain/Node/Continuant/Atom.Substance
  - Claim Value Set
  - Property
  - Subject Expression
  - IS_ALLOWED_VALUE_OF
version: 15
updated_at: 2026-10-23 03:20:06 +0400
relations:
  evaluation_for:
  - CA-R-1359
  - CA-M-237
atom_id: CA-E-402@15
content_role: Evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
status: Archived
author: Anatoly Maslennikov
type: Policy
global_tier: 11
---
# Summary

Reject Invalid Claim Value Sets

## Scope

Claim Value Sets.

## Claim

the Evaluation **must** reject a Claim Value Set **if** it identifies **`!=1`** Property, has **`=0`** values, repeats a value, uses one noncanonical value, has nonfinite **or** ordered semantics, **contains** one value **not** allowed by its Property, permits one value **to** be accepted, replaced, **or** retired independently, **or** parses `:` as Subject Expression syntax.

## Details
