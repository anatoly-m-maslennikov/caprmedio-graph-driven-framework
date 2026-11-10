---
identity:
  atom_id: CA-R-2953
  ref_id: CA-R-2953@4
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
  version: 4
  updated_at: 2026-11-10 00:46:37 +0400
destination:
  file:
    name: CA-R-2953@4-WORKBENCH-SOLUTION--query-results-support-read-only-sorting-filtering-and-grouping.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
relations:
  IS_REPLACEMENT_FOR:
  - CA-D-697
  - CA-M-493
---

## Summary

Query results support read-only sorting, filtering and grouping

## Claim

### Prose Claim

The Workbench result grid must:

- sort by one or more columns and apply case-insensitive textual contains filters, combined with AND, across the entire materialized result before pagination;
- group by one selected column in ascending or descending key order, showing exact totals across the complete filtered result even when a group spans pages;
- keep the submitted SQL, its cached values, duplicate column labels and positional values unchanged; grid operations read the existing result without rerunning the submitted query;
- show filtered and original row counts and reuse the existing paging limit;
- provide read-only cell actions Copy value and Show full value, a row action Copy row, and column actions Sort ascending, Sort descending, Group by, Filter and Clear filter;
- copy and inspect full returned values regardless of the visible cell-content limit.

The same result-page filtering, sorting and grouping capability is available through MCP. Nested grouping and sorting groups by their counts remain deferred.

## Details

### Grid request and response

`query_page` and `view_fetch` accept an optional `grid` object in addition to their existing result identity and paging arguments. Omission keeps the existing unfiltered page behavior. A supplied grid contains only these optional members:

```json
{
  "sort": [{"column": 0, "direction": "asc"}],
  "filters": [{"column": 1, "operator": "contains", "value": "draft"}],
  "group_by": {"column": 2, "direction": "asc"}
}
```

`column` is a zero-based integer into the original ordered result metadata. `direction` is exactly lowercase `asc` or `desc`. `sort` is an ordered, multi-column list; `filters` is an AND list whose only operator is exactly lowercase `contains` and whose `value` is a string; and `group_by` is absent or exactly one column/direction object. Unknown fields, non-object/list shapes, non-string filter values, invalid directions or operators, and an out-of-range index are rejected without reading SQL or mutating cache state.

Both operations retain the existing result identity, column count and ordinary paging metadata, without echoing submitted SQL. The following row payload describes explicit inline delivery and the positional rows in a file export. Default file delivery returns a completed descriptor instead of inline rows:

| Field | Meaning |
| --- | --- |
| `rows` | Positional values from the requested offset/page size after all grid filters and orders. |
| `row_count` | Exact count of the filtered result before offset and page limit. |
| `source_row_count` | Exact count of the original materialized result before grid filtering. |
| `columns` | The original ordered result metadata, including duplicate names and `has_values` calculated over the original whole cache, not over a filtered result or page. |
| `groups` | Omitted without `group_by`; otherwise an ordered list of `{value, count}` for distinct group values represented by `rows` on this page. `count` is the complete filtered count for that value, not the page count. |

`has_more` is derived from `row_count`, offset and delivered page size. `groups` has no nested children and has no entries for groups absent from the page. An empty page returns an empty `rows` collection and, when grouping, an empty `groups` collection without changing original metadata.

Expose the same request and response through MCP and the Workbench backend interface. The browser may use the response in a read-only Tabulator grid; cell copy/full value, row copy, column sort/group/filter/clear controls are frontend behavior and do not authorize mutation. Do not add a second grid endpoint, persisted grid state, raw SQL grid clause, result re-execution or a new service.

### Grid operations

Apply an optional grid view only to the current native materialized result identified by `query_page` or by a View's current result in `view_fetch`. The grid is a read-only presentation transform for the first Tabulator pass: it never reruns user SQL, parses or rewrites submitted SQL, writes a second result cache, or changes the original result metadata.

At initial materialization, generate a query-specific quoted private alias and create the same result CTAS as `SELECT row_number() OVER () AS <private_ordinal>, * FROM (<relation.sql_query()>) AS source`. Apply a requested preview relation limit before `sql_query()` and number that limited snapshot. The private ordinal is physical stored position zero; every original public column is stored at its public zero-based index plus one. Retain the ordinary public metadata independently and exclude stored position zero from public metadata, `has_values`, `column_count`, positional rows, filters, sorts and grouping. This adds no second cache, `ALTER`, `UPDATE` or rescan.

The page query forms one internal `result_view` over that cache and resolves every public zero-based column index to its private physical position. It never uses user-supplied column names or DuckDB `rowid`; duplicate output names, dotted aliases and an output column named `rowid` therefore remain unambiguous. The private ordinal is not a public column and is the final ordering tie-breaker for every page, giving a stable cache snapshot across offsets. It freezes the execution order supplied by the accepted query; it does not invent an SQL ordering where the query supplied none.

The accepted grid transform has zero or more filters combined with AND, zero or more sort entries, and at most one `group_by` column. A filter is exactly case-insensitive `contains` over the string rendering of its resolved cached value. Bind the filter value as a DuckDB parameter and use literal containment semantics, such as `instr(lower(CAST(value AS VARCHAR)), lower(?)) > 0`; `%`, `_`, quotes and other input have no wildcard or SQL meaning. Apply every ordering and grouping operation natively in DuckDB. Each user-directed sort and the one optional group order uses `ASC` or `DESC` with `NULLS LAST`; grouping order precedes requested sorting and the private snapshot ordinal resolves all remaining ties. Do not add nested grouping or sort-by-group-count in this pass.

When grouping is requested, compute each group count with a native window `COUNT(*) OVER (PARTITION BY resolved_group_column)` before offset and limit. Return group records only for group values represented in the delivered page, but each record's count is global to the complete filtered result. Filtering, sorting, grouping and paging are derived reads from the single cache, not stored result state.

Validate a grid shape, all indices, directions, filter operators and values before reading or releasing a result. A rejected grid request returns its input error and leaves the cached result available and unchanged.
