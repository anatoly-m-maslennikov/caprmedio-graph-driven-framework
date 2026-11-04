---
atom_id: CA-E-673
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
author: Anatoly Maslennikov
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
version: 1
role: Evaluation
form: Eval Case
tier: 5
carrier_destination:
  file:
    name: CA-E-673@1-WORKBENCH-EVAL_CASE--align-mcp-run-check-and-web-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/06_evaluation/archive
relations:
  evaluation_for:
  - CA-R-2729
  - CA-R-2727
  - CA-D-673
  - CA-D-674
updated_at: 2026-11-03 23:17:14 +0400
---
## Summary

Align MCP Run, Check, and simple web query results

## Claim scope

The MCP query tool and simple local web page that expose the shared SQL
connector.

## Claim

### Prose Claim

The interface passes when MCP Run, MCP Check, and the web page directly use
the same SQL connector in their originating requests. Each execution's data
and counts describe the same committed query state; separate executions may
see different committed states. The public API remains exact SQL plus Run or
Check. MCP Run returns complete rows, column names and types, row count, and
column count before its request completes. MCP Check executes the read-only
query and reports its validity and exact counts, or its query error, without
changing source or Projection state. The web page exposes SQL input, Check and
Run results, row and column counts, ordinary result rows, and query errors
through that connector without another evaluator. If MCP transport cannot
carry the complete result, it returns an explicit full-result delivery failure
instead of claiming a complete result. Query errors remain distinct from
background indexer source errors.

## Details

### Fixtures and expected outcomes

| Fixture | Expected outcome |
| --- | --- |
| Valid multi-row, multi-column query against one committed Projection state | MCP and web directly invoke the same SQL connector in their originating requests. MCP Run returns complete rows, names, types, and counts before its request completes. The web Run shows ordinary result rows and row/column counts from the same connector, but need not display every returned row. MCP Check and the web Check report the exact row and column counts. |
| Direct request integration | Each MCP and web request supplies only SQL and Run or Check to the same direct query process; it returns its result or query error before that request completes. No query job, ticket, queue, planner, scheduler, orchestrator, Workflow, or Step chain is required. |
| Valid query with zero rows | Run and Check report a successful empty result with exact zero row count, not an error or fabricated row. |
| Invalid SQL submitted through MCP and the web page | Both surfaces report the query error; neither reports an empty successful result or changes the Projection. |
| MCP result larger than its caller context can carry | MCP returns an explicit full-result delivery failure; silent truncation, an unreported limit, or a claimed complete result fail. |
| A background source-file error alongside a valid SQL query | The indexer skips the failed source, reports its error on stderr without retry, and does not insert it as a fake result row; the direct query result remains ordinary SQL data. |
| Direct request and background-index technical activity | Direct query results return to MCP or web before each request completes. The background indexer writes counts to technical stdout and errors to stderr; neither process writes a business Journal entry. |
