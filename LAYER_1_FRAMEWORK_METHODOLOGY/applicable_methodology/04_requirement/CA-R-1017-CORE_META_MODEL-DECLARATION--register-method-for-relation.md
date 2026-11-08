---
atom_id: CA-R-1017
ref_id: CA-R-1017
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//method_for
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: Active
version: 31
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1017-CORE_META_MODEL-DECLARATION--register-method-for-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1017-CORE_META_MODEL-DECLARATION--register-method-for-relation.md
  source_atom_id: CA-R-1017
  source_atom_revision: 31
  source_sha256: 23f52626ca55353aa97bebf359c123f180d0280d5bae76421957ad531cc0682f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register method_for relation

## Claim

### Prose Claim

#### Applicability
Method For Relation.

`method_for` **means** the direct relation from a Method Atom to the
Requirement Atom that the Method serves.

Forward `Host ((method_for)) Target` and reverse `Target <((method_for)) Host` are views of the same Relation fact.
method_for relates Method Atom to served Requirement Atom.
### Formal Claim

```CFEL
# model
Relation//method_for ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom/(.Header.Role: Method)//$atom ((method_for)) Atom/(.Header.Role: Requirement)//$atom_2
```

