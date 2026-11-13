---
atom_id: CA-R-2613
ref_id: CA-R-2613@1
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL<+Operator//RelationEndpointSignature
tier: 3
status: archived
version: 1
updated_at: 2026-11-02 08:06:47 +0400
carrier_destination:
  file:
    name: CA-R-2613@1-CORE_META_MODEL-DECLARATION--declare-cfel-relation-endpoint-signature.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare CFEL Relation endpoint signature

## Claim

### Formal Claim

```CFEL
# model
Operator//RelationEndpointSignature == "$host ((RELATION)) $target"
```

## Semantics

Within a Relation Declaration Formal Claim only, `$host` and `$target`
range over declared model entities or instances, including Carrier and CFEL,
and exclude literals. The signature creates neither a Relation fact nor
instance data. Known endpoint kinds remain typed selectors; this does not extend
untyped variables to other CFEL contexts.
