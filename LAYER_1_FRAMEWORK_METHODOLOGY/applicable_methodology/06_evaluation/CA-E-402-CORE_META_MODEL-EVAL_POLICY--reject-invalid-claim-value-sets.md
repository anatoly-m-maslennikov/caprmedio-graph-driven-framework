---
subjects:
  active: CAPRMEDIO_MODEL <+ Atom.Content
  passive:
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ CFEL<+Operator//AllowedValue
version: 33
updated_at: 2026-11-02 08:06:47 +0400
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-402-CORE_META_MODEL-EVAL_POLICY--reject-invalid-claim-value-sets.md
  source_atom_id: CA-E-402
  source_atom_revision: 33
  source_sha256: 3017762d12c5a0f8de451508e86851afa02d1cb06b9e96c53b0d007335cfaf45
  original_relations_sha256: 7b3fb85adc0a1aa2b2fcfda9d6e0b426270d88eabbed8c43561cbb8bd19ca84a
---
## Summary

Reject Invalid Claim Value Sets

## Claim

### Prose Claim


Claim Value Sets.


the Evaluation **must** reject a Claim Value Set **if** it identifies **`!=1`** Property, has **`=0`** values, repeats a value, uses one noncanonical value, has nonfinite **or** ordered semantics, **contains** one value **not** allowed by its Property, permits one value **to** be accepted, replaced, **or** retired independently, **or** parses `:` as Subject Expression syntax.
