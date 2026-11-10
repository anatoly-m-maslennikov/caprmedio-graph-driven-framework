---
identity:
  atom_id: CA-M-472
  ref_id: CA-M-472@3
context:
  container:
    scope_unit: CA-SU-43
  role: Method
  form: Decision
  topics:
    main_subject: CAPRMEDIO_STRUCTURE <+ Aspects <+ Engineering <+ Quality <+ Verification
      <+ Test Design
    dependencies:
    - CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2727
  - CA-R-2728
  - CA-R-2776
  SPECIALIZES:
  - CA-M-424
state:
  status: Archived
  version: 3
  updated_at: 2026-11-09 07:45:15 +0400
destination:
  file:
    name: CA-M-472@3-WORKBENCH-DECISION--test-workbench-through-its-public-interfaces.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Test Workbench through its public interfaces

## Claim

### Prose Claim

Test Workbench through its real browser, MCP and HTTP interfaces.

Use Playwright with Chromium for browser checks against the existing Workbench test container. Reuse that container; do not start a Vite development server or mock the Workbench backend. Keep browser testing dependencies in the frontend's development dependencies. Do not add retries.
