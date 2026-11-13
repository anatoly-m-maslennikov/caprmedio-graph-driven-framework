---
identity:
  atom_id: CA-A-1371
  ref_id: CA-A-1371
context:
  role: analysis_and_advisory
  form: code_synopsis
  tier: 4
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Atom
  container:
    scope_unit: FRAMEWORK_ENGINE
state:
  version: 1
  status: active
  updated_at: '2026-11-12T12:58:58.940667+00:00'
destination:
  file:
    name: CA-A-1371-FRAMEWORK_ENGINE-CODE_SYNOPSIS--status-pilot-test-uses-an-outdated-query-reader-fixture.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/02_analysis_and_advisory
---
## Summary

Status pilot test uses an outdated query reader fixture

## Claim

### Prose Claim

CA-E-825@1 requires an acceptance check for the Status pilot. `FEATURE_TOOLS/tests/test_python_status_workflow.py` uses `IndexedReader` from `test_lifecycle_source.py`. That fixture does not implement `lifecycle_contexts`, which the Status path calls to verify the parent. `test_activate_backlog_tree_with_attached_draft` failed with AttributeError. Production Workbench implements the interface.
