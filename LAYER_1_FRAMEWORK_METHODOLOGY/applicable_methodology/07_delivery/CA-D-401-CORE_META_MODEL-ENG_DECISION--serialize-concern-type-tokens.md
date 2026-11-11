---
atom_id: CA-D-401
ref_id: CA-D-401
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Form'
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 24
updated_at: 2026-11-02 00:18:22 +0400
carrier_destination:
  file:
    name: CA-D-401-CORE_META_MODEL-DECISION--serialize-concern-type-tokens.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-401-CORE_META_MODEL-ENG_DECISION--serialize-concern-type-tokens.md
  source_atom_id: CA-D-401
  source_atom_revision: 24
  source_sha256: 36a4d87e29024d7ee39ce5bef015867e4b89304516219892548810e8b1135ffe
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Concern Type Tokens

## Claim

### Prose Claim


the serialization of Concern Type tokens in a Concern Atom File Carrier filename.


a Concern Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Question: `QUESTION`.
- Problem: `PROBLEM`.
- Risk: `RISK`.
- Opportunity: `OPPORTUNITY`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
