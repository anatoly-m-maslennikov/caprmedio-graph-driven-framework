---
atom_id: CA-R-2763
role: Requirement
form: Scope Unit Declaration
status: Archived
version: 1
updated_at: 2026-11-04 17:55:47 +0400
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH_BACKEND
relations: {}
---
## Summary

Declare WORKBENCH_BACKEND

## Claim

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH_BACKEND.ID == "CA-SU-45";

Scope Unit//WORKBENCH_BACKEND.Name == "WORKBENCH_BACKEND";

Scope Unit//WORKBENCH_BACKEND.Label == "FEATURE";

Scope Unit//WORKBENCH_BACKEND.order.ordered == false;

Scope Unit//WORKBENCH_BACKEND ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH
```

### Prose Claim

Own Workbench source reading, indexing, relation materialization, DuckDB and DuckPGQ query execution, and stable paged results. Shared Workbench requirements and cross-interface contracts remain in WORKBENCH.
