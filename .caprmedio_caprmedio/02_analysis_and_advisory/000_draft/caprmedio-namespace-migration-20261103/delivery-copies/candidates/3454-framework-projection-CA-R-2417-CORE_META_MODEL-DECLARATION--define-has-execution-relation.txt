---
atom_id: CA-R-2417
current_scope_unit: CORE_META_MODEL
status: Active
tier: 1
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//HAS_EXECUTION
relations: {}
version: 4
updated_at: 2026-11-02 08:06:47 +0400
claim_target_scope_unit: CORE_META_MODEL
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2417-CORE_META_MODEL-DECLARATION--define-has-execution-relation.md
  source_atom_id: CA-R-2417
  source_atom_revision: 4
  source_sha256: 6667d5290f94ac3a8935ec5d8c482441428a646621722aff8cb61894df9e912f
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define HAS_EXECUTION Relation

## Claim

HAS_EXECUTION is the declared derived inverse of IS_EXECUTION_OF; its full execution-binding meaning remains in CA-R-2245. No independently stored reverse fact is introduced.

```CFEL
((IS_EXECUTION_OF)) ((HAS_INVERSE)) ((HAS_EXECUTION));

((HAS_EXECUTION)) >| Derivation == Derived;
((HAS_EXECUTION)) ((IS_DERIVED_RELATION_OF)) ((IS_EXECUTION_OF));

Workflow// ((HAS_EXECUTION)) $workflow_run
```

## Semantics



The Host is the reusable Workflow and the Target is its actual Workflow Run.
Forward `Host ((HAS_EXECUTION)) Target` and reverse `Target <((HAS_EXECUTION)) Host` are views of the same Relation fact.
HAS_EXECUTION relates Workflow to Workflow Run. It is the derived inverse of IS_EXECUTION_OF; it does not add a separately authored fact.

