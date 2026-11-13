---
atom_id: CA-R-2526
ref_id: CA-R-2526
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Scope Unit.ID
tier: 3
status: active
version: 7
updated_at: '2026-11-12T22:08:11.294473+00:00'
carrier_destination:
  file:
    name: CA-R-2526-CORE_META_MODEL-DECLARATION--declare-scope-unit-id.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Scope Unit ID

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name="ID",
    relation_name="IS_PROPERTY_OF",
    base_path="Scope Unit",
    property_occurrence_cardinality=1,
    value_format=str,
    value_cardinality=1,
    dependent_property_cardinality=0,
)
```

## Semantics

Every Scope Unit has a stable ID. A non-root Scope Unit keeps its ID through moves and renames; the ID distinguishes those operations from removal. `CA-SU--1` identifies the predefined Scope Unit named `world`.
