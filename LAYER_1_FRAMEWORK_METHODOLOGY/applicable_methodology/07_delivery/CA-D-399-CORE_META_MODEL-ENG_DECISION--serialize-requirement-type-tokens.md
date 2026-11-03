---
subjects:
  active: 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Requirement/Type'
  passive:
  - Carrier
version: 25
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
atom_id: CA-D-399
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-399-CORE_META_MODEL-ENG_DECISION--serialize-requirement-type-tokens.md
  source_atom_id: CA-D-399
  source_atom_revision: 25
  source_sha256: 116eb53aec1e9b52819b0225199e8d0534420ce593c861923943b4d496c85644
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Requirement Type Tokens

## Claim scope

the serialization of Requirement Type tokens in a Requirement Atom File Carrier filename.

## Claim

a Requirement Atom File Carrier **must** serialize its effective Label within the Atom filename grammar governed by CA-D-283 and CA-D-284, using the explicit Label when present and the Type name when Label is absent. The effective Label is normalized as an uppercase structured token; an unlabeled Constraint and Boundary therefore use `CONSTRAINT` and `BOUNDARY`. This generic rule covers every admitted Requirement Type and does not rename a Type, admit a new Type, or prescribe a YAML Type value.
