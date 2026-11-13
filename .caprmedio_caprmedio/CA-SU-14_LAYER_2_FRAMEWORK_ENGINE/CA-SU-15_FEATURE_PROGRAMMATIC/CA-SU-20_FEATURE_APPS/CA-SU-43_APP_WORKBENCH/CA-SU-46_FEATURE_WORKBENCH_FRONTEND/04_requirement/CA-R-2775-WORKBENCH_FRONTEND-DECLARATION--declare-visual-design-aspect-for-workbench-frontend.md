---
identity:
  atom_id: CA-R-2775
  ref_id: CA-R-2775
context:
  container:
    scope_unit: CA-SU-46
  role: Requirement
  form: Declaration
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspect//Visual Design
    dependencies:
    - MODEL//CAPRMEDIO <+ Aspect
  tier: 4
relations: {}
state:
  status: active
  version: 4
  updated_at: '2026-11-13T05:19:37.263532+00:00'
destination:
  file:
    name: CA-R-2775-WORKBENCH_FRONTEND-DECLARATION--declare-visual-design-aspect-for-workbench-frontend.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/04_requirement
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---
## Summary

Declare Visual Design Aspect for Workbench Frontend

## Claim

### Prose Claim

WORKBENCH_FRONTEND uses Visual Design as a project-local Aspect.

### Formal Claim

```python
# project_structure
composition(container="PROJECT STRUCTURE//CAPRMEDIO", parts=("Aspect//Visual Design",))
```

## Semantics

Visual Design covers Operator presentation, not query semantics, source authority or backend behavior.
