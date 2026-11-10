---
identity:
  atom_id: CA-E-797
  ref_id: CA-E-797
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control <+ Code Hot Reload
  tier: 3
state:
  status: Active
  version: 4
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-797-PROGRAMMATIC-DIRECT_POLICY--verify-default-off-code-hot-reload.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  evaluation_for:
  - CA-M-505
---
## Summary

Verify default-off code hot reload

## Claim

### Prose Claim

For each hot-reload mechanism, ordinary startup is disabled without reload-only watcher/process; explicit opt-in enables it and disabling restores normal restart behavior. Verify retained runtime capabilities/source-data synchronization via public launch/configuration behavior.
