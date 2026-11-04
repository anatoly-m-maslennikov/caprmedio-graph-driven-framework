---
subjects:
  active: 'CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Method).Header.Form'
  passive:
  - CAPRMEDIO_MODEL <+ Carrier
version: 28
updated_at: 2026-11-02 00:55:09 +0400
relations: {}
atom_id: CA-D-404
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 3
role: Delivery
form: Decision
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery/CA-D-404-CORE_META_MODEL-ENG_DECISION--serialize-method-type-tokens.md
  source_atom_id: CA-D-404
  source_atom_revision: 28
  source_sha256: daca79b4a9fc832c5c625183a05e19f9d6047bfda01e1c334d941fd6c9b91bca
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Serialize Method Type Tokens

## Claim

### Prose Claim


Method Atom File Carriers.


a Method Atom File Carrier **must** serialize its effective Label within the Atom filename grammar governed by CA-D-283 and CA-D-284, using the explicit Label when present and the Type name when Label is absent. The effective Label is normalized as an uppercase structured token; an unlabeled Eng Policy, Eng Decision, External Implementation Method and Method Binding therefore use `ENG_POLICY`, `ENG_DECISION`, `EXTERNAL_IMPLEMENTATION_METHOD` and `METHOD_BINDING`.

## Details

These examples govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value. The YAML `form` field carries the Atom Form under CA-D-657; the filename token is the effective-Label carrier encoding. An explicit `label` field takes precedence; when it is absent, CA-R-2705 supplies the Type name as the effective Label. Do not infer the Atom Type from a filename token; derive the filename token from the effective Label.

Within PROGRAMMATIC and its declared descendants, Current Method and Delivery Atoms use only Eng Policy or Eng Decision under CA-R-2123; legacy Implementation Method and Implementation Decision names are not additional admitted values there. Existing specialized values remain governed by their own definitions outside that scope.
