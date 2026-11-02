---
subjects:
  governs: 'Subject/Domain/Node/Continuant/Atom/Content Role: Method/Type'
  depends_on:
  - Subject/Engineering/Carrier
version: 18
updated_at: 2026-10-24 09:42:52 +0400
relations: {}
atom_id: CA-D-404@18
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

a Method Atom File Carrier **must** serialize the following Type components within the Atom filename grammar governed by CA-D-283-CORE_META_MODEL-CORE-DELIVERY--serialize-project-owned-markdown-atom-filenames **and** CA-D-284-CORE_META_MODEL-CORE-DELIVERY--serialize-filename-token-case:

- Eng Policy: `ENG_POLICY`.
- Eng Decision: `ENG_DECISION`.
- External Implementation Method: `EXTERNAL_IMPLEMENTATION_METHOD`.
- Method Binding: `METHOD_BINDING`.

## Details

These mappings govern filename representation; they do **not** rename a Type, admit a new Type, **or** prescribe a YAML Type value. The YAML `type` field remains the single admitted Type value under CA-D-276; a filename Type token is only its carrier encoding, not a second Type or a Label. An explicit `label` field is the effective Label when present; when absent, the effective Label is derived from the Atom Type name under CA-R-1594. Do not infer Type from a filename token or from that derived Label.

Within PROGRAMMATIC and its declared descendants, Current Method and Delivery Atoms use only Eng Policy or Eng Decision under CA-R-2123; legacy Implementation Method and Implementation Decision names are not additional admitted values there. Existing specialized values remain governed by their own definitions outside that scope.
