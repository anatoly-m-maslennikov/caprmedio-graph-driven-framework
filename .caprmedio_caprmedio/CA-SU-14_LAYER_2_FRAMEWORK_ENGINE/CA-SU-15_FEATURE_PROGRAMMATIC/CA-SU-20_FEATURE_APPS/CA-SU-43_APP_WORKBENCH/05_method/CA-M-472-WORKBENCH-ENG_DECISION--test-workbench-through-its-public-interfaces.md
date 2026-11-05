---
atom_id: CA-M-472
ref_id: CA-M-472
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
version: 1
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2727
  - CA-R-2728
  - CA-R-2776
carrier_destination:
  file:
    name: CA-M-472-WORKBENCH-ENG_DECISION--test-workbench-through-its-public-interfaces.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method
updated_at: 2026-11-05 02:30:51 +0400
container:
  scope_unit: CA-SU-43
---

## Summary

Test Workbench through its public interfaces

## Claim

Prefer end-to-end tests through the real browser, MCP and HTTP interfaces. Assert user-visible results, not private classes, constructor arguments, call counts or internal call order. Remove unit tests that only repeat those end-to-end checks. Keep focused tests for behavior that the end-to-end tests do not cover.

Use Playwright with Chromium for browser checks against the existing Workbench test container. Reuse that container; do not start a Vite development server or mock the Workbench backend. Keep browser testing dependencies in the frontend's development dependencies. Do not add retries.
