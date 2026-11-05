---
atom_id: CA-D-400
ref_id: CA-D-400
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation).Header.Form'
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 25
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-400-CORE_META_MODEL-DECISION--serialize-evaluation-type-tokens.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Serialize Evaluation Type Tokens

## Claim

### Prose Claim


the serialization of Evaluation Type tokens in an Evaluation Atom File Carrier filename.


an Evaluation Atom File Carrier **must** serialize its effective Label within the Atom filename grammar governed by CA-D-283 and CA-D-284, using the explicit Label when present and the Type name when Label is absent. The effective Label is normalized as an uppercase structured token; an unlabeled Eval Case, Evaluation Control and Evaluation Approach therefore use `EVAL_CASE`, `EVALUATION_CONTROL` and `EVALUATION_APPROACH`. This generic rule covers every admitted Evaluation Type and does not rename a Type, admit a new Type, or prescribe a YAML Type value.
