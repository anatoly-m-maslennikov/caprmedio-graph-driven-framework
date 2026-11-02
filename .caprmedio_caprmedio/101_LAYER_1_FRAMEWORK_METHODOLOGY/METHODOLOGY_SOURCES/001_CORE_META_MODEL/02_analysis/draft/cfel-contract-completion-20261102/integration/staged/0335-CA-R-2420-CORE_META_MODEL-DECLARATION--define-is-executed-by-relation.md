---
atom_id: CA-R-2420
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CFEL <+ Relation//IS_EXECUTED_BY
relations: {}
version: 4
updated_at: 2026-11-02 07:52:54 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
---
## Summary

Define IS_EXECUTED_BY Relation

## Claim

IS_EXECUTED_BY is the declared derived inverse of EXECUTES; its full Runtime-to-Workflow Run meaning remains in CA-R-2255. No independently stored reverse fact is introduced.

```CFEL
((EXECUTES)) ((HAS_INVERSE)) ((IS_EXECUTED_BY));

((IS_EXECUTED_BY)) >| Derivation == Derived;
((IS_EXECUTED_BY)) ((IS_DERIVED_RELATION_OF)) ((EXECUTES));

$workflow_run ((IS_EXECUTED_BY)) $runtime
```

## Semantics



The Host is a Workflow Run and the Target is the actual Runtime that executes it.
Forward `Host ((IS_EXECUTED_BY)) Target` and reverse `Target <((IS_EXECUTED_BY)) Host` are views of the same Relation fact.
IS_EXECUTED_BY relates Workflow Run to Runtime. It is the derived inverse of EXECUTES; it does not add a separately authored fact.

