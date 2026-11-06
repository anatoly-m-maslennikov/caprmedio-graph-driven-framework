---
atom_id: CA-E-402
ref_id: CA-E-402
container:
  scope_unit: CA-SU-11
role: Evaluation
form: Eval Policy
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom.Content
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Property
  - CAPRMEDIO_MODEL <+ Entity
  - CAPRMEDIO_MODEL <+ CFEL<+Operator//AllowedValue
tier: 5
relations:
  evaluation_for:
  - CA-R-1359
  - CA-M-237
status: Active
version: 33
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-E-402-CORE_META_MODEL-EVAL_POLICY--reject-invalid-claim-value-sets.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/06_evaluation/CA-E-402-CORE_META_MODEL-EVAL_POLICY--reject-invalid-claim-value-sets.md
  source_atom_id: CA-E-402
  source_atom_revision: 33
  source_sha256: 2d23c7fd40d148bab67dd40d925e059d6755917bf81bfbd4dcc3972e2c7e1c6a
  original_relations_sha256: 7b3fb85adc0a1aa2b2fcfda9d6e0b426270d88eabbed8c43561cbb8bd19ca84a
---
## Summary

Reject Invalid Claim Value Sets

## Claim

### Prose Claim


Claim Value Sets.


the Evaluation **must** reject a Claim Value Set **if** it identifies **`!=1`** Property, has **`=0`** values, repeats a value, uses one noncanonical value, has nonfinite **or** ordered semantics, **contains** one value **not** allowed by its Property, permits one value **to** be accepted, replaced, **or** retired independently, **or** parses `:` as Subject Expression syntax.
