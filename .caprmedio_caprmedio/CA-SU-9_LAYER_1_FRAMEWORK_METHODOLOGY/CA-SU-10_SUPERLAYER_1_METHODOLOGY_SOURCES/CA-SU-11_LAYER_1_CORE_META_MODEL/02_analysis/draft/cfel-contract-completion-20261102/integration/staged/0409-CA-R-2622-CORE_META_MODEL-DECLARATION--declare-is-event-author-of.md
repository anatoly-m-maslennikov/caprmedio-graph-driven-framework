---
atom_id: CA-R-2622
role: Requirement
form: Declaration
status: Active
version: 1
updated_at: 2026-11-02 08:06:47 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CFEL <+ Relation//IS_EVENT_AUTHOR_OF
relations: {}
---

## Summary

Declare IS_EVENT_AUTHOR_OF

## Claim

An Actor performed the event described by an Event Record. IS_EVENT_AUTHOR_OF is the derived inverse of HAS_EVENT_AUTHOR. It expresses the same fact and is not authored separately.

```CFEL
Actor// ((IS_EVENT_AUTHOR_OF)) Event Record//;
((HAS_EVENT_AUTHOR)) ((HAS_INVERSE)) ((IS_EVENT_AUTHOR_OF));

((IS_EVENT_AUTHOR_OF)) >| Derivation == Derived;
((IS_EVENT_AUTHOR_OF)) ((IS_DERIVED_RELATION_OF)) ((HAS_EVENT_AUTHOR))
```

## Semantics


Forward `Host ((IS_EVENT_AUTHOR_OF)) Target` and reverse `Target <((IS_EVENT_AUTHOR_OF)) Host` are views of the same Relation fact.
IS_EVENT_AUTHOR_OF relates Actor instance to Event Record instance. It is the derived inverse of HAS_EVENT_AUTHOR; it does not add a separately authored fact.

