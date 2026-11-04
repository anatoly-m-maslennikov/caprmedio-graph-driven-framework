---
atom_id: CA-M-470
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
version: 1
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2727
  - CA-R-2729
  - CA-R-2776
carrier_destination:
  file:
    name: CA-M-470@1-WORKBENCH-ENG_DECISION--save-sql-and-browser-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/archive
updated_at: 2026-11-04 23:19:17 +0400
---

## Summary

Save SQL and browser state for Workbench

## Claim scope

Open SQL Worksheets, browser drafts and saved-query files.

## Claim

Save every open Worksheet's whole script and tab state in browser local storage every 5 seconds and restore it on the next page load. Ask before closing an unsaved tab or window; a native `beforeunload` warning is allowed. Flush the latest draft on `pagehide` and `beforeunload` when possible. Save Run and Check SQL through the shared `query_save` contract before execution, and save the whole script through `worksheet_save`. Load through `query_load` without execution, including when the reference is a URL. Keep browser drafts separate from immutable UTF-8 query and Worksheet files. Keep saved links in the current Workbench browser context; do not add cross-browser discovery or cross-app synchronization. Do not add sharing, authentication, deduplication, retry, repair, rollback, expiry or deletion workflows.
