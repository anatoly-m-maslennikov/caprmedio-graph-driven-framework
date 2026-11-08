---
identity:
  atom_id: CA-D-703
  ref_id: CA-D-703@2-draft
context:
  container:
    scope_unit: CA-SU-45
  role: Delivery
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  delivery_for:
  - CA-R-2998
state:
  status: Draft
  version: 2
  updated_at: 2026-11-08 20:40:58 +0400
destination:
  file:
    name: CA-D-703@2-draft-WORKBENCH_BACKEND-SOLUTION--deliver-workbench-profile-artifacts-under-project-temporary-storage.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/07_delivery/draft/engine-refinement-20261108
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Deliver Workbench profiles under project temporary storage

## Claim

### Prose Claim

Provide an explicit development CLI with the selected Project root and an optional output directory constrained beneath that Project’s configured temporary root. Write cpu.pstats and report.json there. The report includes runtime/build context, dataset and rebuild-cycle counts, instrumented timings, Python current/peak allocation bytes and top allocation traces, process high-water RSS with byte units, and DuckDB-managed memory. State unavailable measurements explicitly; do not present cumulative RSS as current live memory. Keep disposable databases separate from source files and the live runtime database, and attempt bounded cleanup on completion or failure. If cleanup is interrupted or denied, report the retained path under the Project temporary root; do not retry or modify source files.
