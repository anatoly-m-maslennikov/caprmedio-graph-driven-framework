---
atom_id: CA-M-470
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
version: 2
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2727
  - CA-R-2729
  - CA-R-2776
carrier_destination:
  file:
    name: CA-M-470-WORKBENCH-ENG_DECISION--save-sql-and-browser-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method
updated_at: 2026-11-05 01:40:28 +0400
---

## Summary

Save SQL and browser state for Workbench

## Claim scope

Open SQL Worksheets, browser drafts and saved-item Journal records.

## Claim

Save every open Worksheet's whole script, current local Worksheet name and tab state in browser local storage every 5 seconds and restore it on the next page load. Ask before closing an unsaved tab or window; a native `beforeunload` warning is allowed. Flush the latest draft on `pagehide` and `beforeunload` when possible. Save Run and Check SQL through the shared `query_save` contract before execution without a name. Explicit Save may provide an optional query name; Save Worksheet may provide an optional name and persists it in the saved-item Journal. Saved query and Worksheet names are not renamed after creation. Load through `query_load` without execution, including when the reference is a URL. Keep browser drafts separate from the Project-level saved-item Journal. Keep saved links in the current Workbench browser context; do not add cross-browser discovery or cross-app synchronization. Saved-item Journal writes use the existing date-partitioned `workbench-saved-items` writer and are excluded from source watching, so autosave does not trigger Atom reindexing. Do not add sharing, authentication, deduplication, retry, repair, rollback, expiry or deletion workflows.

Use Python 3.14 standard-library `uuid.uuid7()` for new saved-entry IDs. Do not add a UUID library. Store `saved_query_id`, `kind`, exact `sql`, optional `name` and `saved_at` in each Journal row. Existing runtime q_/w_ saved files remain read-only compatibility sources.
