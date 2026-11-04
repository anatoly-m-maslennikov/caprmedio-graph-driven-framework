---
atom_id: CA-D-674
current_scope_unit: WORKBENCH
claim_target_scope_unit: WORKBENCH
status: Active
version: 2
author: Anatoly Maslennikov
role: Delivery
form: Eng Decision
tier: 4
subjects:
  active: CAPRMEDIO_MODEL <+ Projection
relations:
  delivery_for:
  - CA-R-2727
carrier_destination:
  file:
    name: CA-D-674-WORKBENCH-ENG_DECISION--deliver-simple-sql-query-page.md
    path: .caprmedio_caprmedio/CA-SU-14_LAYER_2_FRAMEWORK_ENGINE/CA-SU-15_FEATURE_PROGRAMMATIC/CA-SU-20_FEATURE_APPS/CA-SU-43_APP_WORKBENCH/07_delivery
updated_at: 2026-11-04 00:38:14 +0400
---

## Summary

Deliver a simple SQL query page through the shared connector

## Claim scope

The local web representation of the in-memory DuckDB Projection.

## Claim

### Prose Claim

The existing application must deliver one small query page with a SQL text area, Check and Run buttons, row and column counts, ordinary result rows, and query errors. Check shows validity and exact counts or the query error; Run shows ordinary result rows and their counts through the shared connector.

The page remains inside the existing local application boundary. It does not add a second query evaluator, web service, renderer, or custom TABLE, DOC, or TREE result view. It need not materialize or display all rows at once, and this Draft defines no UI truncation or pagination policy.

