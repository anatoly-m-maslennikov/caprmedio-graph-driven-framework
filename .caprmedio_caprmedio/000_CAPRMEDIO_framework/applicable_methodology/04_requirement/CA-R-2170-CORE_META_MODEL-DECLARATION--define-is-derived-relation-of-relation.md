---
atom_id: CA-R-2170
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation//IS_DERIVED_RELATION_OF
  passive:
  - CFEL > Relation
version: 9
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2170-CORE_META_MODEL-DECLARATION--define-is-derived-relation-of-relation.md
  source_atom_id: CA-R-2170
  source_atom_revision: 9
  source_sha256: 9a4f162c5e4b92775d7ffba93d35ab2d216c1196ccb1cb38b0a29a092f355149
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define is derived relation of relation

## Claim scope

Type-level derivation between Relation Type instances.

## Claim

`IS_DERIVED_RELATION_OF` **means** a direct relation from one derived Relation
Type instance to one source Relation Type instance from which its relation
meaning is derived.

```CFEL
Relation// ((IS_DERIVED_RELATION_OF)) Relation//;

((IS_DERIVED_RELATION_OF)) >| Derivation == Direct
```

## Semantics


Forward `Host ((IS_DERIVED_RELATION_OF)) Target` and reverse `Target <((IS_DERIVED_RELATION_OF)) Host` are views of the same Relation fact.
IS_DERIVED_RELATION_OF relates derived Relation Type instance to source Relation Type instance.

## Details

This relation does not itself define an endpoint transformation, source-storage
direction, mandatory evidence, provenance, or inference behavior. A
pair-specific definition states any such meaning. `IS_DERIVED_RELATION_OF` is
not `DERIVED_FROM`, which links a derived Artifact Revision to an exact source
Artifact Revision.
