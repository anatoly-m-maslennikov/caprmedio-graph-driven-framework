---
atom_id: CA-R-1021
ref_id: CA-R-1021
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//evidence_for
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: active
version: 34
updated_at: '2026-11-12T23:18:16.780674+00:00'
carrier_destination:
  file:
    name: CA-R-1021-CORE_META_MODEL-DECLARATION--register-evidence-for-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Register evidence_for relation

## Claim

### Prose Claim

evidence_for is the direct Relation owned by an evidence Carrier. The Host is that evidence Carrier and each tuple targets the Evaluation or Implementation Carrier it supports.

### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name='evidence_for',
    source_endpoint={'level': 'instances', 'entity_paths': ('Carrier',)},
    target_endpoint={'level': 'instances', 'entity_paths': ('Carrier',)},
)
```

