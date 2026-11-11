---
atom_id: CA-R-2420
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//IS_EXECUTED_BY
relations: {}
version: 4
updated_at: 2026-11-02 08:06:47 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2420-CORE_META_MODEL-DECLARATION--define-is-executed-by-relation.md
  source_atom_id: CA-R-2420
  source_atom_revision: 4
  source_sha256: b3951c3f33120a64b58d12b9c1a05e6ea49dff52724d5cc57a540e24c5161686
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define IS_EXECUTED_BY Relation

## Claim

IS_EXECUTED_BY is the declared derived inverse of EXECUTES; its full Runtime-to-Workflow Run meaning remains in CA-R-2255. No independently stored reverse fact is introduced.

```CFEL
((EXECUTES)) ((HAS_INVERSE)) ((IS_EXECUTED_BY));

((IS_EXECUTED_BY)) >| Derivation == Derived;
((IS_EXECUTED_BY)) ((IS_DERIVED_RELATION_OF)) ((EXECUTES));

$workflow_run ((IS_EXECUTED_BY)) $runtime
```

## Semantics



The Host is a Workflow Run and the Target is the actual Runtime that executes it.
Forward `Host ((IS_EXECUTED_BY)) Target` and reverse `Target <((IS_EXECUTED_BY)) Host` are views of the same Relation fact.
IS_EXECUTED_BY relates Workflow Run to Runtime. It is the derived inverse of EXECUTES; it does not add a separately authored fact.

