---
identity:
  atom_id: CA-R-3131
  ref_id: CA-R-3131
context:
  role: requirement
  form: requirement
  tier: 3
  container:
    scope_unit: CA-SU-50
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Scope Unit//FORMAL_MODEL_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-13T10:43:02.276377+00:00'
destination:
  file:
    name: CA-R-3131-FORMAL_MODEL_ENGINE-REQUIREMENT--stop-on-formal-claim-errors.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-51_FEATURE_MODEL/CA-SU-50_FEATURE_FORMAL_MODEL_ENGINE/04_requirement
---
## Summary

Stop on Formal Claim errors

## Claim

### Prose Claim

When a Formal Claim fails, write the error to stderr and stop the affected build or runtime operation. Do not retry or repair the Claim.
