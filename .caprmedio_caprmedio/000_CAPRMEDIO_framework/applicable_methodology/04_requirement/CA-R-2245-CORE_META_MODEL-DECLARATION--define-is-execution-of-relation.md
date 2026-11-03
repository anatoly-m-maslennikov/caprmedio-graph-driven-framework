---
atom_id: CA-R-2245
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CFEL <+ Relation//IS_EXECUTION_OF
  passive:
  - Entity/Object/Occurrent/Execution/Workflow Run
  - 'Entity/Object/Continuant/Governing Objects/Atom/Content Role: Operations/Type: Workflow'
version: 7
relations: {}
tier: 1
updated_at: 2026-11-02 08:06:47 +0400
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2245-CORE_META_MODEL-DECLARATION--define-is-execution-of-relation.md
  source_atom_id: CA-R-2245
  source_atom_revision: 7
  source_sha256: d407b253ea312c8b107025de4fa32d29fab0498ec3bc8727174a6103c6a12ad5
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define IS_EXECUTION_OF Relation

## Claim

IS_EXECUTION_OF connects an actual execution to the reusable definition being
executed. The stored direction is Workflow Run to Workflow. HAS_EXECUTION is
its declared derived inverse, not a second stored fact.

```CFEL
((IS_EXECUTION_OF)) ((HAS_INVERSE)) ((HAS_EXECUTION));

((IS_EXECUTION_OF)) >| Derivation == Direct;

$workflow_run ((IS_EXECUTION_OF)) Workflow//
```

## Semantics



The Host is an actual Workflow Run and the Target is the reusable Workflow executed.
Forward `Host ((IS_EXECUTION_OF)) Target` and reverse `Target <((IS_EXECUTION_OF)) Host` are views of the same Relation fact.
Workflow Run ((IS_EXECUTION_OF)) Workflow

The reusable definition is not the execution itself. Workflow Run's binding to
one Workflow belongs in the Workflow Run Entity Definition, not in every use
of this Relation Type.

## Details

This named Type uses the general `((RELATION_TYPE))` form. It defines the reusable Type and creates no occurrence or actual endpoint tuple.
