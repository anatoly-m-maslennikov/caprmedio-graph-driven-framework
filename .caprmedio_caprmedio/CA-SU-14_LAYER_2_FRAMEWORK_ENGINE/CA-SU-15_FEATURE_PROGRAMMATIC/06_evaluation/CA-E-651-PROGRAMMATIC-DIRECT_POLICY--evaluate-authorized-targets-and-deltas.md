---
identity:
  atom_id: CA-E-651
  ref_id: CA-E-651
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control <+ Effect Authorization
  tier: 2
relations:
  evaluation_for:
  - CA-M-404
state:
  status: Active
  version: 16
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-E-651-PROGRAMMATIC-DIRECT_POLICY--evaluate-authorized-targets-and-deltas.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
current_scope_unit: PROGRAMMATIC
claim_target_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---
## Summary

Evaluate authorized targets and deltas

## Claim

### Prose Claim

Observed effects must match authorized target, delta and expected state, not adapter success. Wrong Project/target, extra delta, substitution, stale, ambiguous and unsupported cases have no unauthorized effect. Independently retain verified concurrent/bulk members; no replay, invented rollback, approval or retry.
