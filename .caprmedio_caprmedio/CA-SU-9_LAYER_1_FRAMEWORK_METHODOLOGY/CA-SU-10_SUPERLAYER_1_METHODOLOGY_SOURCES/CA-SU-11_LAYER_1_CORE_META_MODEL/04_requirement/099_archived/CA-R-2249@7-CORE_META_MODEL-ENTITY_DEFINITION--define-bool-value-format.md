---
atom_id: CA-R-2249
ref_id: CA-R-2249@7
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Format/bool
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Format
tier: 1
status: archived
version: 7
updated_at: 2026-11-11 16:04:42 +0400
carrier_destination:
  file:
    name: CA-R-2249@7-CORE_META_MODEL-ENTITY_DEFINITION--define-bool-value-format.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/099_archived
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define bool Value Format

## Claim

### Prose Claim


The bool Value Format admits the Boolean values true and false. It does not set a
property's cardinality, default, nullability, or carrier representation.



### Formal Claim

```CFEL
# model
CFEL <+ Format/bool;

Format/bool ((NARROWER_THAN)) Format;
```

## Semantics

bool is the value domain selected by a `[bool]` annotation on one direct
Property value.
