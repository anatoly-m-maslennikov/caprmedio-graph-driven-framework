---
atom_id: CA-R-2521
ref_id: CA-R-2521
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Operations)/Action.Execution
    Kind
tier: 3
status: active
version: 4
updated_at: '2026-11-12T23:58:00.042337+00:00'
carrier_destination:
  file:
    name: CA-R-2521-CORE_META_MODEL-DECLARATION--declare-atom-role-operations-action-execution-kind.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---

## Summary

Declare Atom/(.Role := Operations)/Action.Execution Kind

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name="Execution Kind",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom/(.Header.Context.Role := Operations)/Action",
    property_occurrence_cardinality=1,
    value_format=str,
    value_cardinality=1,
    dependent_property_cardinality=0,
    allowed_values=("Programmatic", "Agentic"),
)
```

