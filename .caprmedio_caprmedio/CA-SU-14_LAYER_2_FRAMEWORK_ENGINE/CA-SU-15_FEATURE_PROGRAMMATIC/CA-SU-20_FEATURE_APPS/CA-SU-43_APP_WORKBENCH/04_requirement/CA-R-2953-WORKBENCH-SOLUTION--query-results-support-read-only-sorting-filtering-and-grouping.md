---
identity:
  atom_id: CA-R-2953
  ref_id: CA-R-2953
context:
  container:
    scope_unit: CA-SU-43
  role: Requirement
  form: Solution
  topics:
    main_subject: MODEL//CAPRMEDIO <+ Projection
  tier: 3
state:
  status: Active
  version: 5
  updated_at: 2026-11-10 20:47:54 +0400
destination:
  file:
    name: CA-R-2953-WORKBENCH-SOLUTION--query-results-support-read-only-sorting-filtering-and-grouping.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
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

Grid transforms operate read-only over the entire existing materialized result before pagination: multi-column sort, AND case-insensitive literal `contains` filters, and at most one ascending/descending group with exact filtered-global counts even across pages. Submitted SQL/cache values/duplicate labels/positional values remain unchanged; show filtered/original counts and reuse paging. Expose only Cell Copy value/Show full value, Row Copy row, Sort asc/desc, Group by, Filter, Clear filter; copy/show full values regardless visible limit. MCP has same page semantics; nested grouping and sort-by-count remain deferred.

`query_page`/`view_fetch` optional `grid` accepts ordered zero-based sort, AND contains filters with string values, and zero-or-one group object, all lowercase `asc`/`desc`/`contains`. Omission is unfiltered page. Reject unknown fields/shapes/indices/directions/operators/value types before SQL/cache change. Responses retain identity/count/paging and no SQL echo: rows are positional; `row_count` filtered total; `source_row_count` original total; original ordered `columns` retain duplicate names/whole-cache `has_values`; page groups are `{value,count}` for represented values with global count. Default remains completed file descriptor; inline pages share this shape.

Use stable page ordering with group order before sort and nulls last; ties retain result order. Filter values are literal: `%`, `_` and quotes have no special meaning. Do not persist grid state or re-execute the query. Rejected requests leave the result available unchanged.
