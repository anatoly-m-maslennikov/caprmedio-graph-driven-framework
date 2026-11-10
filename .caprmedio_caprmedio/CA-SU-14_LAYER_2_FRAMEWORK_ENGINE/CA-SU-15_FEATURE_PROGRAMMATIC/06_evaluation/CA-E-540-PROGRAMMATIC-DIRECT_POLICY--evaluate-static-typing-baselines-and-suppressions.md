---
identity:
  atom_id: CA-E-540
  ref_id: CA-E-540
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Quality
      <+ Verification <+ Static Analysis
    dependencies: []
  tier: 5
relations:
  evaluation_for:
  - CA-M-420
  - CA-M-427
state:
  status: Active
  version: 16
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-540-PROGRAMMATIC-DIRECT_POLICY--evaluate-static-typing-baselines-and-suppressions.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
## Summary

Evaluate static typing baselines and suppressions

## Claim

### Prose Claim

Within admitted Mypy targets, new code passes strict pinned profile, changed code does not regress passing baseline, and every suppression is narrow and explained. Missing profile/targets/baseline/evidence is unresolved; runtime and behavioral evidence remain distinct.
