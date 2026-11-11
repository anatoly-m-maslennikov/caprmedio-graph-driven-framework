---
atom_id: CA-R-2814
ref_id: CA-R-2814@1-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Rule
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL
tier: 3
status: Draft
version: 1
updated_at: 2026-11-05 16:33:24 +0400
carrier_destination:
  file:
    name: CA-R-2814@1-draft-RULE--define-generic-relation-declaration-endpoint-signature.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Define generic Relation Declaration endpoint signature

## Claim

### Prose Claim

Within a Relation Declaration Formal Claim only, `$host ((RELATION)) $target` is the reusable generic endpoint signature. `$host` and `$target` range over the endpoint domains explicitly admitted by the Relation Declaration. Those domains are declared model entities or instances, including Carrier and CFEL, except for the literal values and constraint data explicitly admitted as endpoints of HAS_ALLOWED_VALUE, HAS_VALUE_CONSTRAINT and their declared derived inverses. CFEL glyphs are not endpoints. This signature creates neither a Relation fact nor instance data. Known endpoint kinds remain typed selectors; the generic signature does not extend untyped variables to any other CFEL context.
