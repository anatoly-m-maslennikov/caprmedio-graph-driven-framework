---
identity:
  atom_id: CA-R-2764
  ref_id: CA-R-2764
context:
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH_FRONTEND
  tier: 3
  container:
    scope_unit: CA-SU-43
state:
  status: Active
  version: 2
  updated_at: 2026-11-08 22:18:08 +0400
destination:
  file:
    name: CA-R-2764-WORKBENCH-SCOPE_DELEGATION-WORKBENCH_FRONTEND--declare-workbench-frontend.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
---
## Summary

Declare WORKBENCH_FRONTEND

## Claim

### Prose Claim

Own the Workbench query UI, component palette, presentation, formatting, page navigation and frontend state. Shared Workbench requirements and cross-interface contracts remain in WORKBENCH.
The receiving Scope Unit is WORKBENCH_FRONTEND. These permissions apply only to local Atoms whose Header.Container-derived `IS_CONTAINED_BY` target is WORKBENCH_FRONTEND. Its default local admissions remain applicable. Its explicit local Role/Form pairs are Requirement / Declaration, Method / Decision, Evaluation / Eval Case, and Delivery / Decision. Each selection is limited to declared model entities or declared instances resolved at [`CAPRMEDIO_MODEL <+ Projection`, `PROJECT_STRUCTURE <+ Aspect//Visual Design`]. These selections identify endpoint objects, not strings, all members of a type, or descendants. An unresolved address is diagnostic and grants no admission.

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH_FRONTEND.ID == "CA-SU-46";

Scope Unit//WORKBENCH_FRONTEND.Name == "WORKBENCH_FRONTEND";

Scope Unit//WORKBENCH_FRONTEND.Label == "FEATURE";

Scope Unit//WORKBENCH_FRONTEND.order.ordered == false;

Scope Unit//WORKBENCH_FRONTEND ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH
```

