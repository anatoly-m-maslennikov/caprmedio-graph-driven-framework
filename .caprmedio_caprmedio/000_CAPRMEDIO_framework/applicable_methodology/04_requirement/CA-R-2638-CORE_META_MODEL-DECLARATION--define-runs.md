---
atom_id: CA-R-2638
ref_id: CA-R-2638
container:
  scope_unit: CA-SU-11
role: Requirement
form: Declaration
topics:
  main_subject: CAPRMEDIO_MODEL <+ CFEL <+ Relation//RUNS
tier: 3
status: Active
version: 3
updated_at: 2026-11-03 20:00:05 +0400
carrier_destination:
  file:
    name: CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md
    path: .caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
projection:
  source_carrier_path: ../../../.caprmedio_caprmedio/CA-SU-9_LAYER_1_FRAMEWORK_METHODOLOGY/CA-SU-10_SUPERLAYER_1_METHODOLOGY_SOURCES/CA-SU-11_LAYER_1_CORE_META_MODEL/04_requirement/CA-R-2638-CORE_META_MODEL-DECLARATION--define-runs.md
  source_atom_id: CA-R-2638
  source_atom_revision: 3
  source_sha256: 4e4d95996eea1d4c24dbefdbb3fa88e9b4820833a491e204a62d01dc046b0082
  original_relations_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
---
## Summary

Define RUNS

## Claim

### Prose Claim

RUNS binds a Step or Substep invocation to its execution target. Its inverse is IS_RUN_BY.
### Formal Claim

```CFEL
# model
Relation//RUNS ((HAS_INVERSE)) Relation//IS_RUN_BY;

Relation//RUNS ((HAS_CLASSIFICATION)) Derivation == Direct;

# instances
Step//$step ((RUNS)) (in (Action, Workflow))//$selected;

Substep//$substep ((RUNS)) Action//$action;
```

