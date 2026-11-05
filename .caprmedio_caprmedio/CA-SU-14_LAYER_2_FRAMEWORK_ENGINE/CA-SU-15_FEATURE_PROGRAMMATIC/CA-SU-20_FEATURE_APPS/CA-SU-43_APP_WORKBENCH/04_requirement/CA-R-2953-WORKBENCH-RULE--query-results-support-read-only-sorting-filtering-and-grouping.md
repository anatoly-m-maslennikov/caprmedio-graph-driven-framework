---
atom_id: CA-R-2953
ref_id: CA-R-2953
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
version: 1
author: Anatoly Maslennikov
role: Requirement
form: Rule
tier: 3
topics:
  main_subject: CAPRMEDIO_MODEL <+ Projection
updated_at: 2026-11-05 20:27:41 +0400
carrier_destination:
  file:
    name: CA-R-2953-WORKBENCH-RULE--query-results-support-read-only-sorting-filtering-and-grouping.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/04_requirement
container:
  scope_unit: CA-SU-43
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
