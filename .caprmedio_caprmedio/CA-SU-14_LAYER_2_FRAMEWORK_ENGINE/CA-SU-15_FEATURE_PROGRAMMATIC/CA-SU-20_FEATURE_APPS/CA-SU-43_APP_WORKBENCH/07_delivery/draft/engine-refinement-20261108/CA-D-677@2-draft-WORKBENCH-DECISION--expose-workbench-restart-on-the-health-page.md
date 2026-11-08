---
identity:
  atom_id: CA-D-677
  ref_id: CA-D-677@2-draft
context:
  container:
    scope_unit: CA-SU-43
  role: Delivery
  form: Decision
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 5
relations:
  delivery_for:
  - CA-R-2782
  depends_on:
  - CA-D-676
state:
  status: Draft
  version: 2
  updated_at: 2026-11-08 20:10:59 +0400
destination:
  file:
    name: CA-D-677@2-draft-WORKBENCH-DECISION--expose-workbench-restart-on-the-health-page.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/draft/engine-refinement-20261108
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Expose Workbench restart on the health page

## Claim

Show a Restart Workbench button on the HTML health page at `/caprmedio/health`. Use a native HTML POST form to `/caprmedio/health/workbench-restart`. On the Project server, its body is empty. On a shared host, require one `project_root` value, labelled Project folder. Reject unknown or repeated fields before any effect.

Route the action through the same gateway `workbench_restart` operation exposed by MCP, with the same Project selection, blacklist and public error boundary. Do not reimplement lifecycle control in the page. Show the ready or failure outcome as escaped text in the health view. Do not automatically repeat or restart another service.

GET health requests stay read-only. Preserve existing JSON readiness and HTML snapshot behavior. Keep the health page available when Workbench fails. The explicit action requires no separate approval form. It adds no generic service picker, shell commands, container control, JavaScript dependency or Workbench query-editor button.
