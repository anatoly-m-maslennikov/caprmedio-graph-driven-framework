---
atom_id: CA-R-2729
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
version: 7
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2729-WORKBENCH-RULE--return-complete-consistent-results-for-query-run-and-check.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
updated_at: 2026-11-05 13:04:02 +0400
---
## Summary

Return complete, consistent results for query Run and Check

## Claim scope

The public Run and Check operations for a query over the query Projection.

## Claim

### Prose Claim

The query interface **must**:

- provide synchronous MCP Run and Check operations.
- select the statement at the supplied optional UTF-16 cursor_position using native SQL tokenization. Return the selected SQL exactly as submitted, including comments, Unicode and any existing LIMIT.
- let Run accept optional non-negative integer preview and boolean save parameters. The default for save is false; an optional name is valid only when save is true.
- make Run materialize the selected query result once and return its first bounded page, query ID, column information, selected SQL and exact row and column counts for that execution. A preview caps the result at most at N rows while preserving an existing SQL LIMIT; it does not rewrite the SQL or its text and also works for GRAPH_TABLE queries.
- provide Page to retrieve subsequent portions of the same materialized result without re-executing the query. Pagination is stable, and its rows and counts describe the previewed execution when preview was supplied.
- save the exact selected SQL only after a successful Run when save is true. A successful save adds the saved query identity, URL, kind and optional name to the normal Run response.
- keep a completed Run result and query ID when saving after that Run fails. Return outcome partial and save_error, without a saved identity unless one is actually known; do not retry or roll back the completed result.
- create no saved entry when query execution or statement selection fails. Run with save false, Check and Page do not save SQL or append a Journal record.
- make Check return whether the query is valid and, when valid, the selected SQL and exact row and column counts for its validation execution.
- keep Check free of source and source-Projection modifications; temporary internal result materialization is derived cache work.
- return query errors to the caller through both Run and Check.
- keep the counts and rows of one Run consistent with the same materialized execution.
- expose pagination explicitly without adding a hidden SQL limit or dropping selected rows. Pages remain stable while the materialized result is held.

When preview is omitted, Run applies no added preview cap.
