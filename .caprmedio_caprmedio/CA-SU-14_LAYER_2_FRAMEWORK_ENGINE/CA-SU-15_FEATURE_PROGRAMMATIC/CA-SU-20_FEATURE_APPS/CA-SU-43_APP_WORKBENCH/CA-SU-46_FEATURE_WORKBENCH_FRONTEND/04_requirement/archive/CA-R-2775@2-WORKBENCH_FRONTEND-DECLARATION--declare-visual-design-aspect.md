---
identity:
  atom_id: CA-R-2775
  ref_id: CA-R-2775@2
context:
  container:
    scope_unit: CA-SU-46
  role: Requirement
  form: Declaration
  topics:
    main_subject: PROJECT_STRUCTURE <+ Aspect//Visual Design
  tier: 4
relations:
  depends_on:
  - CA-R-2543
state:
  status: Archived
  version: 2
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-R-2775@2-WORKBENCH_FRONTEND-DECLARATION--declare-visual-design-aspect.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/04_requirement/archive
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
author: Anatoly Maslennikov
---

## Summary

Declare Visual Design Aspect for Workbench Frontend

## Claim

### Prose Claim

- WORKBENCH_FRONTEND uses Visual Design as a project-local Aspect.

### Formal Claim

```CFEL
# project_structure
PROJECT_STRUCTURE <+ Aspect//Visual Design;
```

## Semantics

Visual Design covers how the Workbench is presented to its Operator. It does not define query semantics, source authority or backend behavior.
