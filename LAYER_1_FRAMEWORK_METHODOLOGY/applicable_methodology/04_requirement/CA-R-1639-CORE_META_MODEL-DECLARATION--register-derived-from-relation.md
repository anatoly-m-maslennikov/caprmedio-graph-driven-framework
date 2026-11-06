---
atom_id: CA-R-1639
ref_id: CA-R-1639
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//DERIVED_FROM
  dependencies:
  - CAPRMEDIO_MODEL <+ Term//Artifact
tier: 1
status: Active
version: 38
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-1639-CORE_META_MODEL-DECLARATION--register-derived-from-relation.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1639-CORE_META_MODEL-DECLARATION--register-derived-from-relation.md
  source_atom_id: CA-R-1639
  source_atom_revision: 38
  source_sha256: 96b8eb251c0c7dca2a97309a3abb90a2403792088803fef0b502a4ac64145ceb
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register derived_from relation

## Claim

### Prose Claim

#### Applicability
direct derivation relations between exact represented content versions.

DERIVED_FROM means the directed Relation from a derived represented content version to an exact source content version used to derive it. Version references identify the relevant states; this does not introduce a Revision entity.

The Host is a derived represented-content version and the Target is the exact source content version used to derive it.
Forward `Host ((DERIVED_FROM)) Target` and reverse `Target <((DERIVED_FROM)) Host` are views of the same Relation fact.
DERIVED_FROM relates derived represented content version to exact source content version.
### Formal Claim

```CFEL
# model
Relation//DERIVED_FROM ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
$derived_content_version ((DERIVED_FROM)) $source_content_version
```

