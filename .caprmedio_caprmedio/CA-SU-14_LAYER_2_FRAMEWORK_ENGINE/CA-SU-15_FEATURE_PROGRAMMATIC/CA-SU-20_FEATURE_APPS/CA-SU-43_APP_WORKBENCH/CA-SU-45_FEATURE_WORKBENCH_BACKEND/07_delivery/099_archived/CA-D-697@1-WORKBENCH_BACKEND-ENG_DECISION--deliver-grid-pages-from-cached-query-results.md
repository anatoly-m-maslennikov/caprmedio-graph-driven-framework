---
atom_id: CA-D-697
ref_id: CA-D-697@1
container:
  scope_unit: CA-SU-45
role: Delivery
form: Eng Decision
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
tier: 4
relations:
  delivery_for:
  - CA-M-462
  - CA-M-493
  - CA-O-240
  - CA-E-784
status: Archived
version: 1
updated_at: 2026-11-05 20:32:03 +0400
carrier_destination:
  file:
    name: CA-D-697@1-WORKBENCH_BACKEND-ENG_DECISION--deliver-grid-pages-from-cached-query-results.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/CA-SU-45_FEATURE_WORKBENCH_BACKEND/07_delivery/archived
current_scope_unit: WORKBENCH_BACKEND
claim_target_scope_unit: WORKBENCH_BACKEND
author: Anatoly Maslennikov
---

## Summary

Deliver grid pages from cached query results

## Claim

### Prose Claim

`query_page` and `view_fetch` accept an optional `grid` object in addition to their existing result identity and paging arguments. Omission keeps the existing unfiltered page behavior. A supplied grid contains only these optional members:

```json
{
  "sort": [{"column": 0, "direction": "asc"}],
  "filters": [{"column": 1, "operator": "contains", "value": "draft"}],
  "group_by": {"column": 2, "direction": "asc"}
}
```

`column` is a zero-based integer into the original ordered result metadata. `direction` is exactly lowercase `asc` or `desc`. `sort` is an ordered, multi-column list; `filters` is an AND list whose only operator is exactly lowercase `contains` and whose `value` is a string; and `group_by` is absent or exactly one column/direction object. Unknown fields, non-object/list shapes, non-string filter values, invalid directions or operators, and an out-of-range index are rejected without reading SQL or mutating cache state.

Both operations retain the existing result identity, SQL, column count and ordinary paging fields. Their page payload additionally and consistently has these meanings:

| Field | Meaning |
| --- | --- |
| `rows` | Positional values from the requested offset/page size after all grid filters and orders. |
| `row_count` | Exact count of the filtered result before offset and page limit. |
| `source_row_count` | Exact count of the original materialized result before grid filtering. |
| `columns` | The original ordered result metadata, including duplicate names and `has_values` calculated over the original whole cache, not over a filtered result or page. |
| `groups` | Omitted without `group_by`; otherwise an ordered list of `{value, count}` for distinct group values represented by `rows` on this page. `count` is the complete filtered count for that value, not the page count. |

`has_more` is derived from `row_count`, offset and delivered page size. `groups` has no nested children and has no entries for groups absent from the page. An empty page returns an empty `rows` collection and, when grouping, an empty `groups` collection without changing original metadata.

Expose the same request and response through MCP and the Workbench backend interface. The browser may use the response in a read-only Tabulator grid; cell copy/full value, row copy, column sort/group/filter/clear controls are frontend behavior and do not authorize mutation. Do not add a second grid endpoint, persisted grid state, raw SQL grid clause, result re-execution or a new service.
