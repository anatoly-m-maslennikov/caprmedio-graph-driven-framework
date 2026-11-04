---
atom_id: CA-R-2775
current_scope_unit: WORKBENCH_FRONTEND
claim_target_scope_unit: WORKBENCH_FRONTEND
status: Active
author: Anatoly Maslennikov
role: Requirement
form: Declaration
tier: 4
version: 1
subjects:
  active: PROJECT_STRUCTURE <+ Aspect//Visual Design
relations:
  depends_on:
  - CA-R-2543
carrier_destination:
  file:
    name: CA-R-2775-WORKBENCH_FRONTEND-DECLARATION--declare-visual-design-aspect.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-46_FEATURE_WORKBENCH_FRONTEND/04_requirement
updated_at: 2026-11-04 23:19:17 +0400
---

## Summary

Declare Visual Design Aspect for Workbench Frontend

## Claim

### Formal Claim

```CFEL
# project_structure
PROJECT_STRUCTURE <+ Aspect//Visual Design;
```

### Prose Claim

- WORKBENCH_FRONTEND uses Visual Design as a project-local Aspect.

## Semantics

Visual Design covers how the Workbench is presented to its Operator. It does not define query semantics, source authority or backend behavior.
