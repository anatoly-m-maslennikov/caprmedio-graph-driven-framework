---
atom_id: CA-R-2776
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
version: 2
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2776-WORKBENCH-RULE--save-and-load-sql-by-id.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
updated_at: 2026-11-05 01:40:28 +0400
---

## Summary

Save and load SQL by ID

## Claim scope

Workbench SQL saved-query operations and saved-query references in Run, Check and the web URL.

## Claim

The Workbench **must**:

- write each new saved query or Worksheet as one entry in a dedicated append-only Journal under the configured Project Journal root. Each entry has a canonical unprefixed UUIDv7 ID, `kind` (`query` or `worksheet`), exact `sql`, optional `name` and `saved_at`;
- use the existing Journal writer's 1,000-row parts with the reserved `workbench-saved-items` prefix and date partition. Do not create one unbounded file. Approximate the limit under concurrent writes;
- accept an optional `name` only when `query_save` or `worksheet_save` creates the entry. Run and Check save unnamed. Do not rename saved queries or saved Worksheets after creation;
- expose `query_save({sql, cursor_position?, name?}) -> {saved_query_id, saved_query_url, kind, sql, name?}` and `worksheet_save({sql, name?}) -> {saved_query_id, saved_query_url, kind, sql, name?}`;
- expose `query_load({reference}) -> {saved_query_id, saved_query_url, kind, sql, name?}` and `query_saved_list({limit?})` for recent query and Worksheet entries, with default limit 20 and maximum 1,000. Names are returned when present;
- expose the same contracts through the web `/save`, `/worksheet-save`, `/load` and `/saved-list` endpoints, and expose `query_schema({})` through `/schema` for table and column metadata;
- load a saved query or Worksheet by ID or URL and return its exact SQL without executing it;
- let `?query=<saved_query_id>` load either kind without automatic execution and preserve the `project_root` parameter;
- keep saved-query identities separate from materialized result query IDs and distinguish them with `kind`;
- keep existing `q_<hex>.sql` and `w_<hex>.json` runtime files as read-only fallback sources for load/list. Preserve their IDs and URLs; do not rewrite or migrate them;
- exclude saved-item Journal writes from source watching so saving a query does not trigger Atom reindexing;
- omit sharing, authentication, deduplication, retry, repair, rollback, expiry and deletion workflows.
