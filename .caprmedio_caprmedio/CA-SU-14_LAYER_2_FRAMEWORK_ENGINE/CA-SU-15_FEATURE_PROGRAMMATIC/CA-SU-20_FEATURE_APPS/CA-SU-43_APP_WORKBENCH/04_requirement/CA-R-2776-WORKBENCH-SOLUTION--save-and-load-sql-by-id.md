---
identity:
  atom_id: CA-R-2776
  ref_id: CA-R-2776
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: Active
  version: 9
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2776-WORKBENCH-SOLUTION--save-and-load-sql-by-id.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---
## Summary

Save and load SQL by ID

## Claim scope

Workbench SQL Bookmark operations and Bookmark references in the web URL.

## Claim


### Prose Claim
The Workbench writes a permanent Bookmark only after successful `query_run(save: true)`: exact SQL, optional creation name, `saved_at`, `kind: query`, and a stable saved ID and URL. Bookmark names are immutable. A failed Run writes nothing; a post-Run save failure retains the completed result and its ID, returns partial/save_error, produces no invented saved identity, and never retries or rolls back. `query_run` is the sole query-save operation and the UI action is Run & Save; no second query-save operation is introduced.

`view_save({sql, name?})` writes one complete Tab script as `kind: view` (a retained storage compatibility value). Saved Views and permanent Bookmarks are distinct from temporary query history, never rename and have no expiry. `query_load({reference})` loads exact SQL by ID or URL without execution. `query_saved_list({limit?})` lists recent query/View entries (20 default, 1,000 maximum) as metadata only: saved identity/URL, kind, optional name, preview and saved time, never full SQL. Existing worksheet entries and q_/w_ runtime files remain read-only compatibility, with IDs/URLs unchanged and no migration.

`?query=<saved_query_id>` loads either saved kind into the current Project context without a Run. Saved identities differ from materialized result IDs. Exclude sharing, authorization, deduplication, retry, repair, rollback and deletion. Call permanent saved SQL a Bookmark and retain its distinction from a saved View.
