---
atom_id: CA-R-1017
ref_id: CA-R-1017
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//method_for
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: active
version: 32
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-1017-CORE_META_MODEL-DECLARATION--register-method-for-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Register method_for relation

## Claim

### Prose Claim

#### Applicability
Method For Relation.

`method_for` **means** the direct relation from a Method Atom to the
Requirement Atom that the Method serves.

Forward `Host ((method_for)) Target` and reverse `Target <((method_for)) Host` are views of the same Relation fact.
method_for relates Method Atom to served Requirement Atom.
### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='method_for',
    source_endpoint={'level': 'instances', 'entity_paths': ('Atom/(.Header.Context.Role := Method)',)},
    target_endpoint={'level': 'instances', 'entity_paths': ('Atom/(.Header.Context.Role := Requirement)',)},
)
```

