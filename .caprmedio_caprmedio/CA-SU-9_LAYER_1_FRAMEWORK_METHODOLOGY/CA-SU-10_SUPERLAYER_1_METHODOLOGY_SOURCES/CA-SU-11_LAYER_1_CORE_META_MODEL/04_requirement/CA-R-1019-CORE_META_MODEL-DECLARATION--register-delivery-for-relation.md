---
atom_id: CA-R-1019
ref_id: CA-R-1019
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//delivery_for
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: active
version: 31
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-1019-CORE_META_MODEL-DECLARATION--register-delivery-for-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register delivery_for relation

## Claim

### Prose Claim

#### Applicability
`delivery_for` relations.

`delivery_for` **means** the direct relation from a Delivery Atom to the Atom
that the Delivery realizes.

Forward `Host ((delivery_for)) Target` and reverse `Target <((delivery_for)) Host` are views of the same Relation fact.
delivery_for relates Delivery Atom to realized Atom.
### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='delivery_for',
    source_endpoint={'level': 'instances', 'entity_paths': ('Atom/(.Header.Context.Role := Delivery)',)},
    target_endpoint={'level': 'instances', 'entity_paths': ('Atom',)},
)
```

