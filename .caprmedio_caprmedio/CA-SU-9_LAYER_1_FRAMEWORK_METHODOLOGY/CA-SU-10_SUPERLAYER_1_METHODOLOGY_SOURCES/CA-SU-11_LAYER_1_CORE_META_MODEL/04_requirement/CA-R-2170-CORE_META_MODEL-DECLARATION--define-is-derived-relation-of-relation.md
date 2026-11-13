---
atom_id: CA-R-2170
ref_id: CA-R-2170
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_DERIVED_RELATION_OF
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: active
version: 13
updated_at: '2026-11-12T18:19:27.964526+00:00'
carrier_destination:
  file:
    name: CA-R-2170-CORE_META_MODEL-DECLARATION--define-is-derived-relation-of-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define is derived relation of relation

## Claim

### Prose Claim

IS_DERIVED_RELATION_OF relates a derived Relation Type instance to its source Relation Type instance. It does not itself specify the endpoint transformation or any qualification. A direct Declaration's inverse binding entails the bound inverse's IS_DERIVED_RELATION_OF link to the direct Relation. A qualified derivation must retain its explicit qualification; it must not be normalized to an unconditional inverse.
### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='IS_DERIVED_RELATION_OF',
    source_endpoint={'level': 'instances', 'entity_paths': ('Relation',)},
    target_endpoint={'level': 'instances', 'entity_paths': ('Relation',)},
)
```

