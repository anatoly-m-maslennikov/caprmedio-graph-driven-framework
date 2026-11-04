---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Evaluation).Header.Form'
  passive:
  - CAPRMEDIO_MODEL <+ Carrier
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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-400-CORE_META_MODEL-ENG_DECISION--serialize-evaluation-type-tokens.md
  source_atom_id: CA-D-400
  source_atom_revision: 25
  source_sha256: 8dccc08440171849ed368d98a6051a72f0bf677ea919a7f263de568ef65d91d4
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Evaluation Type Tokens

## Claim

### Prose Claim


the serialization of Evaluation Type tokens in an Evaluation Atom File Carrier filename.


an Evaluation Atom File Carrier **must** serialize its effective Label within the Atom filename grammar governed by CA-D-283 and CA-D-284, using the explicit Label when present and the Type name when Label is absent. The effective Label is normalized as an uppercase structured token; an unlabeled Eval Case, Evaluation Control and Evaluation Approach therefore use `EVAL_CASE`, `EVALUATION_CONTROL` and `EVALUATION_APPROACH`. This generic rule covers every admitted Evaluation Type and does not rename a Type, admit a new Type, or prescribe a YAML Type value.
