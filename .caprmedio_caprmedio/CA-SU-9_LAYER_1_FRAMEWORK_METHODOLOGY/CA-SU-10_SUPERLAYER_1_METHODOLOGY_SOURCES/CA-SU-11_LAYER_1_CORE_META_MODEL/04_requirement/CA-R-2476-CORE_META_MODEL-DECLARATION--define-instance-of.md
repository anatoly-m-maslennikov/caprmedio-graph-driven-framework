---
atom_id: CA-R-2476
ref_id: CA-R-2476
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//INSTANCE_OF
tier: 3
status: Active
version: 6
updated_at: 2026-11-04 05:21:15 +0400
carrier_destination:
  file:
    name: CA-R-2476-CORE_META_MODEL-DECLARATION--define-instance-of.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
---
## Summary

Define INSTANCE_OF

## Claim

### Prose Claim

The Host is an instance of the Target declared kind. A Property instance is borne by its data bearer and is an instance of its corresponding model Property, which remains borne by its model bearer. A Property instance has no independent Carrier; its bearer and kind Relations are distinct and may coexist.

Forward `Host ((INSTANCE_OF)) Target` and reverse `Target <((INSTANCE_OF)) Host` are views of the same Relation fact.
In `X//Y`, Y INSTANCE_OF X; traversal runs from kind to instance.
INSTANCE_OF relates instance of a declared kind to declared kind.
### Formal Claim

```python
# model
relation(source='Relation//INSTANCE_OF', name='HAS_INVERSE', target='Relation//HAS_INSTANCE')
set_value(address='alias(Relation//INSTANCE_OF)', value='"//"')
classify(address='Relation//INSTANCE_OF', axis='Derivation', value='Direct', notation='relation')
# instances
relation(source='$instance', name='INSTANCE_OF', target='$kind')
```

