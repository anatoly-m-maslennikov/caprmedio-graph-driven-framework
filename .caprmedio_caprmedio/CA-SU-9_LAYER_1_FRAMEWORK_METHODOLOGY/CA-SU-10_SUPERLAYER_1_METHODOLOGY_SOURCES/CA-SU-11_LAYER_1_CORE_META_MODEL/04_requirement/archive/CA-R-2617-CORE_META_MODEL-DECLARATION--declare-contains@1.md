---
atom_id: CA-R-2617
role: Requirement
form: Declaration
status: Active
version: 1
updated_at: 2026-11-02 08:06:47 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//CONTAINS
relations: {}
---

## Summary

Declare CONTAINS

## Claim

A Container contains the directly contained Entity or instance. CONTAINS is the derived inverse of IS_CONTAINED_BY. It expresses the same fact and is not authored separately.

```CFEL
$container ((CONTAINS)) $part;
((IS_CONTAINED_BY)) ((HAS_INVERSE)) ((CONTAINS));

((CONTAINS)) == <+;

((CONTAINS)) >| Derivation == Derived;
((CONTAINS)) ((IS_DERIVED_RELATION_OF)) ((IS_CONTAINED_BY))
```

## Semantics

The Host is the immediate Container of the Target and must have the classification `Container = yes`.

Forward `Host ((CONTAINS)) Target` and reverse `Target <((CONTAINS)) Host` are views of the same Relation fact.

CONTAINS relates Container to immediate contained Entity or instance. It is the derived inverse of IS_CONTAINED_BY; it does not add a separately authored fact.
