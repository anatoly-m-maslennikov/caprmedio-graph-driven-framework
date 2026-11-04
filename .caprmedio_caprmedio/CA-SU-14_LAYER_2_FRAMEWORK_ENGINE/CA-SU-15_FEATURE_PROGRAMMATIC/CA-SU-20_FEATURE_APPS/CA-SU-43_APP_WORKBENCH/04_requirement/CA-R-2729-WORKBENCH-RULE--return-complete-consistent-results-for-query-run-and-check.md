---
atom_id: CA-R-2729
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
version: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2729-WORKBENCH-RULE--return-complete-consistent-results-for-query-run-and-check.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
updated_at: 2026-11-04 23:19:17 +0400
---
## Summary

Return complete, consistent results for query Run and Check

## Claim scope

The public Run and Check operations for a query over the query Projection.

## Claim

### Prose Claim

The query interface **must**:

- provide synchronous MCP Run and Check operations.
- select the statement at the supplied optional UTF-16 `cursor_position` using native SQL tokenization, save that exact selected SQL as UTF-8 before executing each Run or Check, and return its `saved_query_id`, `saved_query_url` and `kind` separately from the materialized result `query_id`.
- make Run materialize the complete query result once and return its first bounded page, query ID, column information and exact total row and column counts.
- provide Page to retrieve subsequent portions of that same materialized result without re-executing the query.
- keep those pages stable if source files are refreshed after Run.
- make Check return whether the query is valid and, when valid, the result's exact row and column counts.
- make the counts and rows of one Run describe the same query execution.
- return query errors to the caller through both Run and Check.
- include `saved_query_id`, `saved_query_url`, `kind` and the actual selected `sql` in successful and query-error Run and Check answers. Page returns the original saved identity and URL for its result.
- if saving the SQL fails, return an explicit save error, do not execute the query, and do not promise a saved-query ID.
- expose pagination explicitly without adding a hidden SQL limit or dropping selected rows. The complete result remains available through its pages until restart.
- keep Check free of source and source-Projection modifications; temporary internal result materialization is derived cache work.
