---
identity:
  atom_id: CA-R-2763
  ref_id: CA-R-2763
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Scope Delegation
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Scope Unit//WORKBENCH_BACKEND
  tier: 3
state:
  status: Active
  version: 6
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2763-WORKBENCH-SCOPE_DELEGATION-WORKBENCH_BACKEND--declare-workbench-backend.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Declare WORKBENCH_BACKEND

## Claim

### Prose Claim

Own Workbench source reading, indexing, relation materialization, DuckDB and DuckPGQ query execution, shared source-adapter updates under CA-R-2728, stable paged results, saved-item Journal storage and read-only schema metadata. Shared Workbench requirements and cross-interface contracts remain in WORKBENCH. Existing legacy `q_<hex>.sql` and `w_<hex>.json` files are read-only fallback sources.

The receiving Scope Unit is WORKBENCH_BACKEND. The additional local Role/Form pairs are exactly:

- Delivery / Solution;
- Method / Solution;
- Requirement / Rule;

- Concern / Problem;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `MODEL//CAPRMEDIO <+ CFEL <+ Relation`;
- `MODEL//CAPRMEDIO <+ Projection`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Indexing`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Query Processing`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Schema`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Retrieval`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ State Synchronization`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Failure Handling`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Observability <+ Logging`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Temporary State`;
- `PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality <+ Performance <+ Measurement and Profiling`;

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH_BACKEND.ID == "CA-SU-45";

Scope Unit//WORKBENCH_BACKEND.Name == "WORKBENCH_BACKEND";

Scope Unit//WORKBENCH_BACKEND.Label == "FEATURE";

Scope Unit//WORKBENCH_BACKEND.order.ordered == false;

Scope Unit//WORKBENCH_BACKEND ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH
```
