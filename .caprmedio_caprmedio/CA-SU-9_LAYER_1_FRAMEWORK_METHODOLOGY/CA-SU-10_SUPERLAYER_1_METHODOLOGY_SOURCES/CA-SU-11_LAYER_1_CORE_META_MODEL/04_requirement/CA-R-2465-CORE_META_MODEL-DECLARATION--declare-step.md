---
atom_id: CA-R-2465
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ Atom/(.Header.Role := Operations)/Step
version: 4
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Declare Step

## Claim

### Formal Claim

```CFEL
Atom/(.Header.Role: Operations)/Step;
Step//{:1}((IS_CONTAINED_BY)) Workflow//;
IF Step// {=0}((RUNS)) THEN Step// {:1+}((CONTAINS)) Substep//;
IF Step// {>0}((RUNS)) THEN Step// {:0}((CONTAINS));
IF Step// {=0}((CONTAINS)) THEN Step// {:1}((RUNS)) (in (Action, Workflow))//
```

## Semantics

A Step is a unit of work within a Workflow.
