---
identity:
  atom_id: CA-M-470
  ref_id: CA-M-470
context:
  container:
    scope_unit: CA-SU-43
  role: Method
  form: Decision
  topics:
    main_subject: PROJECT STRUCTURE//CAPRMEDIO <+ Aspects <+ Engineering <+ Operation
      <+ Storage
    dependencies:
    - MODEL//CAPRMEDIO <+ Projection
  tier: 4
relations:
  method_for:
  - CA-R-2727
  - CA-R-2729
  - CA-R-2776
state:
  status: Active
  version: 12
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-M-470-WORKBENCH-DECISION--save-sql-and-browser-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Save SQL and browser state for Workbench

## Claim scope

Open SQL Tabs, browser drafts and saved-item Journal records.

## Claim

### Prose Claim

Persist each open Tab query, local name and tabs in browser localStorage every five seconds and restore on load; ask before unsaved close, flush on pagehide/beforeunload when possible. Persist density with Theme/text/interface zoom/workspace settings: Compact default only explicit embedded, Comfortable standalone, saved preference wins; do not infer embedding from screen/Workspace.

Neither ordinary Run nor Check creates a permanent saved item. Run & Save executes the exact submitted SQL and then synchronously writes that same SQL and an optional creation name; for a selected Run it saves only the selected SQL, while Save Tab snapshots the full Tab script; failure writes nothing, while a post-Run save failure keeps result/ID/prior saved identity/dirty state, shows an error and neither retries nor rolls back. After Run and requested synchronous Save handling, automatic Run history is submitted asynchronously under CA-M-534; Check is not logged. Save snapshots the full Tab script. Unfinished editing is allowed; Run or Check uses the whole script or explicit statement selection under CA-R-2728.

Browser drafts remain separate from the Project Journal; saved links stay in the current Workbench context. The existing date-partitioned writer avoids Atom reindexing. Use Python 3.14 `uuid.uuid7()` only; historical worksheet/q_/w_ sources remain read-only. Reload reuses an open Tab by exact saved ID—not equal SQL—without losing edits or results. Duplicate after sync copies query and cursor only into an independent unsaved/no-result Tab with the first unused `(n)` suffix. Automatic Run history remains asynchronous and distinct from saved items.
