---
atom_id: CA-R-2638
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//RUNS
version: 2
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---

## Summary

Define RUNS

## Claim

```CFEL
Step// ((RUNS)) (in (Action, Workflow))//;
Substep// ((RUNS)) Action//;
((RUNS)) ((HAS_INVERSE)) ((IS_RUN_BY));
((RUNS)) >| Derivation == Direct
```

## Semantics

RUNS binds a Step or Substep invocation to its execution target. Its inverse is IS_RUN_BY.
