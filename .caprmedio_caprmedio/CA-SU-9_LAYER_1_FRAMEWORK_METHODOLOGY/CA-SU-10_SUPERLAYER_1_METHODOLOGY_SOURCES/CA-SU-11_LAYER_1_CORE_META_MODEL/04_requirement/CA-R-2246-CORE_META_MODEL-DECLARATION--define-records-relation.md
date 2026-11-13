---
atom_id: CA-R-2246
ref_id: CA-R-2246
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//RECORDS
  dependencies:
  - CAPRMEDIO_MODEL <+ Event Record
  - CAPRMEDIO_MODEL <+ Event
tier: 1
status: active
version: 9
updated_at: 2026-11-04 16:07:35 +0400
carrier_destination:
  file:
    name: CA-R-2246-CORE_META_MODEL-DECLARATION--define-records-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define RECORDS Relation

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_relation

declare_relation(
    relation_name="RECORDS",
    source_endpoint={"level": "instances", "entity_paths": ("Event Record",)},
    target_endpoint={"level": "instances", "entity_paths": ("Event",)},
    inverse_alias="IS_RECORDED_BY",
)
```

## Semantics

RECORDS is the stored Relation from an Event Record to the Event it describes. Its declared inverse IS_RECORDED_BY is a derived view; an Event Record is distinct from the Event.
