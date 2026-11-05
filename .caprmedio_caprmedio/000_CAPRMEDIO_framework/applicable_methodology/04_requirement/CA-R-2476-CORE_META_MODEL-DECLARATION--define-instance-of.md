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
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2476-CORE_META_MODEL-DECLARATION--define-instance-of.md
  source_atom_id: CA-R-2476
  source_atom_revision: 6
  source_sha256: ae70ac12df63c5481a3c802c272b4252278816d12e9081b21db79f0c0b85496b
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
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

```CFEL
# model
Relation//INSTANCE_OF ((HAS_INVERSE)) Relation//HAS_INSTANCE;

alias(Relation//INSTANCE_OF) == "//";

Relation//INSTANCE_OF ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$instance ((INSTANCE_OF)) $kind;
```

