---
identity:
  atom_id: CA-R-2775
  ref_id: CA-R-2775@3
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
  status: archived
  version: 3
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2775@3-WORKBENCH_FRONTEND-DECLARATION--declare-visual-design-aspect.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/04_requirement/099_archived
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

```CFEL
# project_structure
PROJECT STRUCTURE//CAPRMEDIO <+ Aspect//Visual Design;
```

## Semantics

Visual Design covers Operator presentation, not query semantics, source authority or backend behavior.
