---
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//DERIVED_FROM
  passive:
  - CAPRMEDIO <+ MODEL <+ Term//Artifact
version: 37
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
atom_id: CA-R-1639
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-1639-CORE_META_MODEL-DECLARATION--register-derived-from-relation.md
  source_atom_id: CA-R-1639
  source_atom_revision: 37
  source_sha256: 9c360dae88d04a87ff041eaf9d46fff18f34f5203c704a8f1135b73e74a132cd
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Register derived_from relation

## Claim scope

direct derivation relations between exact represented content versions.

## Claim

DERIVED_FROM means the directed Relation from a derived represented content version to an exact source content version used to derive it. Version references identify the relevant states; this does not introduce a Revision entity.

```CFEL
((DERIVED_FROM)) >| Derivation == Direct;

$derived_content_version ((DERIVED_FROM)) $source_content_version
```

## Semantics



The Host is a derived represented-content version and the Target is the exact source content version used to derive it.
Forward `Host ((DERIVED_FROM)) Target` and reverse `Target <((DERIVED_FROM)) Host` are views of the same Relation fact.
DERIVED_FROM relates derived represented content version to exact source content version.

