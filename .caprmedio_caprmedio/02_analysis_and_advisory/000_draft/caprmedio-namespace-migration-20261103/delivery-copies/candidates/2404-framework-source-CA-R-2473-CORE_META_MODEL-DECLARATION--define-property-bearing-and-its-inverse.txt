---
atom_id: CA-R-2473
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
---
## Summary

Define Property bearing and its inverse

## Claim

IS_PROPERTY_OF directs a Property to exactly one immediate bearer. HAS_PROPERTY is its derived inverse. The bearer relation is acyclic. `Bearer.Property` addresses the Property.

```CFEL
$property ((IS_PROPERTY_OF)) $bearer;
((IS_PROPERTY_OF)) ((HAS_INVERSE)) ((HAS_PROPERTY));

((IS_PROPERTY_OF)) == .;
((IS_PROPERTY_OF)) >| Derivation == Direct
```

## Semantics

A Property has exactly one immediate bearer; the bearer may be any applicable declared model Entity or instance.



Forward `Host ((IS_PROPERTY_OF)) Target` and reverse `Target <((IS_PROPERTY_OF)) Host` are views of the same Relation fact.
In `X.Y`, Y IS_PROPERTY_OF X; traversal runs from bearer to Property.
IS_PROPERTY_OF relates Property to immediate bearer.

