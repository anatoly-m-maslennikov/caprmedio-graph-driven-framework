---
atom_id: CA-R-2961
ref_id: CA-R-2961
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Workflow.Content.Claim
tier: 3
status: active
version: 2
updated_at: '2026-11-13T03:15:59.506677+00:00'
carrier_destination:
  file:
    name: CA-R-2961-CORE_META_MODEL-DECLARATION--declare-workflow-content-claim.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Workflow.Content.Claim

## Claim

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name="Claim",
    relation_name="IS_PROPERTY_OF",
    base_path="Workflow.Content",
    property_occurrence_cardinality=1,
    value_cardinality=0,
    dependent_property_cardinality=Cardinality(minimum=1, maximum=3),
    allowed_dependent_property_names=("Mermaid Scheme", "Prose Claim", "Formal Claim"),
    ordered_dependent_property_pairs=(
        ("Mermaid Scheme", "Prose Claim"),
        ("Prose Claim", "Formal Claim"),
    ),
)
```

## Semantics

Workflow Claim has unique child Property names. At least one of Prose Claim and Formal Claim is present, and their text together specifies the Workflow completely without reliance on the Mermaid Scheme.
