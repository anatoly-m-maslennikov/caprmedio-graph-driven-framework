---
atom_id: CA-R-2476
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation//INSTANCE_OF
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2476-CORE_META_MODEL-DECLARATION--define-instance-of.md
  source_atom_id: CA-R-2476
  source_atom_revision: 4
  source_sha256: c69deb7dc4fe259191cf373bc36a9ab472dc6b87538f1c3e36eff1dd89fe516a
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define INSTANCE_OF

## Claim

```CFEL
$instance ((INSTANCE_OF)) $kind;
((INSTANCE_OF)) ((HAS_INVERSE)) ((HAS_INSTANCE));

((INSTANCE_OF)) == //;
((INSTANCE_OF)) >| Derivation == Direct
```

## Semantics

The Host is an instance of the Target declared kind; a Property kind is not independently instantiated.



Forward `Host ((INSTANCE_OF)) Target` and reverse `Target <((INSTANCE_OF)) Host` are views of the same Relation fact.
In `X//Y`, Y INSTANCE_OF X; traversal runs from kind to instance.
INSTANCE_OF relates instance of a declared kind to declared kind.

