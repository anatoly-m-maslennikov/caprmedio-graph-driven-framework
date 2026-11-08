---
identity:
  atom_id: CA-M-470
  ref_id: CA-M-470@9-draft
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
  - CA-R-2729
  - CA-R-2776
state:
  status: Draft
  version: 9
  updated_at: 2026-11-08 20:10:59 +0400
destination:
  file:
    name: CA-M-470@9-draft-WORKBENCH-DECISION--save-sql-and-browser-state.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/05_method/draft/engine-refinement-20261108
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Save SQL and browser state for Workbench

## Claim scope

Open SQL Views, browser drafts and saved-item Journal records.

## Claim

Save every open View's query text, current local View name and tab state in browser local storage every 5 seconds and restore it on the next page load. Ask before closing an unsaved tab or window; a native beforeunload warning is allowed. Flush the latest draft on pagehide and beforeunload when possible. A View's open lifetime pins its current temporary query result; closing the View unpins it, while a young unpinned result remains subject to the shared backend TTL.

Run and Check do not create permanent saved items or saved-item Journal records. The temporary query log is separate. Query saving is the combined Run & Save operation: it executes the View's exact query successfully first, then writes that SQL and optional creation name to the saved-item Journal. A failed query creates no saved entry. If saving fails after the Run succeeds, keep the completed result, its query ID, the previous saved identity and the dirty state; show the save error and do not retry or roll back. Save View remains the one-query View operation and may persist its optional name. An editor caret may be persisted as metadata, but it never selects an executable statement; editing unfinished SQL is allowed, while Run and Check reject multiple whole queries.

When a View is rerun, drop its previous temporary result before attempting the new query. If the new query fails, the previous result is not restored or returned.

Load through query_load without execution, including when the reference is a URL. Keep browser drafts separate from the Project-level saved-item Journal. Keep saved links in the current Workbench browser context; do not add cross-browser discovery or cross-app synchronization. Saved-item Journal writes use the existing date-partitioned workbench-saved-items writer and do not trigger Atom reindexing, though their observed filesystem changes may appear in the technical change log. Do not add sharing, authentication, saved-Journal deduplication, retry, repair or rollback. Permanent saved items have no expiry.

Use Python 3.14 standard-library uuid.uuid7() for new saved-entry IDs. Do not add a UUID library. Store saved_query_id, kind, exact sql, optional name and saved_at in each Journal row. New View entries use kind view. Existing saved entries with kind worksheet and existing runtime q_/w_ files remain read-only compatibility sources.

Persist the selected Compact or Comfortable density with the existing Theme, text Zoom and workspace settings. Compact is the default for an explicitly embedded Workbench; Comfortable is the default standalone. Saved explicit preferences win. Keep Text zoom, Interface zoom and Density independent; do not infer embedding from physical screen size or Workspace presence.

Keep the saved-entry identity with the existing standalone browser View draft so a reload can recognize that already-open saved item. Reuse its open View by exact saved ID, preferring the active matching View and then the first matching View in tab order. Keep unsaved edits and results intact when focusing it; equal SQL alone does not identify a saved item. This is reuse of an open View, not deduplication of permanent saved Journal records.

Duplicate through the shared backend View operation after the existing draft-sync path has acknowledged the current editor text. Copy query and cursor only. The new View is independent and has no saved-entry identity or query results. Use the current display name with the first unused `(n)` suffix. Do not rerun, save, share result-table ownership, or add a new queue or retry path.
