---
topics:
  main_subject: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Concern).Header.Form'
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
version: 24
updated_at: 2026-11-02 00:18:22 +0400
atom_id: CA-D-401
ref_id: CA-D-401
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
container:
  scope_unit: CA-SU-11
carrier_destination:
  file:
    name: CA-D-401-CORE_META_MODEL-DECISION--serialize-concern-type-tokens.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
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
