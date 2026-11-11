---
subjects:
  active: 'CAPRMEDIO <+ MODEL <+ Entity/Object/Continuant/Governing Objects/Atom/Content Role: Evaluation/Type'
  passive:
  - CAPRMEDIO <+ MODEL <+ Carrier
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-400
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
---
## Summary

Serialize Evaluation Type Tokens

## Claim scope

the serialization of Evaluation Type tokens in an Evaluation Atom File Carrier filename.

## Claim

an Evaluation Atom File Carrier **must** serialize its effective Label within the Atom filename grammar governed by CA-D-283 and CA-D-284, using the explicit Label when present and the Type name when Label is absent. The effective Label is normalized as an uppercase structured token; an unlabeled Eval Case, Evaluation Control and Evaluation Approach therefore use `EVAL_CASE`, `EVALUATION_CONTROL` and `EVALUATION_APPROACH`. This generic rule covers every admitted Evaluation Type and does not rename a Type, admit a new Type, or prescribe a YAML Type value.
