---
atom_id: CA-R-2951
ref_id: CA-R-2951
container:
  scope_unit: CA-SU-11
role: Requirement
form: Relation Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_INVERSE_ALIAS_FOR
tier: 3
status: active
version: 2
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-2951-CORE_META_MODEL-RELATION_DECLARATION--declare-is-inverse-alias-for.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare IS_INVERSE_ALIAS_FOR

## Claim

### Prose Claim

IS_INVERSE_ALIAS_FOR binds an inverse alias model address to its canonical Relation model address. The inverse alias is introduced by the canonical Relation Declaration and is not a separate Relation entity or Declaration. Normalizing an inverse alias to its canonical Relation swaps the written endpoints and their cardinality slots, preserving the numeric bounds. Explicit reverse writing of an inverse alias reverses its endpoints and slots again. Both writings refer to the same fact. This binding infers no bounds, grants no endpoint permission and creates no second authored Relation fact.

### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='IS_INVERSE_ALIAS_FOR',
    source_endpoint={'level': 'model_entities',
 'entity_paths': ('Relation',),
 'address_form': 'inverse_alias'},
    target_endpoint={'level': 'model_entities', 'entity_paths': ('Relation',), 'address_form': 'canonical'},
    swap_endpoints=True,
    swap_endpoint_cardinalities=True,
)
```

## Semantics

IS_INVERSE_ALIAS_FOR relates an inverse alias address to its canonical Relation address.
