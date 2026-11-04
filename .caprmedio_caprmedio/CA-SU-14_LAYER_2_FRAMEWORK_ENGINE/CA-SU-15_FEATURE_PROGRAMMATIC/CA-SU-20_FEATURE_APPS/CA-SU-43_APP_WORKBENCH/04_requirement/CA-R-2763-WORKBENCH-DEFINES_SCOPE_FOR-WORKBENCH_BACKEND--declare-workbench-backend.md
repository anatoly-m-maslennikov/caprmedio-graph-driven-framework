---
atom_id: CA-R-2763
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH_BACKEND
status: Active
version: 3
author: Anatoly Maslennikov
role: Requirement
form: Scope Unit Declaration
tier: 3
subjects:
  active: CAPRMEDIO_STRUCTURE <+ Scope Unit//WORKBENCH_BACKEND
relations: {}
carrier_destination:
  file:
    name: CA-R-2763-WORKBENCH-DEFINES_SCOPE_FOR-WORKBENCH_BACKEND--declare-workbench-backend.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
updated_at: 2026-11-05 01:40:28 +0400
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

Own Workbench source reading, indexing, relation materialization, DuckDB and DuckPGQ query execution, stable paged results, saved-item Journal storage and read-only schema metadata. Shared Workbench requirements and cross-interface contracts remain in WORKBENCH. Existing legacy `q_<hex>.sql` and `w_<hex>.json` files are read-only fallback sources.
