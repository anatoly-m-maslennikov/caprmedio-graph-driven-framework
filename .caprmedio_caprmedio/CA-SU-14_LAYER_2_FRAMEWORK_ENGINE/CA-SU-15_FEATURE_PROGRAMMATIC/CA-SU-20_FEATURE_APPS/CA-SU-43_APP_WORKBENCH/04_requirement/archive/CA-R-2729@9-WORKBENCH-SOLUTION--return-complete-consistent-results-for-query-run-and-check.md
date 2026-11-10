---
identity:
  atom_id: CA-R-2729
  ref_id: CA-R-2729@9
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
  version: 9
  updated_at: 2026-11-10 00:46:37 +0400
destination:
  file:
    name: CA-R-2729@9-WORKBENCH-SOLUTION--return-complete-consistent-results-for-query-run-and-check.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
---

## Summary

Return complete, consistent results for query Run and Check

## Claim scope

The public Run and Check operations for a query over the query Projection.

## Claim

### Prose Claim

The query interface must:

- provide synchronous Run, Check and result fetch through the shared backend, MCP and web interfaces;
- validate one complete submitted query. A cursor position is editor metadata only. Keep submitted SQL unchanged for execution, Bookmarks and the Run log;
- let Run accept optional non-negative preview and optional save, default false. An optional Bookmark name is valid only when save is true;
- materialize a Run once and return its query ID, ordered column metadata, exact row and column counts, and either a result-file descriptor or explicitly requested inline page;
- use result files by default. JSON matrix is the default format; CSV and TOON are alternatives. Do not put result rows or the full SQL into an ordinary MCP Run or file-fetch answer;
- write actual results under the selected Project's `.caprmedio_tmp/workbench/query_results` and return the file path, format, exported row count, column count, offset and remaining-page information. Return a path only after that file is complete;
- let a direct Run export its complete materialized result, or the preview-capped result when preview is supplied. Fetch and Page export only the requested bounded page. Neither export nor pagination executes SQL again;
- preserve an existing SQL LIMIT when preview caps at most N rows, without rewriting SQL. Apply this equally to CTE and GRAPH_TABLE queries;
- let Page and View Fetch read the same stable materialized result. The browser may explicitly request inline pages for its grid; this does not change the stored data or create another query executor;
- make Check return validity, exact counts when available, and query errors. Check returns query-request metadata only: no result rows, result file, SQL echo, Bookmark or query-log entry;
- omit automatic full-SQL echoes from Run, Check, Page, View Run, View Check and View Fetch. Explicit Load, View-query reads and query-log reads may return SQL because the caller requested it;
- save the exact original SQL as a Bookmark only after a successful Run when save is true. Return the saved identity, full URL, kind and optional name only when that save succeeds;
- keep the completed query ID and result available if a later Bookmark save or result export fails. Report the failed part without a fabricated saved ID or successful file path, retry or rollback;
- create no Bookmark on validation or query failure. Run without save, Check and Page create no permanent saved-item Journal entry;
- preserve ordered columns, duplicate column names, SQL nulls, empty strings, Unicode, source newlines and Formal Claim text through export and readback. Use the shared result-value encoding consistently in every format;
- keep View Run metadata-only unless a result fetch is explicitly requested. An AI Agent can run and focus a View without fetching its rows.

Query-log metadata, Bookmarks, saved Views, temporary result files and materialized result tables have separate purposes. A result file is not a Bookmark, log entry or source Atom.
