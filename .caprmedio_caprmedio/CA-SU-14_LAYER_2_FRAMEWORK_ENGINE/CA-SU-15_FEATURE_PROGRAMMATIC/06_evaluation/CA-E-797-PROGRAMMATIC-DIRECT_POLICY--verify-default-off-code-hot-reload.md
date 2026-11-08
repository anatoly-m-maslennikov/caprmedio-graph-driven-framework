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
    main_subject: Subject/CAPRMEDIO/Graph/Node/Aspect/Engineering/Execution Control
  tier: 2
state:
  status: Active
  version: 2
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-E-797-PROGRAMMATIC-DIRECT_POLICY--verify-default-off-code-hot-reload.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
---

## Summary

Verify default-off code hot reload

## Claim

### Prose Claim

For each code hot-reload mechanism, verify that ordinary startup leaves it disabled with no reload-only process/watcher, explicit opt-in enables it, and turning it off restores normal restart behavior. Verify that retained runtime capabilities and source-data synchronization still work in default mode. Test public launch/configuration behavior rather than internal implementation structure.
