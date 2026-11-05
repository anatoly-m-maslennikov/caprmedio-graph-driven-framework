---
atom_id: CA-R-2476
status: Draft
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//INSTANCE_OF
version: 7
updated_at: 2026-11-05 05:13:56 +0400
relations:
  IS_CONTAINED_BY:
    scope_unit: CA-SU-11
tier: 3
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-2476@7-draft-CORE_META_MODEL-DECLARATION--define-instance-of.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/draft
---
## Summary

Define INSTANCE_OF

## Claim

### Formal Claim

```CFEL
# model
Relation//INSTANCE_OF ((HAS_INVERSE)) Relation//HAS_INSTANCE;

Relation//INSTANCE_OF ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$instance ((INSTANCE_OF)) $kind;
```

### Prose Claim

The Host is an instance of the Target declared kind. A Property instance is borne by its data bearer and is an instance of its corresponding model Property, which remains borne by its model bearer. A Property instance has no independent Carrier; its bearer and kind Relations are distinct and may coexist.

Forward `Host ((INSTANCE_OF)) Target` and reverse `Target <((INSTANCE_OF)) Host` are views of the same Relation fact.
INSTANCE_OF relates instance of a declared kind to declared kind.
