---
identity:
  atom_id: CA-R-2730
  ref_id: CA-R-2730
context:
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKBENCH
  tier: 3
  container:
    scope_unit: CA-SU-20
state:
  status: Active
  version: 5
  updated_at: 2026-11-11 15:29:41 +0400
destination:
  file:
    name: CA-R-2730-APPS-SCOPE_DELEGATION--declare-workbench.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/04_requirement
author: Anatoly Maslennikov
---

## Summary

Declare WORKBENCH

## Claim


### Prose Claim

The receiving Scope Unit is WORKBENCH. The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Observability <+ Logging`;

- `MODEL//CAPRMEDIO <+ Project`;
- `MODEL//CAPRMEDIO <+ Workspace`;
- `MODEL//CAPRMEDIO <+ View`;
- `MODEL//CAPRMEDIO <+ Projection`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Authoring <+ Query Authoring <+ SQL`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Indexing`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ State Synchronization`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Temporary State`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Performance <+ Measurement and Profiling`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Verification <+ Test Design`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//CODEX_EXTENSION`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKBENCH_BACKEND`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKBENCH_FRONTEND`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Component Structure`;


### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH.ID == "CA-SU-43";

Scope Unit//WORKBENCH.Name == "WORKBENCH";

Scope Unit//WORKBENCH.Label == "APP";

Scope Unit//WORKBENCH.order.ordered == false;

Scope Unit//WORKBENCH ((IS_CONTAINED_BY)) Scope Unit//APPS;

Atom/(.Header.Context.Container.scope_unit in ("CA-SU-43"))/(.Header.Context.Role in (Delivery)).Header.Context.Form :: Solution;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-43"))/(.Header.Context.Role in (Method)).Header.Context.Form :: Direct Policy;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-43"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Direct Policy;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-43"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Rule;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-43"))/(.Header.Context.Role in (Requirement)).Header.Context.Form :: Solution;
Atom/(.Header.Context.Container.scope_unit in ("CA-SU-43"))/(.Header.Context.Role in (Concern)).Header.Context.Form :: Problem;
```
