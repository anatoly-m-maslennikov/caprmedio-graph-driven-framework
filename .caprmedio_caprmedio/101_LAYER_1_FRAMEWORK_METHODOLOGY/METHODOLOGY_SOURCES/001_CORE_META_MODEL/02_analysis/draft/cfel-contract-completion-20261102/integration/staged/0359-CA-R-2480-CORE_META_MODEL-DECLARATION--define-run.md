---
atom_id: CA-R-2480
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation//RUN
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Define RUN

## Claim

RUN binds a Step or Substep to an Action for execution.

```CFEL
(in (Step, Substep))// ((RUN)) Action//;
Action// ((IS_RUN_BY)) (in (Step, Substep))//;
((RUN)) ((HAS_INVERSE)) ((IS_RUN_BY));

((RUN)) >| Derivation == Direct
```

## Semantics


Forward `Host ((RUN)) Target` and reverse `Target <((RUN)) Host` are views of the same Relation fact.
RUN relates Step or Substep instance to Action instance.

