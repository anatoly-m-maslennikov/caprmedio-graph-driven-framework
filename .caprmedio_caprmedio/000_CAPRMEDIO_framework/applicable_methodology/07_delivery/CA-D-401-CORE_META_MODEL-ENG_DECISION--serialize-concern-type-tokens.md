---
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Concern/Type'
  passive:
  - Carrier
version: 24
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-401
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-401-CORE_META_MODEL-ENG_DECISION--serialize-concern-type-tokens.md
  source_atom_id: CA-D-401
  source_atom_revision: 24
  source_sha256: 1d80ceb0c14c957b05887e5cbe4d3d9ad5f62f48199a0b141b579180d07d4d93
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Concern Type Tokens

## Claim scope

the serialization of Concern Type tokens in a Concern Atom File Carrier filename.

## Claim

a Concern Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283 **and** CA-D-284:

- Question: `QUESTION`.
- Problem: `PROBLEM`.
- Risk: `RISK`.
- Opportunity: `OPPORTUNITY`.

these mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value.
