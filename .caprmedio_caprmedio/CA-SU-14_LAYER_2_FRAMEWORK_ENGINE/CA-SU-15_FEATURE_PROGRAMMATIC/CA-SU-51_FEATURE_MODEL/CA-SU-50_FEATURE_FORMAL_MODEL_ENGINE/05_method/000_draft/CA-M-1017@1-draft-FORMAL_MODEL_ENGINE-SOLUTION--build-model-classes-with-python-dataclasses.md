---
identity:
  atom_id: CA-M-1017
  ref_id: CA-M-1017@1-draft
context:
  role: method
  form: solution
  tier: 3
  container:
    scope_unit: CA-SU-50
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FORMAL_MODEL_ENGINE
state:
  version: 1
  status: draft
  updated_at: '2026-11-13T16:16:47.381063+00:00'
destination:
  file:
    name: CA-M-1017@1-draft-FORMAL_MODEL_ENGINE-SOLUTION--build-model-classes-with-python-dataclasses.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-51_FEATURE_MODEL/CA-SU-50_FEATURE_FORMAL_MODEL_ENGINE/05_method/000_draft
relations:
  CONTRIBUTES_TO:
  - CA-R-3137
---
## Summary

Build Model classes with Python dataclasses

## Claim

### Prose Claim

- Use `declare_entity` for Nodes and Properties and `declare_relation` for Relations. Read fields and constraints from their Python Formal Claims.
- Generate classes with Python `@dataclass`. Use class inheritance for narrower kinds.
- Before each write, validate the complete proposed instance against its applicable Model rules. Reuse the declared types, allowed values, cardinalities, Relation contracts, and any declared `instance_check`.
- Use the standard decorator. Introduce a thin `@model_dataclass` only if it removes repeated class setup. Keep validation at the write boundary.
