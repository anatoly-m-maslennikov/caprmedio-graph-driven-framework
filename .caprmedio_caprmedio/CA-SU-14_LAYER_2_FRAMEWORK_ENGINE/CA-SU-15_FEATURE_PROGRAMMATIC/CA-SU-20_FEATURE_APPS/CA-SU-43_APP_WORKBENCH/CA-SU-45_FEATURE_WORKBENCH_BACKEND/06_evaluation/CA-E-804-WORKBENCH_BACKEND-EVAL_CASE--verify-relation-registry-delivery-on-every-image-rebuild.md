---
identity:
  ref_id: CA-E-804
  id: CA-E-804
context:
  container:
    scope_unit: CA-SU-45
  role: Evaluation
  form: Eval Case
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Data Handling <+ Schema
    dependencies:
    - MODEL//CAPRMEDIO <+ CFEL <+ Relation
  tier: 7
relations:
  evaluation_for:
  - CA-M-509
state:
  status: active
  version: 5
  updated_at: '2026-11-12T12:29:30.190837+00:00'
destination:
  file:
    name: CA-E-804-WORKBENCH_BACKEND-EVAL_CASE--verify-relation-registry-delivery-on-every-image-rebuild.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/06_evaluation
author: Anatoly Maslennikov
---
## Summary

Verify relation registry delivery on every image rebuild

## Claim

### Prose Claim

Verify the selected relation registry reaches the image unchanged for every supported build entry point, including Local Release.

- In refresh mode, compile the registry before image assembly. A selected Declaration change changes asset and build identity. Identical inputs yield identical bytes. A compilation failure stops the build.
- In existing mode, use the checkout registry unchanged. A missing asset stops the build. Verify this mode with the CAPRMEDIO service stopped and without a predecessor image.

Verify the source IDs, Versions, paths and fingerprints in the delivered metadata. Keep Project authority carriers outside the image context. Verify the installed runtime uses the packaged registry and that a Declaration change takes effect after asset refresh and image rebuild.
