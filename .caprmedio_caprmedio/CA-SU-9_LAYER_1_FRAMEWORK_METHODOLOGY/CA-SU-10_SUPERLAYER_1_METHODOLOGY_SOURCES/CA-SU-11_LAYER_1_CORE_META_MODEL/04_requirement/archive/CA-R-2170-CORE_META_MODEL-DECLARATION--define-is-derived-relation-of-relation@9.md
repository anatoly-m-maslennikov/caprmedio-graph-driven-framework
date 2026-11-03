---
atom_id: CA-R-2170
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO_MODEL <+ CFEL <+ Relation//IS_DERIVED_RELATION_OF
  passive:
  - CAPRMEDIO_MODEL <+ CFEL > Relation
version: 9
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 1
role: Requirement
form: Declaration
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
