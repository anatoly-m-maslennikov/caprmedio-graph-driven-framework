---
atom_id: CA-R-2485
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation//HAS_INVERSE
version: 4
updated_at: 2026-11-02 08:06:47 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2485-CORE_META_MODEL-DECLARATION--define-has-inverse.md
  source_atom_id: CA-R-2485
  source_atom_revision: 4
  source_sha256: 8c08d760aba624232e0793598e59a8e280826b678aff042011bf00b818b9619e
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define HAS_INVERSE

## Claim

HAS_INVERSE links a direct Relation to its derived inverse. The inverse swaps the direct Relation's Host and Target. Its links are derived from the direct links and are not authored separately.

```CFEL
Relation// ((HAS_INVERSE)) Relation//;

((HAS_INVERSE)) >| Derivation == Direct
```

## Semantics


Forward `Host ((HAS_INVERSE)) Target` and reverse `Target <((HAS_INVERSE)) Host` are views of the same Relation fact.
HAS_INVERSE relates direct Relation to derived inverse Relation.

