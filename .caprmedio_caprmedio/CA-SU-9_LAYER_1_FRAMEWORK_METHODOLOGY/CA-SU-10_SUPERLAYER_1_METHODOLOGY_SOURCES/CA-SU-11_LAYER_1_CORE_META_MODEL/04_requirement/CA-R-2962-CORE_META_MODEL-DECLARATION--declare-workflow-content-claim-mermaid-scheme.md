---
atom_id: CA-R-2962
ref_id: CA-R-2962
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Workflow.Content.Claim.Mermaid Scheme
tier: 3
status: active
version: 2
updated_at: '2026-11-12T17:23:54+00:00'
carrier_destination:
  file:
    name: CA-R-2962-CORE_META_MODEL-DECLARATION--declare-workflow-content-claim-mermaid-scheme.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Workflow.Content.Claim.Mermaid Scheme

## Claim

### Prose Claim

The scheme shows all Workflow Steps, including nested Steps.

### Formal Claim

```python
# model
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name='Mermaid Scheme',
    relation_name='IS_PROPERTY_OF',
    base_path='Workflow.Content.Claim',
    property_occurrence_cardinality=1,
    value_cardinality=1,
    value_format='markdown',
    dependent_property_cardinality=0,
)
```

## Semantics

The value is exactly one `mermaid`-labelled fenced Markdown block. A Mermaid Scheme is a visual Minto summary of its owning Claim's text: removing it must leave that text's specification complete and unchanged. It may repeat the text.
