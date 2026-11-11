---
atom_id: CA-D-402
ref_id: CA-D-402
container:
  scope_unit: CA-SU-11
role: Delivery
form: Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Delivery).Header.Context.Form
  dependencies:
  - CAPRMEDIO_MODEL <+ Carrier
tier: 3
status: Active
version: 29
updated_at: "2026-11-07 15:18:44 +0400"
carrier_destination:
  file:
    name: CA-D-402-CORE_META_MODEL-DECISION--serialize-delivery-type-tokens.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/07_delivery
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Serialize Delivery Type Tokens

## Claim

### Prose Claim

A Delivery Atom File Carrier must serialize its effective Label within the Atom filename grammar governed by CA-D-283 and CA-D-284. Use the explicit Label when present and the Form name when Label is absent. Normalize the effective Label as an uppercase structured token.

## Details

The filename token is the effective-Label carrier encoding; it does not rename or admit a Form or prescribe a YAML Form value. The YAML `form` field carries the Atom Form under CA-D-657. An explicit `label` field takes precedence; when absent, CA-R-2705 supplies the Form name as the effective Label. Do not infer the Atom Form from a filename token; derive the filename token from the effective Label.

Release Definition and Environment Definition remain subject to their applicable admission authority, including CA-R-1665.
