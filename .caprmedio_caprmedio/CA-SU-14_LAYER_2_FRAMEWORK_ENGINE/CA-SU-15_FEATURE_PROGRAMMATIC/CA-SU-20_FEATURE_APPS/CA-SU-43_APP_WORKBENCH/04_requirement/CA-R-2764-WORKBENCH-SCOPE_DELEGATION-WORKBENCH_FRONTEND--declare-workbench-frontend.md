---
identity:
  atom_id: CA-R-2764
  ref_id: CA-R-2764
context:
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKBENCH_FRONTEND
  tier: 3
  container:
    scope_unit: CA-SU-43
state:
  status: Active
  version: 6
  updated_at: 2026-11-11 15:29:41 +0400
destination:
  file:
    name: CA-R-2764-WORKBENCH-SCOPE_DELEGATION-WORKBENCH_FRONTEND--declare-workbench-frontend.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
relations:
  depends_on:
  - CA-R-3022
author: Anatoly Maslennikov
---

## Summary

Declare WORKBENCH_FRONTEND

## Claim

### Prose Claim

Own the Workbench query UI, component palette, presentation, formatting, page navigation and frontend state. Shared Workbench requirements and cross-interface contracts remain in WORKBENCH.

The receiving Scope Unit is WORKBENCH_FRONTEND. The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `MODEL//CAPRMEDIO <+ Projection`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Delivery <+ Packaging`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Code Authoring`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Query Authoring <+ SQL`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspect//Visual Design`;

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering <+ Libraries and Frameworks`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering <+ Component Authoring`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Frontend Engineering <+ Code Style`;

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH_FRONTEND.ID == "CA-SU-46";

Scope Unit//WORKBENCH_FRONTEND.Name == "WORKBENCH_FRONTEND";

Scope Unit//WORKBENCH_FRONTEND.Label == "FEATURE";

Scope Unit//WORKBENCH_FRONTEND.order.ordered == false;

Scope Unit//WORKBENCH_FRONTEND ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH;

Atom/(.Header.Context.Container.scope_unit in ("CA-SU-46"))/(.Header.Context.Role in (Method)).Header.Context.Form :: Solution;
```
