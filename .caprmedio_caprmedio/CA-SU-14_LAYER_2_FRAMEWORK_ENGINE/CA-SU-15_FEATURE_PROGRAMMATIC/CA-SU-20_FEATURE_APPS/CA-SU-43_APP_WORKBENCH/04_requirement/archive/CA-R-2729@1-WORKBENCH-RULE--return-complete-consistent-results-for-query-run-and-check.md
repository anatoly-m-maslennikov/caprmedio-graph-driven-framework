---
atom_id: CA-R-2729
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
version: 1
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations: {}
carrier_destination:
  file:
    name: CA-R-2729@1-WORKBENCH-RULE--return-complete-consistent-results-for-query-run-and-check.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
updated_at: 2026-11-03 23:17:14 +0400
---
## Summary

Return complete, consistent results for query Run and Check

## Claim scope

The public Run and Check operations for a query over the query Projection.

## Claim

### Prose Claim

The query interface **must**:

- provide an MCP query tool with synchronous Run and Check operations.

- make Run return the complete query result, column names and types, row count, and column count.
- make Check return whether the query is valid and, when valid, its exact row count and column count; exact counts come from executing the read-only query.
- make the counts and rows of one Run describe the same query execution.
- return query errors to the caller through both Run and Check.
- neither silently add a LIMIT nor truncate rows. If a transport cannot carry the complete result, it **must** report that limit explicitly.
- keep Check free of source and Projection modifications.

