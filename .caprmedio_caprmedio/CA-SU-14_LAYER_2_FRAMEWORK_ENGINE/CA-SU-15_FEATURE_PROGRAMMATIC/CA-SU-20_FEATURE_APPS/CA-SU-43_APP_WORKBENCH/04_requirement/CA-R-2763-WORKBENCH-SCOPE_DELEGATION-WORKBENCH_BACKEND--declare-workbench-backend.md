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
  version: 4
  updated_at: 2026-11-08 22:18:08 +0400
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
The receiving Scope Unit is WORKBENCH_BACKEND. These permissions apply only to local Atoms whose Header.Container-derived `IS_CONTAINED_BY` target is WORKBENCH_BACKEND. Its default local admissions remain applicable. Its explicit local Role/Form pairs are Requirement / Rule, Method / Decision, Method / Solution, Evaluation / Eval Case, Delivery / Decision, and Delivery / Solution. Each selection is limited to declared model entities or declared instances resolved at [`CAPRMEDIO_MODEL <+ Projection`, `CAPRMEDIO_MODEL <+ CFEL <+ Relation`]. These selections identify endpoint objects, not strings, all members of a type, or descendants. An unresolved address is diagnostic and grants no admission.

### Formal Claim

```CFEL
# instances
Scope Unit//WORKBENCH_BACKEND.ID == "CA-SU-45";

Scope Unit//WORKBENCH_BACKEND.Name == "WORKBENCH_BACKEND";

Scope Unit//WORKBENCH_BACKEND.Label == "FEATURE";

Scope Unit//WORKBENCH_BACKEND.order.ordered == false;

Scope Unit//WORKBENCH_BACKEND ((IS_CONTAINED_BY)) Scope Unit//WORKBENCH
```

