---
identity:
  atom_id: CA-E-823
  ref_id: CA-E-823
context:
  container:
    scope_unit: CA-SU-15
  role: Evaluation
  form: Direct Policy
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Execution Control
  tier: 3
state:
  status: Active
  version: 1
  updated_at: 2026-11-11 05:51:23 +0400
destination:
  file:
    name: CA-E-823-PROGRAMMATIC-DIRECT_POLICY--verify-fixed-runtime-code-and-schemas.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/06_evaluation
current_scope_unit: PROGRAMMATIC
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-E-797
  evaluation_for:
  - CA-M-551
---

## Summary

Verify fixed runtime code and schemas

## Claim

### Prose Claim

Change code or a declaration while a service is running. Verify that its code and compiled contracts stay fixed through normal data refresh and full reread. Start the rebuilt image and verify that it applies the change. Verify that source-data synchronization continues with the current contracts and that an invalid generated artifact produces an explicit error.
