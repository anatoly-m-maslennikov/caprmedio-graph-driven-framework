---
atom_id: CA-D-673
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Archived
version: 6
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2724
  - CA-R-2728
  - CA-R-2729
carrier_destination:
  file:
    name: CA-D-673@6-WORKBENCH-ENG_DECISION--deliver-shared-query-run-and-check-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery/archive
updated_at: 2026-11-04 16:59:55 +0400
---

## Summary

Deliver shared query Run and Check results

## Claim scope

The synchronous SQL, MCP and web Run, Page and Check interfaces.

## Claim

### Prose Claim

Use one shared synchronous native DuckDB and DuckPGQ connector. Serve MCP through `/caprmedio/mcp`. Public tools are `query_run`, `query_page` and `query_check`; the web uses the same capability. No queue, job, planner or second executor is required.

Run accepts `sql` and optional `page_size` (default 100, maximum 1,000). It returns `query_id`, ordered `columns` (name and native type), positional `rows`, exact total `row_count` and `column_count`, `offset`, `page_size` and `has_more`. Page accepts `query_id`, a non-negative integer `offset` and optional `page_size`, and returns the same result shape. Page reads the stable materialized result; it does not rerun SQL. Check accepts `sql` and returns validity and exact counts, or its query error, without sending all rows.

Preserve duplicate column names positionally. Encode ordinary JSON values losslessly; encode integers outside JavaScript's safe range and Decimal values as strings, dates/times as ISO strings and binary values as `base64:` strings. Apply conversion recursively to lists and string-keyed mappings. Non-finite numbers, non-string mapping keys and unsupported values produce a delivery error. Counts remain integers. Do not add row hashes to arbitrary SQL results.

Keep source-file errors on stderr with their source path. Return known query and page errors to their originating caller. Source files and source-derived facts remain unchanged by public queries; internal result tables are disposable cache, not a third public source table.
