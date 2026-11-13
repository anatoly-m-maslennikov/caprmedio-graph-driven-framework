---
atom_id: CA-R-2476
ref_id: CA-R-2476@7-draft
container:
  scope_unit: CA-SU-11
role: Requirement
form: Relation Declaration
topics:
  main_subject: CAPRMEDIO_MODEL/CFEL/Relation//INSTANCE_OF
tier: 3
status: Draft
version: 7
updated_at: 2026-11-05 19:33:47 +0400
carrier_destination:
  file:
    name: CA-R-2476@7-draft-CORE_META_MODEL-RELATION_DECLARATION--define-instance-of.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/000_draft
---
## Summary

Define INSTANCE_OF

## Claim

### Prose Claim

The Host is an instance of the Target declared Model entity. A Property instance is borne by its data bearer and is an instance of its corresponding model Property, which remains borne by its model bearer. A Property instance has no independent Carrier; its bearer and kind Relations are distinct and may coexist.

HAS_INSTANCE is the inverse alias of INSTANCE_OF. Both writings identify the same fact, with endpoints reversed; the alias does not grant an endpoint permission or add a fact.

For a declared Model entity `x`, `$a[<x>] ((INSTANCE_OF)) x` is a generic example: `$a` selects an existing instance of `x`; bare `x` denotes that Model entity. The example does not create either participant.

### Formal Claim

```python
# model
relation(source='$host', name='INSTANCE_OF', target='$target')
relation(source='Relation//HAS_INSTANCE', name='IS_INVERSE_ALIAS_FOR', target='Relation//INSTANCE_OF')
classify(address='Relation//INSTANCE_OF', axis='Derivation', value='Direct', notation='relation')
```

## Semantics

INSTANCE_OF relates an instance to its declared Model entity.
