---
atom_id: CA-R-2623
role: Requirement
form: Declaration
status: Active
version: 3
updated_at: 2026-11-02 17:54:42 +0400
current_scope_unit: CORE_META_MODEL
tier: 3
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_RUN_BY
relations: {}
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2623-CORE_META_MODEL-DECLARATION--declare-is-run-by.md
  source_atom_id: CA-R-2623
  source_atom_revision: 3
  source_sha256: 60ecb82eb46e05d097853a3eb301c4a4276da87c15b019512a5d34a881626861
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Declare IS_RUN_BY

## Claim

```CFEL
Action// ((IS_RUN_BY)) (in (Step, Substep))//;
Workflow// ((IS_RUN_BY)) Step//;
((IS_RUN_BY)) >| Derivation == Derived;
((IS_RUN_BY)) ((IS_DERIVED_RELATION_OF)) ((RUNS))
```

## Semantics

IS_RUN_BY is the derived inverse view of RUNS and is not authored as a separate fact.
