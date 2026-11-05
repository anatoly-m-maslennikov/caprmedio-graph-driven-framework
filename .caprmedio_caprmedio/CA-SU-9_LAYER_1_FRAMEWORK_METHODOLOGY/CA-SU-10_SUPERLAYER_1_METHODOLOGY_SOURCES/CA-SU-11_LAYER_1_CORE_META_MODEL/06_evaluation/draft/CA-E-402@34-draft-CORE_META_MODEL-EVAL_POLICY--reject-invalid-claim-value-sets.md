---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ CFEL
version: 34
updated_at: 2026-11-05 14:25:52 +0400
relations:
  evaluation_for:
  - CA-R-1359
  - CA-M-237
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
atom_id: CA-E-402
status: Draft
tier: 5
role: Evaluation
form: Eval Policy
carrier_destination:
  file:
    name: CA-E-402@34-draft-CORE_META_MODEL-EVAL_POLICY--reject-invalid-claim-value-sets.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/draft
---
## Summary

Reject Invalid Claim Value Sets

## Claim

### Prose Claim


Claim Value Sets.


the Evaluation **must** reject a Claim Value Set **if** it identifies **`!=1`** Property, has **`=0`** values, repeats a value, uses one noncanonical value, has nonfinite **or** ordered semantics, **contains** one value **not** allowed by its Property, permits one value **to** be accepted, replaced, **or** retired independently, **or** parses `:` as Subject Expression syntax.
