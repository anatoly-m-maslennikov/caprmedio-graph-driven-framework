---
identity:
  atom_id: CA-M-472@2
  ref_id: CA-M-472@2
context:
  container:
    scope_unit: CA-SU-43
  role: Method
  form: Decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2727
  - CA-R-2728
  - CA-R-2776
state:
  status: Archived
  version: 2
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-M-472@2-WORKBENCH-DECISION--test-workbench-through-its-public-interfaces.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Test Workbench through its public interfaces

## Claim

Prefer end-to-end tests through the real browser, MCP and HTTP interfaces. Assert user-visible results, not private classes, constructor arguments, call counts or internal call order. Remove unit tests that only repeat those end-to-end checks. Keep focused tests for behavior that the end-to-end tests do not cover.

Use Playwright with Chromium for browser checks against the existing Workbench test container. Reuse that container; do not start a Vite development server or mock the Workbench backend. Keep browser testing dependencies in the frontend's development dependencies. Do not add retries.
