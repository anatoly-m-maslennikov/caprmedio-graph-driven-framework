---
atom_id: CA-R-2473
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_PROPERTY_OF
version: 5
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2473-CORE_META_MODEL-DECLARATION--define-property-bearing-and-its-inverse.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
---
## Summary

Define Property bearing and its inverse

## Claim

### Formal Claim

```CFEL
# model
$property ((IS_PROPERTY_OF)) $bearer;

Relation//IS_PROPERTY_OF ((HAS_INVERSE)) Relation//HAS_PROPERTY;

alias(Relation//IS_PROPERTY_OF) == ".";

Relation//IS_PROPERTY_OF ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

IS_PROPERTY_OF directs a Property to exactly one immediate bearer. HAS_PROPERTY is its derived inverse. The bearer relation is acyclic. `Bearer.Property` addresses the Property.

A Property has exactly one immediate bearer; the bearer may be any applicable declared model Entity or instance.

Forward `Host ((IS_PROPERTY_OF)) Target` and reverse `Target <((IS_PROPERTY_OF)) Host` are views of the same Relation fact.
In `X.Y`, Y IS_PROPERTY_OF X; traversal runs from bearer to Property.
IS_PROPERTY_OF relates Property to immediate bearer.
