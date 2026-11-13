---
identity:
  atom_id: CA-M-1019
  ref_id: CA-M-1019
context:
  role: method
  form: decision
  container:
    scope_unit: CA-SU-45
  tier: 4
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
relations:
  SPECIALIZES:
  - CA-R-2776@10
state:
  version: 1
  status: active
  updated_at: '2026-11-13T16:24:47.409913+00:00'
destination:
  file:
    name: CA-M-1019-WORKBENCH_BACKEND-DECISION--use-one-saved-sql-store-for-load-and-recent.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
---
## Summary

Use one saved SQL store for Load and Recent

## Claim scope

Workbench backend reads of Bookmarks and saved Views.

## Claim

### Prose Claim

Use the saved SQL store in `saved_queries.py` for both Load and Recent. Load resolves the ID or URL and returns the stored SQL verbatim. Recent reads the same store and returns the saved ID, kind, optional name, preview and saved time.