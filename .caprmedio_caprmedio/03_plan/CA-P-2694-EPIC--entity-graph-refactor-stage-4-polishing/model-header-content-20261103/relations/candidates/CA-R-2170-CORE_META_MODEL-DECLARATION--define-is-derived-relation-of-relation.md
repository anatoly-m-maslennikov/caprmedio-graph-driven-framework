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

## Claim

### Formal Claim

```CFEL
Relation// ((IS_DERIVED_RELATION_OF)) Relation//;
Relation//IS_DERIVED_RELATION_OF ((HAS_CLASSIFICATION)) Derivation == Direct
```

### Prose Claim

IS_DERIVED_RELATION_OF relates a derived Relation Type instance to its source Relation Type instance. It does not itself specify the endpoint transformation or any qualification. A direct Declaration's inverse binding entails the bound inverse's IS_DERIVED_RELATION_OF link to the direct Relation. This inferred metadata is not repeated in the minimal derived Declaration. A qualified derivation must retain its explicit qualification; it must not be normalized to an unconditional inverse. This Relation is distinct from DERIVED_FROM between Artifact Revisions.
