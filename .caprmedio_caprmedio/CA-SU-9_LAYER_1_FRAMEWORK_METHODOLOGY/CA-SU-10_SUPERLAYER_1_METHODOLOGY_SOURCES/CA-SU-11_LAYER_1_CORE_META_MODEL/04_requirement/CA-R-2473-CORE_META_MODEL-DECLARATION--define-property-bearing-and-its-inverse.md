---
atom_id: CA-R-2473
ref_id: CA-R-2473
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
tier: 3
status: active
version: 6
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-2473-CORE_META_MODEL-DECLARATION--define-property-bearing-and-its-inverse.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define Property bearing and its inverse

## Claim

### Prose Claim

IS_PROPERTY_OF directs a Property to exactly one immediate bearer. HAS_PROPERTY is its derived inverse. The bearer relation is acyclic. `Bearer.Property` addresses the Property.

A Property has exactly one immediate bearer; the bearer may be any applicable declared model Entity or instance.

Forward `Host ((IS_PROPERTY_OF)) Target` and reverse `Target <((IS_PROPERTY_OF)) Host` are views of the same Relation fact.
In `X.Y`, Y IS_PROPERTY_OF X; traversal runs from bearer to Property.
IS_PROPERTY_OF relates Property to immediate bearer.
### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='IS_PROPERTY_OF',
    source_endpoint={'level': 'model_entities_or_instances', 'dependency': 'property'},
    target_endpoint={'level': 'model_entities_or_instances'},
    inverse_alias='HAS_PROPERTY',
    written_alias='.',
    targets_per_source=1,
    acyclic=True,
)
```

