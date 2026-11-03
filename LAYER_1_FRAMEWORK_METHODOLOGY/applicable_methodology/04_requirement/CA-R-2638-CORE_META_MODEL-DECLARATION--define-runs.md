---
atom_id: CA-R-2638
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
status: Active
subjects:
  active: CAPRMEDIO <+ MODEL <+ CFEL <+ Relation//RUNS
version: 2
updated_at: 2026-11-02 17:54:42 +0400
relations: {}
tier: 3
role: Requirement
form: Declaration
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md
  source_atom_id: CA-R-2638
  source_atom_revision: 2
  source_sha256: e49bef756968b7120cd404a9aa153c842bb4cb72bf2ed1fa0dc7247db754eb35
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---

## Summary

Define RUNS

## Claim

```CFEL
Step// ((RUNS)) (in (Action, Workflow))//;
Substep// ((RUNS)) Action//;
((RUNS)) ((HAS_INVERSE)) ((IS_RUN_BY));
((RUNS)) >| Derivation == Direct
```

## Semantics

RUNS binds a Step or Substep invocation to its execution target. Its inverse is IS_RUN_BY.
