---
atom_id: CA-R-2480@2
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Archived
subjects:
  active: CFEL <+ Relation//RUN
version: 2
updated_at: 2026-11-02 00:18:22 +0400
relations: {}
tier: 3
role: Requirement
form: Relation Definition
---
## Summary

Define RUN

## Claim

RUN binds a Step or Substep to an Action for execution.

```CFEL
(in (Step, Substep))// ((RUN)) Action//;
Action// ((IS_RUN_BY)) (in (Step, Substep))//;
RUN ((HAS_INVERSE)) IS_RUN_BY
```
