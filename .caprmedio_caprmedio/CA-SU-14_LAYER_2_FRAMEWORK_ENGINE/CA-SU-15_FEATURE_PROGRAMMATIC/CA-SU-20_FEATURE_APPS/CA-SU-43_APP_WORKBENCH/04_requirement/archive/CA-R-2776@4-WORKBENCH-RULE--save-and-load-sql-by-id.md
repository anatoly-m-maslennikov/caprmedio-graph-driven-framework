---
atom_id: CA-R-2776
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 4
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2776@4-WORKBENCH-RULE--save-and-load-sql-by-id.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
updated_at: 2026-11-05 13:04:02 +0400
---
## Summary

Save and load SQL by ID

## Claim scope

Workbench SQL saved-query operations and saved-query references in the web URL.

## Claim

The Workbench **must**:

- write a new saved query only after a successful query_run with save true. The entry contains the exact selected SQL, optional name, saved_at, kind query and a canonical unprefixed UUIDv7 ID.
- accept query_run fields sql, optional cursor_position, optional preview, optional save defaulting to false and optional name only when save is true. A failed query_run never creates a saved query.
- return saved_query_id, saved_query_url, kind and optional name with a successful saved Run. If saving fails after the Run has completed, keep that Run result and query ID, return outcome partial and save_error, and do not retry or roll back.
- keep query_run as the only query-save operation. Do not expose a separate query_save operation or a save-only web endpoint. The UI action for this operation is Run & Save.
- keep Save Worksheet as the existing whole-script worksheet operation. It writes one worksheet entry with kind worksheet, exact whole-script SQL and optional creation name.
- write each saved query or Worksheet as one entry in a dedicated append-only Journal under the configured Project Journal root.
- use the existing Journal writer's 1,000-row parts with the reserved workbench-saved-items prefix and date partition. Approximate the limit under concurrent writes rather than creating one unbounded file.
- do not rename saved queries or saved Worksheets after creation. Names are creation-time values.
- expose query_load({reference}) -> {saved_query_id, saved_query_url, kind, sql, name?} and query_saved_list({limit?}) for recent query and Worksheet entries, with default limit 20 and maximum 1,000. Names are returned when present.
- expose the same query_run, worksheet_save, query_load and query_saved_list contracts through the web. Keep worksheet-save, load and saved-list endpoints; do not add a /save endpoint.
- load a saved query or Worksheet by ID or URL and return its exact SQL without executing it.
- let ?query=<saved_query_id> load either kind without automatic execution and preserve the project_root parameter.
- keep saved-query identities separate from materialized result query IDs and distinguish them with kind.
- keep existing q_<hex>.sql and w_<hex>.json runtime files as read-only fallback sources for load/list. Preserve their IDs and URLs; do not rewrite or migrate them.
- exclude saved-item Journal writes from source watching so saving does not trigger Atom reindexing.
- omit sharing, authentication, deduplication, retry, repair, rollback, expiry and deletion workflows.
