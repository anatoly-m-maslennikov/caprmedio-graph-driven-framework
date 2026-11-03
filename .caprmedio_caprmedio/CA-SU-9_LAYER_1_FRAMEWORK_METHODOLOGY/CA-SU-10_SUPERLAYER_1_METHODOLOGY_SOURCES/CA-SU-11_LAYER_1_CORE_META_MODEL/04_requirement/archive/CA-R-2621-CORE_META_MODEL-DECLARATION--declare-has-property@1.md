---
atom_id: CA-R-2621
role: Requirement
form: Declaration
status: Active
version: 1
updated_at: 2026-11-02 08:06:47 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//HAS_PROPERTY
relations: {}
---

## Summary

Declare HAS_PROPERTY

## Claim

A bearer has its dependent Property. HAS_PROPERTY is the derived inverse of IS_PROPERTY_OF. It expresses the same fact and is not authored separately.

```CFEL
$bearer ((HAS_PROPERTY)) $property;
((IS_PROPERTY_OF)) ((HAS_INVERSE)) ((HAS_PROPERTY));

((HAS_PROPERTY)) >| Derivation == Derived;
((HAS_PROPERTY)) ((IS_DERIVED_RELATION_OF)) ((IS_PROPERTY_OF))
```

## Semantics

The Target is a Property borne directly by the Host.


Forward `Host ((HAS_PROPERTY)) Target` and reverse `Target <((HAS_PROPERTY)) Host` are views of the same Relation fact.
HAS_PROPERTY relates Node or Property to dependent Property. It is the derived inverse of IS_PROPERTY_OF; it does not add a separately authored fact.

