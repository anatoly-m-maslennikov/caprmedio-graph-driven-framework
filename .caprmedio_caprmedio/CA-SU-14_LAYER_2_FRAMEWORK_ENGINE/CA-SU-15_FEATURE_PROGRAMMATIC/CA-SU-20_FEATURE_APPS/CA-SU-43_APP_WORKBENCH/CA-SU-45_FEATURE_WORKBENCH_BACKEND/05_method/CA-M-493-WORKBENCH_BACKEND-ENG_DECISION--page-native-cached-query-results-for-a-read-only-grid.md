---
atom_id: CA-M-493
ref_id: CA-M-493
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
status: Active
version: 1
author: Anatoly Maslennikov
role: Method
form: Eng Decision
tier: 4
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
relations:
  method_for:
  - CA-R-2729
  - CA-M-462
carrier_destination:
  file:
    name: CA-M-493-WORKBENCH_BACKEND-ENG_DECISION--page-native-cached-query-results-for-a-read-only-grid.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/05_method
updated_at: 2026-11-05 20:32:03 +0400
container:
  scope_unit: CA-SU-45
---

## Summary

Page native cached query results for a read-only grid

## Claim

### Prose Claim

Apply an optional grid view only to the current native materialized result identified by `query_page` or by a View's current result in `view_fetch`. The grid is a read-only presentation transform for the first Tabulator pass: it never reruns user SQL, parses or rewrites submitted SQL, writes a second result cache, or changes the original result metadata.

At initial materialization, generate a query-specific quoted private alias and create the same result CTAS as `SELECT row_number() OVER () AS <private_ordinal>, * FROM (<relation.sql_query()>) AS source`. Apply a requested preview relation limit before `sql_query()` and number that limited snapshot. The private ordinal is physical stored position zero; every original public column is stored at its public zero-based index plus one. Retain the ordinary public metadata independently and exclude stored position zero from public metadata, `has_values`, `column_count`, positional rows, filters, sorts and grouping. This adds no second cache, `ALTER`, `UPDATE` or rescan.

The page query forms one internal `result_view` over that cache and resolves every public zero-based column index to its private physical position. It never uses user-supplied column names or DuckDB `rowid`; duplicate output names, dotted aliases and an output column named `rowid` therefore remain unambiguous. The private ordinal is not a public column and is the final ordering tie-breaker for every page, giving a stable cache snapshot across offsets. It freezes the execution order supplied by the accepted query; it does not invent an SQL ordering where the query supplied none.

The accepted grid transform has zero or more filters combined with AND, zero or more sort entries, and at most one `group_by` column. A filter is exactly case-insensitive `contains` over the string rendering of its resolved cached value. Bind the filter value as a DuckDB parameter and use literal containment semantics, such as `instr(lower(CAST(value AS VARCHAR)), lower(?)) > 0`; `%`, `_`, quotes and other input have no wildcard or SQL meaning. Apply every ordering and grouping operation natively in DuckDB. Each user-directed sort and the one optional group order uses `ASC` or `DESC` with `NULLS LAST`; grouping order precedes requested sorting and the private snapshot ordinal resolves all remaining ties. Do not add nested grouping or sort-by-group-count in this pass.

When grouping is requested, compute each group count with a native window `COUNT(*) OVER (PARTITION BY resolved_group_column)` before offset and limit. Return group records only for group values represented in the delivered page, but each record's count is global to the complete filtered result. Filtering, sorting, grouping and paging are derived reads from the single cache, not stored result state.

Validate a grid shape, all indices, directions, filter operators and values before reading or releasing a result. A rejected grid request returns its input error and leaves the cached result available and unchanged.
