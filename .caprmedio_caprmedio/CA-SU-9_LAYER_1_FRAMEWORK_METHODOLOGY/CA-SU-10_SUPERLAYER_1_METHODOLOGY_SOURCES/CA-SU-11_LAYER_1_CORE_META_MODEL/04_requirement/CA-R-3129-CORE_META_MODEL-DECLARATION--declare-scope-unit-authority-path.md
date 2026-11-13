---
identity:
  atom_id: CA-R-3129
  ref_id: CA-R-3129
context:
  role: requirement
  form: declaration
  container:
    scope_unit: CA-SU-11
  tier: 3
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Scope Unit.Paths.Authority
state:
  version: 1
  status: active
  updated_at: '2026-11-12T22:04:01.428900+00:00'
destination:
  file:
    name: CA-R-3129-CORE_META_MODEL-DECLARATION--declare-scope-unit-authority-path.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Declare Scope Unit Authority Path

## Claim

### Prose Claim

Authority is the Project-root-relative path to the Scope Unit’s Atom folder in the Project’s `.caprmedio_<project name>` tree. Use the actual folder names.

### Formal Claim

```python
from caprmedio.formal_claims import declare_entity

declare_entity(
    entity_name="Authority",
    relation_name="IS_PROPERTY_OF",
    base_path="Scope Unit.Paths",
    property_occurrence_cardinality=1,
    value_format=str,
    value_cardinality=1,
    dependent_property_cardinality=0,
)
```
