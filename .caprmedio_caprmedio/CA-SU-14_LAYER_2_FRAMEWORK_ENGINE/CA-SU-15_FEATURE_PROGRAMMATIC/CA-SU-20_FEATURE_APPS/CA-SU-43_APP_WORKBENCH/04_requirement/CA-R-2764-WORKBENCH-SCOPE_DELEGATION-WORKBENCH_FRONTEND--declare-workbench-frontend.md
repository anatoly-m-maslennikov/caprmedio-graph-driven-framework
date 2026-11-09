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
  version: 4
  updated_at: 2026-11-09 17:00:18 +0400
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

The receiving Scope Unit is WORKBENCH_FRONTEND. Existing default Role and Form admissions remain applicable. The additional local Role/Form pairs are exactly:

- Method / Solution;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `CAPRMEDIO_MODEL <+ Projection`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Delivery <+ Packaging`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Code Authoring`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Query Authoring <+ SQL`;
- `PROJECT_STRUCTURE <+ Aspect//Visual Design`;

Each address selects one endpoint object, not the address string, other members of its type or descendants. An unresolved address is diagnostic and grants no admission. These permissions apply only to local Atoms whose Header.Container resolves to WORKBENCH_FRONTEND. The Scope Unit identity, Parent, responsibility and structural tree are unchanged.

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH_FRONTEND.ID == "CA-SU-46";

Scope Unit//WORKBENCH_FRONTEND.Name == "WORKBENCH_FRONTEND";

Scope Unit//WORKBENCH_FRONTEND.Label == "FEATURE";

Scope Unit//WORKBENCH_FRONTEND.order.ordered == false;

Scope Unit//WORKBENCH_FRONTEND ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH
```
