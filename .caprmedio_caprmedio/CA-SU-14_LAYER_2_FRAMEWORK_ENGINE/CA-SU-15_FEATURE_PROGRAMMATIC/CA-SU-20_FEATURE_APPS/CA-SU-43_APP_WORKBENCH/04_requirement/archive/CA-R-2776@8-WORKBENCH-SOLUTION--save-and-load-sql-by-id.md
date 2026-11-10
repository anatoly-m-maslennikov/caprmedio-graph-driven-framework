---
identity:
  atom_id: CA-R-2776
  ref_id: CA-R-2776@8
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: CAPRMEDIO_MODEL <+ Projection
  tier: 3
state:
  status: Archived
  version: 8
  updated_at: 2026-11-10 00:46:37 +0400
destination:
  file:
    name: CA-R-2776@8-WORKBENCH-SOLUTION--save-and-load-sql-by-id.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Save and load SQL by ID

## Claim scope

Workbench SQL Bookmark operations and Bookmark references in the web URL.

## Claim

The Workbench **must**:

- write a new Bookmark only after a successful query_run with save true. The entry contains the exact submitted SQL, optional name, saved_at, kind query and a canonical unprefixed UUIDv7 ID.
- accept query_run fields sql, optional cursor_position as editor-caret metadata only, optional preview, optional save defaulting to false and optional name only when save is true. A failed query_run never creates a Bookmark. Editing unfinished SQL is allowed; Run and Check reject multiple whole queries, including semicolon-delimited statements, rather than executing a cursor-selected part.
- return saved_query_id, saved_query_url, kind and optional name with a successful saved Run. If saving fails after the Run has completed, keep that Run result and query ID, return outcome partial and save_error, and do not retry or roll back.
- keep query_run as the only query-save operation. Do not expose a separate query_save operation or a save-only web endpoint. The UI action for this operation is Run & Save.
- expose `view_save({sql, name?})` as the one-query View save operation. It writes one View entry with kind view, exact one-query SQL and optional creation name.
- write each Bookmark or View as one entry in a dedicated append-only Journal under the configured Project Journal root.
- use the existing Journal writer's 1,000-row parts with the reserved workbench-saved-items prefix and date partition. Approximate the limit under concurrent writes rather than creating one unbounded file.
- do not rename Bookmarks or saved Views after creation. Names are creation-time values.
- expose query_load({reference}) -> {saved_query_id, saved_query_url, kind, sql, name?} and query_saved_list({limit?}) for recent query and View entries, with default limit 20 and maximum 1,000. Names are returned when present. Existing saved entries with kind worksheet remain readable as historical entries; new saves use kind view.
- expose the same query_run, view_save, query_load and query_saved_list contracts through the web. Use `/view-save`, `/load` and `/saved-list`; do not add a `/save` endpoint or a new worksheet-save alias.
- load a Bookmark or View by ID or URL and return its exact SQL without executing it. Historical saved entries with kind worksheet and existing `w_<hex>.json` runtime items remain loadable for compatibility.
- let ?query=<saved_query_id> load either kind without automatic execution and preserve the project_root parameter.
- keep Bookmark identities separate from materialized result query IDs and distinguish them with kind.
- keep existing q_<hex>.sql and w_<hex>.json runtime files as read-only fallback sources for load/list. Preserve their IDs and URLs; do not rewrite or migrate them.
- exclude saved-item Journal writes from Atom reindexing; their observed filesystem changes may still appear in the technical change log.
- omit sharing, authentication, deduplication, retry, repair, rollback, expiry and deletion workflows for permanent saved items. Temporary materialized results remain subject to the shared backend's age-or-open-View retention policy.
- when a View is rerun, drop its previous temporary result before attempting the replacement; if the new query fails, do not return or restore the previous result.

Call permanent saved SQL a **Bookmark**. Keep saved Views distinct. Existing public tool names, `saved_query_id`, `saved_query_url`, stored kind values and IDs remain unchanged; this terminology change does not migrate or duplicate saved entries.
