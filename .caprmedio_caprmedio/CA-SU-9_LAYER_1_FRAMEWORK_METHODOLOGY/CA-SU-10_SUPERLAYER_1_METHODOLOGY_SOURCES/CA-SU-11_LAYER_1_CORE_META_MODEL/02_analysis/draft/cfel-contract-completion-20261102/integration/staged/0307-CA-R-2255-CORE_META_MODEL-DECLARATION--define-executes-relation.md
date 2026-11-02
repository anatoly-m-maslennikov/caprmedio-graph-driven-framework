---
atom_id: CA-R-2255
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation//EXECUTES
  passive:
  - Entity/Object/Occurrent/Runtime
  - Entity/Object/Occurrent/Execution/Workflow Run
version: 8
relations: {}
tier: 1
updated_at: 2026-11-02 07:52:54 +0400
role: Requirement
form: Declaration
---
## Summary

Define EXECUTES Relation

## Claim

EXECUTES connects an actual Runtime to a Workflow Run it executes. The stored direction is Runtime to Workflow Run. IS_EXECUTED_BY is its declared derived inverse and is not a second stored fact.

```CFEL
((EXECUTES)) ((HAS_INVERSE)) ((IS_EXECUTED_BY));

((EXECUTES)) >| Derivation == Direct;

$runtime ((EXECUTES)) $workflow_run
```

## Semantics



The Host is an actual Runtime and the Target is the Workflow Run it executes.
Forward `Host ((EXECUTES)) Target` and reverse `Target <((EXECUTES)) Host` are views of the same Relation fact.
EXECUTES relates Runtime to Workflow Run.

## Details

This named Type uses the general `((RELATION_TYPE))` form. It has no dedicated short Subject operator. This defines the reusable Type and its derived reverse view; it creates no Runtime or actual endpoint tuple.
