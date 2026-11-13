---
atom_id: CA-R-2969
ref_id: CA-R-2969
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Step.Content.Claim.Mermaid Scheme
  dependencies:
  - CAPRMEDIO_MODEL <+ Workflow.Content.Claim.Mermaid Scheme
tier: 3
status: active
version: 2
updated_at: '2026-11-12T18:39:04.030100+00:00'
carrier_destination:
  file:
    name: CA-R-2969-CORE_META_MODEL-DECLARATION--declare-step-content-claim-mermaid-scheme.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Step.Content.Claim.Mermaid Scheme

## Claim

### Prose Claim

Mermaid Scheme semantics: [Workflow Mermaid Scheme declaration](CA-R-2962-CORE_META_MODEL-DECLARATION--declare-workflow-content-claim-mermaid-scheme.md#semantics).

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(
    entity_name="Mermaid Scheme",
    relation_name="IS_PROPERTY_OF",
    base_path='Atom/(.Header.Context.Role := Operations)/(.Header.Context.Form := Step).Content.Claim',
    property_occurrence_cardinality=Cardinality(minimum=0, maximum=1),
    value_format="markdown",
    value_cardinality=1,
    dependent_property_cardinality=0,
)
```
