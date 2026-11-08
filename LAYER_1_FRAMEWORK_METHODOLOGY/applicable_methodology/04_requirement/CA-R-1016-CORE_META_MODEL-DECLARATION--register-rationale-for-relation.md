---
atom_id: CA-R-1016
ref_id: CA-R-1016
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//rationale_for
  dependencies:
  - CAPRMEDIO_MODEL <+ CFEL <+ Relation
tier: 1
status: Active
version: 32
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1016-CORE_META_MODEL-DECLARATION--register-rationale-for-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1016-CORE_META_MODEL-DECLARATION--register-rationale-for-relation.md
  source_atom_id: CA-R-1016
  source_atom_revision: 32
  source_sha256: 052b70b178a1449ac1e9b435956a52024c00196a04b5f089433e0f590da773e0
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register rationale_for relation

## Claim

### Prose Claim

#### Applicability
Rationale For Relation.

`rationale_for` **means** the direct relation from a Rationale Analysis & Advisory Atom
to the Atom that it explains.

Forward `Host ((rationale_for)) Target` and reverse `Target <((rationale_for)) Host` are views of the same Relation fact.
rationale_for relates Rationale Analysis & Advisory Atom to explained Atom.
### Formal Claim

```CFEL
# model
Relation//rationale_for ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Atom/(.Header.Role: "Analysis & Advisory")/(.Header.Form: Rationale)//$atom ((rationale_for)) Atom//$atom_2
```

