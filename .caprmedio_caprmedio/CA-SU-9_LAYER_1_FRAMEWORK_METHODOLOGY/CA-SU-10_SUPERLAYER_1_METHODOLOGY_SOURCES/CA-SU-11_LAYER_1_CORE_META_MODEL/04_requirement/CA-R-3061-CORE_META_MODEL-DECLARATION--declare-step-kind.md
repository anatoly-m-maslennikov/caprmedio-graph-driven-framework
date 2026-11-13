---
atom_id: CA-R-3061
ref_id: CA-R-3061
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ Step.Kind
tier: 3
status: active
version: 3
updated_at: '2026-11-12T23:10:04.194712+00:00'
carrier_destination:
  file:
    name: CA-R-3061-CORE_META_MODEL-DECLARATION--declare-step-kind.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---

## Summary

Declare Step.Kind

## Claim

### Prose Claim

A Step has exactly one Kind: Input, Execution, or Decision. Kind classifies the Step in the Workflow and is independent of its Agentic Step Execution Context.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(entity_name='Kind', relation_name="IS_PROPERTY_OF", base_path='Atom/(.Header.Context.Role:=Operations)/Step', property_occurrence_cardinality=1, value_cardinality=1, allowed_values=("Input", "Execution", "Decision"))
```
