---
subjects:
  active: Atom.Content
  passive:
  - Term//Property
  - Entity
  - CFEL<+Operator//AllowedValue
version: 33
updated_at: 2026-11-02 07:52:54 +0400
relations:
  evaluation_for:
  - CA-R-1359
  - CA-M-237
atom_id: CA-E-402
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 5
role: Evaluation
form: Eval Policy
---
## Summary

Reject Invalid Claim Value Sets

## Claim scope

Claim Value Sets.

## Claim

the Evaluation **must** reject a Claim Value Set **if** it identifies **`!=1`** Property, has **`=0`** values, repeats a value, uses one noncanonical value, has nonfinite **or** ordered semantics, **contains** one value **not** allowed by its Property, permits one value **to** be accepted, replaced, **or** retired independently, **or** parses `:` as Subject Expression syntax.
