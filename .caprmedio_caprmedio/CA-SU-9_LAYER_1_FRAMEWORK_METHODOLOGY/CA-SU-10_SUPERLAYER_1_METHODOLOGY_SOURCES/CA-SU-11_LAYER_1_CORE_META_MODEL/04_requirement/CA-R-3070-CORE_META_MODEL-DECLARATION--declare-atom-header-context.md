---
identity:
  id: CA-R-3070
  ref_id: CA-R-3070
context:
  container:
    scope_unit: CA-SU-11
  role: requirement
  form: declaration
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Atom.Header.Context
  tier: 3
state:
  status: active
  version: 2
  updated_at: '2026-11-13T00:27:07.579107+00:00'
destination:
  file:
    name: CA-R-3070-CORE_META_MODEL-DECLARATION--declare-atom-header-context.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---


## Summary

Declare Atom.Header.Context

## Claim

### Prose Claim

A Role-specific group uses the Role name. A Form-specific group is nested in its Role-specific group and uses the Form name.

### Formal Claim

```python
from caprmedio.formal_claims import Cardinality, declare_entity

declare_entity(entity_name="Context", relation_name="IS_PROPERTY_OF", base_path="Atom.Header", property_occurrence_cardinality=1, value_cardinality=0, dependent_property_cardinality=Cardinality(minimum=5, maximum=7), allowed_dependent_property_names=("Container", "Role", "Form", "Label", "Topics", "Tier", "Plan", "Concern"), ordered_dependent_property_pairs=(("Container", "Role"), ("Role", "Form"), ("Form", "Label"), ("Label", "Topics"), ("Topics", "Tier")))
```
