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

