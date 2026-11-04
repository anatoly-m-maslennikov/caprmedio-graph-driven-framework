---
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//method_for
  passive:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
version: 31
updated_at: 2026-11-03 20:00:05 +0400
relations: {}
atom_id: CA-R-1017
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
carrier_destination:
  file:
    name: CA-R-1017-CORE_META_MODEL-DECLARATION--register-method-for-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1017-CORE_META_MODEL-DECLARATION--register-method-for-relation.md
  source_atom_id: CA-R-1017
  source_atom_revision: 31
  source_sha256: 4719ba251ad9e2f577804ca25f7573765d10c1059abef0b1b6a044bd5ea8b681
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register method_for relation

## Claim

### Formal Claim

```CFEL
# model
Relation//method_for ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom/(.Header.Role: Method)//$atom ((method_for)) Atom/(.Header.Role: Requirement)//$atom_2
```

### Prose Claim

#### Applicability
Method For Relation.

`method_for` **means** the direct relation from a Method Atom to the
Requirement Atom that the Method serves.

Forward `Host ((method_for)) Target` and reverse `Target <((method_for)) Host` are views of the same Relation fact.
method_for relates Method Atom to served Requirement Atom.
