---
subjects:
  governs: 'Subject/Graph Node/Domain/Continuant/Atom/Content Role: Method/Type'
  depends_on:
  - Subject/Graph Node/Engineering/Continuant/Carrier
version: 20
updated_at: 2026-10-25 17:32:27 +0400
relations: {}
atom_id: CA-D-404@20
content_role: Delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
author: Anatoly Maslennikov
tier: 3
type: Eng Decision
---
# Summary

Serialize Method Type Tokens

## Scope

Method Atom File Carriers.

## Claim

a Method Atom File Carrier **must** serialize its effective Label within the Atom filename grammar governed by CA-D-283 and CA-D-284, using the explicit Label when present and the Type name when Label is absent. The effective Label is normalized as an uppercase structured token; an unlabeled Eng Policy, Eng Decision, External Implementation Method and Method Binding therefore use `ENG_POLICY`, `ENG_DECISION`, `EXTERNAL_IMPLEMENTATION_METHOD` and `METHOD_BINDING`.

## Details

These examples govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value. The YAML `type` field remains the single admitted Type value under CA-D-276; the filename token is the effective-Label carrier encoding. An explicit `label` field takes precedence; when it is absent, CA-R-1594 supplies the Type name as the effective Label. Do not infer the Atom Type from a filename token; derive the filename token from the effective Label.

Within PROGRAMMATIC and its declared descendants, Current Method and Delivery Atoms use only Eng Policy or Eng Decision under CA-R-2123; legacy Implementation Method and Implementation Decision names are not additional admitted values there. Existing specialized values remain governed by their own definitions outside that scope.
