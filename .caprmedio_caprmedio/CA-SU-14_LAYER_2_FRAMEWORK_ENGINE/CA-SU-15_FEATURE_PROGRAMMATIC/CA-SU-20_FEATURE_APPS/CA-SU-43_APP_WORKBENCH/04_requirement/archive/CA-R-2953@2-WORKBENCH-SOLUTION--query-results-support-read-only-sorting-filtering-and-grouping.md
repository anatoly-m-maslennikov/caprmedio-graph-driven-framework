---
identity:
  atom_id: CA-R-2953@2
  ref_id: CA-R-2953@2
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
  version: 2
  updated_at: 2026-11-09 00:09:26 +0400
destination:
  file:
    name: CA-R-2953@2-WORKBENCH-SOLUTION--query-results-support-read-only-sorting-filtering-and-grouping.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement/archive
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
author: Anatoly Maslennikov
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
