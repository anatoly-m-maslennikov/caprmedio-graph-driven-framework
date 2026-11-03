---
atom_id: CA-R-2623
role: Requirement
form: Declaration
status: Active
version: 3
updated_at: 2026-11-02 17:54:42 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_RUN_BY
relations: {}
---

## Summary

Declare IS_RUN_BY

## Claim

```CFEL
Action// ((IS_RUN_BY)) (in (Step, Substep))//;
Workflow// ((IS_RUN_BY)) Step//;
((IS_RUN_BY)) >| Derivation == Derived;
((IS_RUN_BY)) ((IS_DERIVED_RELATION_OF)) ((RUNS))
```

## Semantics

IS_RUN_BY is the derived inverse view of RUNS and is not authored as a separate fact.
