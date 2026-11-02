---
atom_id: CA-R-2421
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CFEL <+ Relation//IS_RECORDED_BY
relations: {}
version: 4
updated_at: 2026-11-02 08:06:47 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
---
## Summary

Define IS_RECORDED_BY Relation

## Claim

IS_RECORDED_BY is the declared derived inverse of RECORDS; its full Event Record meaning remains in CA-R-2246. No independently stored reverse fact is introduced.

```CFEL
((RECORDS)) ((HAS_INVERSE)) ((IS_RECORDED_BY));

((IS_RECORDED_BY)) >| Derivation == Derived;
((IS_RECORDED_BY)) ((IS_DERIVED_RELATION_OF)) ((RECORDS));

$occurrence ((IS_RECORDED_BY)) Event Record//
```

## Semantics



The Host is the actual Event or execution described by the Target Event Record.
Forward `Host ((IS_RECORDED_BY)) Target` and reverse `Target <((IS_RECORDED_BY)) Host` are views of the same Relation fact.
IS_RECORDED_BY relates actual Event or execution to Event Record. It is the derived inverse of RECORDS; it does not add a separately authored fact.

