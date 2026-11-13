---
atom_id: CA-R-2711
ref_id: CA-R-2711
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Atom/(.Header.Context.Role := Plan).Header.Context.Plan.AI
    Agent Confidence Threshold
tier: 3
status: active
version: 8
updated_at: '2026-11-13T04:30:30.919333+00:00'
carrier_destination:
  file:
    name: CA-R-2711-CORE_META_MODEL-DECLARATION--declare-atom-header-role-plan-header-ai-agent-confidence-threshold.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Atom/(.Header.Role := Plan).Header.AI Agent Confidence Threshold

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name="AI Agent Confidence Threshold",
    relation_name="IS_PROPERTY_OF",
    base_path="Atom/(.Header.Context.Role:=Plan).Header.Context.Plan",
    value_format=int,
    value_cardinality=Cardinality(minimum=0, maximum=1),
    minimum_value=0,
    maximum_value=100,
    dependent_property_cardinality=0,
    fallback_chain=(
        {
            "lookup_relation": "IS_CONTAINED_BY",
            "lookup_property": "Atom/(.Header.Context.Role:=Plan).Header.Context.Plan.AI Agent Confidence Threshold",
        },
        {
            "project_entity": "Project",
            "project_property": "Project.Settings.AI Agent Confidence Threshold",
        },
    ),
)
```
