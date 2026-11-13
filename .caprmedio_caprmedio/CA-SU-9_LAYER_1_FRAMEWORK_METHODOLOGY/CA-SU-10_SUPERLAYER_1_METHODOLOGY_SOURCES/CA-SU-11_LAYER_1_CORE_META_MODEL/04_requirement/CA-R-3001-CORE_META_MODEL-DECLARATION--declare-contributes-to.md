---
atom_id: CA-R-3001
ref_id: CA-R-3001
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTRIBUTES_TO
tier: 3
status: active
version: 3
updated_at: '2026-11-12T12:33:04.158402+00:00'
carrier_destination:
  file:
    name: CA-R-3001-CORE_META_MODEL-DECLARATION--declare-contributes-to.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare CONTRIBUTES_TO

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='CONTRIBUTES_TO',
    source_endpoint={'level': 'instances', 'entity_paths': ('Atom',)},
    target_endpoint={'level': 'instances', 'entity_paths': ('Atom',)},
)
```

## Semantics

The Host contributes toward the Target. Contribution is distinct from verified satisfaction of a Requirement.
