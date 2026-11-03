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
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_RUN_BY
relations: {}
---
## Summary

Declare IS_RUN_BY

## Claim

### Formal Claim

```CFEL
Relation//IS_RUN_BY <((HAS_INVERSE)) Relation//RUNS
```
