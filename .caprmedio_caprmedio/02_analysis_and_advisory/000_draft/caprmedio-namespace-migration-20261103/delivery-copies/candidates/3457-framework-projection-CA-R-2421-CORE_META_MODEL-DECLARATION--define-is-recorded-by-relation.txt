---
atom_id: CA-R-2421
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_RECORDED_BY
relations: {}
version: 4
updated_at: 2026-11-02 08:06:47 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2421-CORE_META_MODEL-DECLARATION--define-is-recorded-by-relation.md
  source_atom_id: CA-R-2421
  source_atom_revision: 4
  source_sha256: 8b9b488ca25a246a6217dd6d67b36cec8aafcde2a038254bf1a922e748e0bd66
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define IS_RECORDED_BY Relation

## Claim

IS_RECORDED_BY is the declared derived inverse of RECORDS; its full Event Record meaning remains in CA-R-2246. No independently stored reverse fact is introduced.

```CFEL
((RECORDS)) ((HAS_INVERSE)) ((IS_RECORDED_BY));

((IS_RECORDED_BY)) >| Derivation == Derived;
((IS_RECORDED_BY)) ((IS_DERIVED_RELATION_OF)) ((RECORDS));

$occurrence ((IS_RECORDED_BY)) Event Record//
```

## Semantics



The Host is the actual Event or execution described by the Target Event Record.
Forward `Host ((IS_RECORDED_BY)) Target` and reverse `Target <((IS_RECORDED_BY)) Host` are views of the same Relation fact.
IS_RECORDED_BY relates actual Event or execution to Event Record. It is the derived inverse of RECORDS; it does not add a separately authored fact.

