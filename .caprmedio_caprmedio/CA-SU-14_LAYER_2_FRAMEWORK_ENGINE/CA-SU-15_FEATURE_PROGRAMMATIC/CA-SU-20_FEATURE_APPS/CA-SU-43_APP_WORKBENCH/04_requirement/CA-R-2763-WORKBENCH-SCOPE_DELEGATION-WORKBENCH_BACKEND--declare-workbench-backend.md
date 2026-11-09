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
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH_BACKEND
  tier: 3
state:
  status: Active
  version: 5
  updated_at: 2026-11-09 07:45:15 +0400
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

Own Workbench source reading, indexing, relation materialization, DuckDB and DuckPGQ query execution, stable paged results, saved-item Journal storage and read-only schema metadata. Shared Workbench requirements and cross-interface contracts remain in WORKBENCH. Existing legacy `q_<hex>.sql` and `w_<hex>.json` files are read-only fallback sources.

The receiving Scope Unit is WORKBENCH_BACKEND. Existing default Role and Form admissions remain applicable. The additional local Role/Form pairs are exactly:

- Delivery / Solution;
- Method / Solution;
- Requirement / Rule;

The admitted HAS_ACTIVE_SUBJECT targets are exactly the declared entities or instances at these addresses:

- `CAPRMEDIO_MODEL <+ CFEL <+ Relation`;
- `CAPRMEDIO_MODEL <+ Projection`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Development <+ Architecture <+ Communication <+ Interface Contracts`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Indexing`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Query Processing`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Schema`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ Source Retrieval`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Data Handling <+ State Synchronization`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Execution Control <+ Failure Handling`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Observability <+ Logging`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Operation <+ Storage <+ Temporary State`;
- `CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Performance <+ Measurement and Profiling`;

Each address selects one endpoint object, not the address string, other members of its type or descendants. An unresolved address is diagnostic and grants no admission. These permissions apply only to local Atoms whose Header.Container resolves to WORKBENCH_BACKEND. The Scope Unit identity, Parent, responsibility and structural tree are unchanged.

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH_BACKEND.ID == "CA-SU-45";

Scope Unit//WORKBENCH_BACKEND.Name == "WORKBENCH_BACKEND";

Scope Unit//WORKBENCH_BACKEND.Label == "FEATURE";

Scope Unit//WORKBENCH_BACKEND.order.ordered == false;

Scope Unit//WORKBENCH_BACKEND ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH
```
